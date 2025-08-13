"""
Enhanced Error Handling for COAI System - Stage 2
Provides comprehensive error handling, logging, and user-friendly messages
"""

import logging
import traceback
import os
from datetime import datetime
from typing import Dict, Any, Optional
from flask import jsonify

# Setup enhanced logging
def setup_error_logging():
    """Setup comprehensive error logging system"""
    
    # Create logs directory
    logs_dir = os.path.join(os.path.dirname(__file__), '..', '.coai', 'logs')
    os.makedirs(logs_dir, exist_ok=True)
    
    # Setup error logger
    error_logger = logging.getLogger('coai_errors')
    error_logger.setLevel(logging.ERROR)
    
    # File handler for error logs
    error_file = os.path.join(logs_dir, 'errors.log')
    error_handler = logging.FileHandler(error_file)
    error_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    error_handler.setFormatter(error_formatter)
    error_logger.addHandler(error_handler)
    
    return error_logger

# Initialize error logger
error_logger = setup_error_logging()

class COAIError(Exception):
    """Base exception class for COAI system"""
    def __init__(self, message: str, error_code: str = None, details: Dict = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code or "COAI_ERROR"
        self.details = details or {}
        self.timestamp = datetime.now().isoformat()

class AIAgentError(COAIError):
    """Errors related to AI agent processing"""
    def __init__(self, message: str, agent_type: str = None, **kwargs):
        super().__init__(message, "AI_AGENT_ERROR", kwargs)
        self.agent_type = agent_type

class ValidationError(COAIError):
    """Input validation errors"""
    def __init__(self, message: str, field: str = None, **kwargs):
        super().__init__(message, "VALIDATION_ERROR", kwargs)
        self.field = field

class ConfigurationError(COAIError):
    """Configuration and environment errors"""
    def __init__(self, message: str, config_key: str = None, **kwargs):
        super().__init__(message, "CONFIG_ERROR", kwargs)
        self.config_key = config_key

class FileAccessError(COAIError):
    """File system access errors"""
    def __init__(self, message: str, file_path: str = None, **kwargs):
        super().__init__(message, "FILE_ACCESS_ERROR", kwargs)
        self.file_path = file_path

def log_error(error: Exception, context: Dict[str, Any] = None):
    """Log error with comprehensive context information"""
    
    context = context or {}
    
    error_data = {
        "error_type": type(error).__name__,
        "error_message": str(error),
        "timestamp": datetime.now().isoformat(),
        "context": context,
        "traceback": traceback.format_exc()
    }
    
    # Add COAI-specific error details if available
    if isinstance(error, COAIError):
        error_data.update({
            "error_code": error.error_code,
            "details": error.details
        })
    
    error_logger.error(f"COAI Error: {error_data}")
    
    return error_data

def create_error_response(error: Exception, context: Dict[str, Any] = None) -> Dict[str, Any]:
    """Create user-friendly error response"""
    
    # Log the error
    error_data = log_error(error, context)
    
    # Create user-friendly response
    if isinstance(error, AIAgentError):
        user_message = "AI service is currently experiencing issues. Please try again in a moment."
        fallback_available = True
    elif isinstance(error, ValidationError):
        user_message = f"Invalid input: {error.message}"
        fallback_available = False
    elif isinstance(error, ConfigurationError):
        user_message = "System configuration issue. Please check your settings."
        fallback_available = False
    elif isinstance(error, FileAccessError):
        user_message = "Unable to access the requested file. Please check the file path."
        fallback_available = False
    else:
        user_message = "An unexpected error occurred. Our team has been notified."
        fallback_available = True
    
    response = {
        "status": "error",
        "error": True,
        "message": user_message,
        "error_code": getattr(error, 'error_code', 'UNKNOWN_ERROR'),
        "timestamp": datetime.now().isoformat(),
        "fallback_available": fallback_available
    }
    
    # Add request context if available
    if context:
        response["request_id"] = context.get("request_id")
        response["project"] = context.get("project")
        response["file"] = context.get("file")
    
    # In debug mode, add more details
    debug_mode = os.getenv('DEBUG_MODE', 'false').lower() == 'true'
    if debug_mode:
        response["debug"] = {
            "error_type": type(error).__name__,
            "error_details": str(error),
            "traceback": traceback.format_exc().split('\n')[-10:]  # Last 10 lines
        }
    
    return response

def handle_api_errors(func):
    """Decorator for comprehensive API error handling"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AIAgentError as e:
            error_response = create_error_response(e, kwargs.get('context'))
            return jsonify(error_response), 503  # Service Unavailable
        except ValidationError as e:
            error_response = create_error_response(e, kwargs.get('context'))
            return jsonify(error_response), 400  # Bad Request
        except ConfigurationError as e:
            error_response = create_error_response(e, kwargs.get('context'))
            return jsonify(error_response), 500  # Internal Server Error
        except FileAccessError as e:
            error_response = create_error_response(e, kwargs.get('context'))
            return jsonify(error_response), 404  # Not Found
        except Exception as e:
            error_response = create_error_response(e, kwargs.get('context'))
            return jsonify(error_response), 500  # Internal Server Error
    return wrapper

def validate_chat_request(data: Dict[str, Any]) -> None:
    """Validate chat request data"""
    
    if not data:
        raise ValidationError("Request body is required")
    
    message = data.get("message", "").strip()
    if not message:
        raise ValidationError("Message cannot be empty", field="message")
    
    if len(message) > int(os.getenv('MAX_MESSAGE_LENGTH', '10000')):
        raise ValidationError(
            f"Message too long (max {os.getenv('MAX_MESSAGE_LENGTH', '10000')} characters)",
            field="message"
        )
    
    project = data.get("project", "").strip()
    if not project:
        raise ValidationError("Project name is required", field="project")
    
    file_name = data.get("file", "").strip()
    if not file_name:
        raise ValidationError("File name is required", field="file")

def validate_file_access(file_path: str) -> None:
    """Validate file access permissions and security"""
    
    if not file_path:
        raise FileAccessError("File path cannot be empty")
    
    # Security check - ensure file is within allowed paths
    allowed_paths = os.getenv('ALLOWED_BASE_PATHS', 'C:/ai_projects').split(',')
    file_path_abs = os.path.abspath(file_path)
    
    allowed = False
    for allowed_path in allowed_paths:
        if file_path_abs.startswith(os.path.abspath(allowed_path.strip())):
            allowed = True
            break
    
    if not allowed:
        raise FileAccessError(f"File access denied: {file_path}", file_path=file_path)
    
    # Check if file exists and is readable
    if not os.path.exists(file_path):
        raise FileAccessError(f"File not found: {file_path}", file_path=file_path)
    
    if not os.path.isfile(file_path):
        raise FileAccessError(f"Path is not a file: {file_path}", file_path=file_path)
    
    # Check file size
    max_size = int(os.getenv('MAX_FILE_SIZE', '10485760'))  # 10MB default
    if os.path.getsize(file_path) > max_size:
        raise FileAccessError(f"File too large (max {max_size} bytes)", file_path=file_path)

def check_system_health() -> Dict[str, Any]:
    """Check overall system health and configuration"""
    
    health_status = {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "checks": {}
    }
    
    try:
        # Check environment configuration
        required_env_vars = ['OPENAI_API_KEY', 'DEFAULT_AI_AGENT']
        for var in required_env_vars:
            value = os.getenv(var)
            health_status["checks"][var] = {
                "configured": bool(value and value != 'your_key_here'),
                "value_length": len(value) if value else 0
            }
        
        # Check logs directory
        logs_dir = os.path.join(os.path.dirname(__file__), '..', '.coai', 'logs')
        health_status["checks"]["logs_directory"] = {
            "exists": os.path.exists(logs_dir),
            "writable": os.access(logs_dir, os.W_OK) if os.path.exists(logs_dir) else False
        }
        
        # Check if any critical issues
        critical_issues = []
        if not health_status["checks"].get("OPENAI_API_KEY", {}).get("configured"):
            critical_issues.append("OpenAI API key not configured")
        
        if critical_issues:
            health_status["status"] = "degraded"
            health_status["critical_issues"] = critical_issues
        
    except Exception as e:
        health_status["status"] = "unhealthy"
        health_status["error"] = str(e)
    
    return health_status
