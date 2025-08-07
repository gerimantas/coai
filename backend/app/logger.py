"""
COAI Logging Module
Handles action logging for queries, prompts, and responses
"""

import json
import logging
import os
from datetime import datetime
from typing import Dict, Any

class COAILogger:
    """
    Handles COAI-specific logging for actions, queries, and responses
    """
    
    def __init__(self, log_dir: str = None):
        if log_dir is None:
            # Default to .coai/logs directory
            log_dir = os.path.join(os.path.dirname(__file__), "..", "..", ".coai", "logs")
        
        self.log_dir = log_dir
        self.actions_log = os.path.join(log_dir, "actions.log")
        self.chat_log = os.path.join(log_dir, "chat_history.json")
        
        # Ensure log directory exists
        os.makedirs(log_dir, exist_ok=True)
        
        # Setup logger
        self.logger = logging.getLogger("coai")
        self.logger.setLevel(logging.INFO)
        
        # File handler for actions
        if not self.logger.handlers:
            handler = logging.FileHandler(self.actions_log)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def log_chat_request(self, message: str, context: Dict[str, Any]) -> str:
        """
        Log a chat request
        
        Returns:
            Request ID for tracking
        """
        request_id = f"req_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
        
        log_entry = {
            "request_id": request_id,
            "timestamp": datetime.now().isoformat(),
            "type": "chat_request",
            "message": message,
            "context": context
        }
        
        self.logger.info(f"Chat request: {request_id} - Project: {context.get('project')} - Message: {message[:50]}...")
        self._append_to_chat_history(log_entry)
        
        return request_id
    
    def log_prompt_processing(self, request_id: str, original_prompt: str, enhanced_prompt: str, metadata: Dict[str, Any]):
        """
        Log prompt processing details
        """
        log_entry = {
            "request_id": request_id,
            "timestamp": datetime.now().isoformat(),
            "type": "prompt_processing",
            "original_prompt": original_prompt,
            "enhanced_prompt": enhanced_prompt,
            "metadata": metadata
        }
        
        self.logger.info(f"Prompt processed: {request_id} - Length: {metadata.get('prompt_length', 0)}")
        self._append_to_chat_history(log_entry)
    
    def log_ai_response(self, request_id: str, response: str, agent_type: str = "unknown"):
        """
        Log AI agent response
        """
        log_entry = {
            "request_id": request_id,
            "timestamp": datetime.now().isoformat(),
            "type": "ai_response",
            "response": response,
            "agent_type": agent_type
        }
        
        self.logger.info(f"AI response: {request_id} - Agent: {agent_type} - Response length: {len(response)}")
        self._append_to_chat_history(log_entry)
    
    def log_error(self, request_id: str, error: str, context: Dict[str, Any] = None):
        """
        Log an error
        """
        log_entry = {
            "request_id": request_id,
            "timestamp": datetime.now().isoformat(),
            "type": "error",
            "error": error,
            "context": context or {}
        }
        
        self.logger.error(f"Error: {request_id} - {error}")
        self._append_to_chat_history(log_entry)
    
    def _append_to_chat_history(self, entry: Dict[str, Any]):
        """
        Append entry to chat history JSON file
        """
        try:
            # Read existing history
            history = []
            if os.path.exists(self.chat_log):
                with open(self.chat_log, 'r', encoding='utf-8') as f:
                    history = json.load(f)
            
            # Append new entry
            history.append(entry)
            
            # Keep only last 1000 entries to prevent file from growing too large
            if len(history) > 1000:
                history = history[-1000:]
            
            # Write back to file
            with open(self.chat_log, 'w', encoding='utf-8') as f:
                json.dump(history, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.logger.error(f"Failed to write to chat history: {str(e)}")
    
    def get_chat_history(self, limit: int = 50) -> list:
        """
        Get recent chat history
        """
        try:
            if os.path.exists(self.chat_log):
                with open(self.chat_log, 'r', encoding='utf-8') as f:
                    history = json.load(f)
                return history[-limit:] if limit else history
            return []
        except Exception as e:
            self.logger.error(f"Failed to read chat history: {str(e)}")
            return []

# Global logger instance
coai_logger = COAILogger()
