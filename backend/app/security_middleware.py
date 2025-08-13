"""
Performance and Security Middleware
Rate limiting, caching, and security validation
"""
import time
import hashlib
import json
from functools import wraps
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
from collections import defaultdict, deque
import os
import logging

logger = logging.getLogger(__name__)

class RateLimiter:
    """Simple in-memory rate limiter"""
    
    def __init__(self):
        self.requests = defaultdict(deque)
        self.blocked_ips = defaultdict(datetime)
    
    def is_allowed(self, ip: str, limit: int = 100, window: int = 3600) -> bool:
        """Check if request is allowed based on rate limits"""
        now = time.time()
        window_start = now - window
        
        # Clean old requests
        while self.requests[ip] and self.requests[ip][0] < window_start:
            self.requests[ip].popleft()
        
        # Check if IP is temporarily blocked
        if ip in self.blocked_ips:
            if datetime.now() < self.blocked_ips[ip]:
                return False
            else:
                del self.blocked_ips[ip]
        
        # Check rate limit
        if len(self.requests[ip]) >= limit:
            # Block IP for 1 hour
            self.blocked_ips[ip] = datetime.now() + timedelta(hours=1)
            logger.warning(f"Rate limit exceeded for IP {ip}, blocking for 1 hour")
            return False
        
        # Add current request
        self.requests[ip].append(now)
        return True

class RequestCache:
    """Simple in-memory request cache"""
    
    def __init__(self, max_size: int = 1000, ttl: int = 300):
        self.cache: Dict[str, tuple] = {}
        self.max_size = max_size
        self.ttl = ttl
    
    def _generate_key(self, data: Any) -> str:
        """Generate cache key from request data"""
        cache_data = json.dumps(data, sort_keys=True)
        return hashlib.md5(cache_data.encode()).hexdigest()
    
    def get(self, key_data: Any) -> Optional[Any]:
        """Get cached response"""
        key = self._generate_key(key_data)
        
        if key in self.cache:
            value, timestamp = self.cache[key]
            
            # Check if expired
            if time.time() - timestamp > self.ttl:
                del self.cache[key]
                return None
            
            return value
        
        return None
    
    def set(self, key_data: Any, value: Any) -> None:
        """Cache response"""
        key = self._generate_key(key_data)
        
        # Clean cache if too large
        if len(self.cache) >= self.max_size:
            # Remove oldest entries
            oldest_keys = sorted(self.cache.keys(), 
                               key=lambda k: self.cache[k][1])[:100]
            for old_key in oldest_keys:
                del self.cache[old_key]
        
        self.cache[key] = (value, time.time())

class SecurityValidator:
    """Security validation and auditing"""
    
    def __init__(self):
        self.allowed_base_paths = os.getenv('ALLOWED_BASE_PATHS', '').split(',')
        self.max_file_size = int(os.getenv('MAX_FILE_SIZE', 10485760))  # 10MB
        self.max_message_length = int(os.getenv('MAX_MESSAGE_LENGTH', 10000))
    
    def validate_file_path(self, file_path: str) -> bool:
        """Validate file access is within allowed paths"""
        if not file_path:
            return False
        
        abs_path = os.path.abspath(file_path)
        
        # Check against allowed base paths
        for base_path in self.allowed_base_paths:
            if base_path.strip() and abs_path.startswith(os.path.abspath(base_path.strip())):
                return True
        
        return False
    
    def validate_file_size(self, file_path: str) -> bool:
        """Check file size limits"""
        try:
            if os.path.exists(file_path):
                size = os.path.getsize(file_path)
                return size <= self.max_file_size
        except OSError:
            return False
        return True
    
    def validate_message(self, message: str) -> bool:
        """Validate message content and length"""
        if not message or len(message) > self.max_message_length:
            return False
        
        # Check for suspicious patterns
        suspicious_patterns = [
            '../', '..\\',  # Directory traversal
            'rm -rf', 'del /f',  # Dangerous commands
            '<script', 'javascript:',  # XSS attempts
        ]
        
        message_lower = message.lower()
        for pattern in suspicious_patterns:
            if pattern in message_lower:
                logger.warning(f"Suspicious pattern detected: {pattern}")
                return False
        
        return True
    
    def log_security_event(self, event_type: str, ip: str, details: str):
        """Log security events for audit"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'event_type': event_type,
            'ip_address': ip,
            'details': details
        }
        
        # Create security log directory
        security_log_dir = os.path.join('.coai', 'logs', 'security')
        os.makedirs(security_log_dir, exist_ok=True)
        
        # Write to daily security log
        log_file = os.path.join(security_log_dir, 
                               f"security_{datetime.now().strftime('%Y%m%d')}.log")
        
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry) + '\n')
        
        logger.warning(f"Security event: {event_type} from {ip} - {details}")

# Global instances
rate_limiter = RateLimiter()
request_cache = RequestCache()
security_validator = SecurityValidator()

def rate_limit(limit: int = None, window: int = None):
    """Rate limiting decorator"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            from flask import request, jsonify
            
            # Get configuration
            actual_limit = limit or int(os.getenv('RATE_LIMIT_REQUESTS', 100))
            actual_window = window or int(os.getenv('RATE_LIMIT_WINDOW', 3600))
            
            # Get client IP
            ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
            
            if not rate_limiter.is_allowed(ip, actual_limit, actual_window):
                security_validator.log_security_event(
                    'RATE_LIMIT_EXCEEDED', ip, 
                    f"Limit: {actual_limit} requests per {actual_window}s"
                )
                return jsonify({
                    'error': 'Rate limit exceeded',
                    'message': 'Too many requests. Please try again later.',
                    'retry_after': 3600
                }), 429
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def cache_response(ttl: int = 300):
    """Response caching decorator"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            from flask import request
            
            # Only cache GET requests
            if request.method != 'GET':
                return f(*args, **kwargs)
            
            # Generate cache key from request
            cache_key = {
                'url': request.url,
                'args': request.args.to_dict(),
                'view_args': request.view_args
            }
            
            # Try to get from cache
            cached_response = request_cache.get(cache_key)
            if cached_response:
                logger.debug(f"Cache hit for {request.url}")
                return cached_response
            
            # Execute function and cache result
            response = f(*args, **kwargs)
            request_cache.set(cache_key, response)
            logger.debug(f"Cached response for {request.url}")
            
            return response
        return decorated_function
    return decorator

def validate_security():
    """Security validation decorator"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            from flask import request, jsonify
            
            ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
            
            # Validate request data
            if request.is_json:
                data = request.get_json()
                
                # Validate message content
                message = data.get('message', '')
                if message and not security_validator.validate_message(message):
                    security_validator.log_security_event(
                        'INVALID_MESSAGE', ip, f"Suspicious message content"
                    )
                    return jsonify({
                        'error': 'Invalid message content',
                        'message': 'Message contains suspicious content'
                    }), 400
                
                # Validate file paths
                project_path = data.get('project_path', '')
                if project_path and not security_validator.validate_file_path(project_path):
                    security_validator.log_security_event(
                        'INVALID_FILE_PATH', ip, f"Access denied to path: {project_path}"
                    )
                    return jsonify({
                        'error': 'Access denied',
                        'message': 'File path not allowed'
                    }), 403
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator
