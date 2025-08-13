"""
COAI Orchestrator Module
Coordinates communication between frontend, preprocessor, and AI agents
"""

import os
import logging
from datetime import datetime
from typing import Dict, Any, Optional
from .preprocessor import preprocessor
from .logger import coai_logger

# Try to import full AI agents first, fallback to basic if needed
try:
    # Check if real AI is enabled
    enable_real_ai = os.getenv('ENABLE_REAL_AI', 'false').lower() == 'true'
    if enable_real_ai:
        from .ai_agents_full import ai_agent_manager
        logger = logging.getLogger(__name__)
        logger.info("Using full AI agents implementation with OpenAI")
    else:
        from .ai_agents import ai_agent_manager
        logger = logging.getLogger(__name__)
        logger.info("Using mock AI agents implementation")
except ImportError as e:
    logger = logging.getLogger(__name__)
    logger.warning(f"Failed to import full AI agents, falling back to mock: {e}")
    from .ai_agents import ai_agent_manager

class COAIOrchestrator:
    """
    Main orchestrator that coordinates all COAI components
    """
    
    def __init__(self):
        self.components = {
            "preprocessor": preprocessor,
            "logger": coai_logger,
            "ai_agents": ai_agent_manager
        }
        self.status = "initialized"
        logger.info("COAI Orchestrator initialized")
    
    def process_chat_request(self, message: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main orchestration method for chat requests
        
        Flow: Frontend → Preprocessor → Orchestrator → AI Agent → Response
        
        Args:
            message: User's message
            context: Request context (project, file, etc.)
            
        Returns:
            Processed response ready for frontend
        """
        request_id = None
        
        try:
            # Step 1: Log incoming request
            request_id = coai_logger.log_chat_request(message, context)
            logger.info(f"Orchestrator processing request: {request_id}")
            
            # Step 2: Validate input
            validation_result = self._validate_request(message, context)
            if not validation_result["valid"]:
                raise ValueError(validation_result["error"])
            
            # Step 3: Preprocess the prompt
            logger.info(f"Step 1/4: Preprocessing prompt for {request_id}")
            processed_data = preprocessor.process_prompt(message, context)
            
            # Step 4: Log preprocessing
            coai_logger.log_prompt_processing(
                request_id,
                message,
                processed_data["enhanced_prompt"],
                processed_data["metadata"]
            )
            
            # Step 5: Call AI agent (real implementation)
            logger.info(f"Step 2/4: Calling AI agent for {request_id}")
            ai_request = {
                "message": processed_data["enhanced_prompt"],
                "metadata": processed_data["metadata"],
                "request_id": request_id
            }
            ai_result = ai_agent_manager.process_request(ai_request)
            
            if ai_result.get("status") != "success":
                # Fallback to simulation if AI agent fails
                logger.warning(f"AI agent failed for {request_id}, falling back to simulation")
                ai_response = self._simulate_ai_response(processed_data)
                agent_type = "simulated_fallback"
            else:
                ai_response = ai_result["response"]
                agent_type = ai_result.get("agent_type", "unknown")
            
            # Step 6: Log AI response
            logger.info(f"Step 3/4: Processing AI response for {request_id}")
            coai_logger.log_ai_response(request_id, ai_response, agent_type)
            
            # Step 7: Prepare final response
            logger.info(f"Step 4/4: Preparing final response for {request_id}")
            final_response = self._prepare_final_response(
                request_id, message, context, processed_data, ai_response, agent_type
            )
            
            logger.info(f"Orchestrator completed processing: {request_id}")
            return final_response
            
        except Exception as e:
            error_msg = f"Orchestrator error: {str(e)}"
            logger.error(f"{error_msg} for request: {request_id}")
            
            if request_id:
                coai_logger.log_error(request_id, error_msg, context)
            
            # Return error response
            return {
                "request_id": request_id,
                "error": True,
                "message": error_msg,
                "status": "orchestrator_error",
                "timestamp": datetime.now().isoformat()
            }
    
    def _validate_request(self, message: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate incoming request
        """
        if not message or not message.strip():
            return {"valid": False, "error": "Message cannot be empty"}
        
        if len(message) > 10000:  # Reasonable limit
            return {"valid": False, "error": "Message too long (max 10000 characters)"}
        
        required_context = ["project", "file"]
        for key in required_context:
            if key not in context:
                return {"valid": False, "error": f"Missing required context: {key}"}
        
        return {"valid": True}
    
    def _simulate_ai_response(self, processed_data: Dict[str, Any]) -> str:
        """
        Simulate AI agent response (MVP implementation)
        In the next phase, this will call actual AI agents
        """
        metadata = processed_data["metadata"]
        project = metadata.get("project", "unknown")
        file = metadata.get("file", "unknown")
        language = metadata.get("language", "English")
        
        # Generate contextual response based on project/file
        if "python" in file.lower() or file.endswith(".py"):
            response = f"""I see you're working on a Python file ({file}) in the {project} project. 

Here are some helpful suggestions:
- Make sure your code follows PEP 8 style guidelines
- Consider adding docstrings to your functions
- Use type hints for better code documentation
- Test your code with pytest

Would you like me to help you with any specific Python coding tasks?"""
        
        elif "javascript" in file.lower() or file.endswith((".js", ".ts", ".jsx", ".tsx")):
            response = f"""I see you're working on a JavaScript/TypeScript file ({file}) in the {project} project.

Here are some helpful suggestions:
- Use ESLint for code quality
- Consider using TypeScript for better type safety
- Follow modern ES6+ practices
- Use proper error handling with try/catch

How can I assist you with your JavaScript/TypeScript development?"""
        
        else:
            response = f"""I'm here to help with your {project} project, specifically with the {file} file.

I can assist you with:
- Code review and optimization
- Bug fixing and debugging
- Best practices and patterns
- Documentation and comments
- Testing strategies

What specific help do you need with your project?"""
        
        # Add language-specific note
        if language == "Lithuanian":
            response += "\n\n(Pastaba: Galiu atsakyti ir lietuviškai, jei pageidaujate)"
        
        return response
    
    def _prepare_final_response(
        self, 
        request_id: str, 
        original_message: str, 
        context: Dict[str, Any],
        processed_data: Dict[str, Any], 
        ai_response: str,
        agent_type: str = "unknown"
    ) -> Dict[str, Any]:
        """
        Prepare the final response for frontend
        """
        return {
            "request_id": request_id,
            "reply": ai_response,
            "original_message": original_message,
            "context": {
                "project": context.get("project"),
                "file": context.get("file"),
                "language": processed_data["metadata"].get("language"),
                "processed_at": datetime.now().isoformat()
            },
            "metadata": {
                "prompt_length": processed_data["metadata"].get("prompt_length"),
                "processing_time": "< 1s",
                "agent_type": agent_type,
                "orchestrator_version": "1.0.0"
            },
            "status": "completed",
            "error": False,
            "debug": {
                "enhanced_prompt_preview": processed_data["enhanced_prompt"][:100] + "...",
                "components_used": ["orchestrator", "preprocessor", "logger", f"ai_agent_{agent_type}"]
            }
        }
    
    def get_orchestrator_status(self) -> Dict[str, Any]:
        """
        Get current orchestrator status and component health
        """
        component_status = {}
        
        # Check each component
        for name, component in self.components.items():
            if component is None:
                component_status[name] = "not_initialized"
            else:
                component_status[name] = "ready"
        
        return {
            "orchestrator_status": self.status,
            "components": component_status,
            "version": "1.0.0",
            "capabilities": [
                "chat_request_processing",
                "prompt_preprocessing", 
                "request_logging",
                "ai_agent_integration",
                "openai_support",
                "copilot_simulation"
            ],
            "next_features": [
                "file_system_access",
                "project_management",
                "real_copilot_integration"
            ]
        }

# Global orchestrator instance
orchestrator = COAIOrchestrator()
