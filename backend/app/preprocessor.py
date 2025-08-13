"""
COAI Prompt Preprocessor Module
Handles prompt preparation and enhancement for AI agents
"""

import logging
from datetime import datetime
from typing import Dict, Any
from .file_context_manager import file_context_manager

logger = logging.getLogger(__name__)

class PromptPreprocessor:
    """
    Handles prompt preprocessing for AI agents
    """
    
    def __init__(self):
        self.default_context = {
            "system_role": "You are COAI, an AI assistant that helps with coding and project management.",
            "language": "English",
            "response_format": "Clear and helpful"
        }
    
    def process_prompt(self, message: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a user message and prepare it for AI agent
        
        Args:
            message: User's input message
            context: Project context (project, file, etc.)
            
        Returns:
            Dictionary with processed prompt and metadata
        """
        try:
            # Validate inputs
            if not message or not message.strip():
                raise ValueError("Message cannot be empty")
                
            # Extract key information
            project = context.get("project", "unknown")
            file = context.get("file", "unknown")
            
            # Build enhanced prompt
            enhanced_prompt = self._build_prompt(message, context)
            
            # Prepare metadata
            metadata = {
                "original_message": message,
                "project": project,
                "file": file,
                "processed_at": datetime.now().isoformat(),
                "prompt_length": len(enhanced_prompt),
                "language": self._detect_language(message)
            }
            
            logger.info(f"Processed prompt for project: {project}, file: {file}")
            
            return {
                "enhanced_prompt": enhanced_prompt,
                "metadata": metadata,
                "context": context,
                "status": "ready_for_agent"
            }
            
        except Exception as e:
            logger.error(f"Error processing prompt: {str(e)}")
            raise
    
    def _build_prompt(self, message: str, context: Dict[str, Any]) -> str:
        """
        Build enhanced prompt with context and file information when needed
        """
        project = context.get("project", "unknown")
        file = context.get("file", "unknown")
        
        prompt_parts = [
            "=== COAI System Context ===",
            f"Project: {project}",
            f"Current File: {file}",
            f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
        ]
        
        # Check if this request needs file context
        if file_context_manager.should_include_file_context(message):
            logger.info(f"Including file context for project: {project}")
            file_data = file_context_manager.get_project_file_listing(project)
            file_context_text = file_context_manager.format_file_context_for_ai(file_data)
            
            prompt_parts.extend([
                "=== PROJECT FILE INFORMATION ===",
                file_context_text,
                "",
            ])
        
        prompt_parts.extend([
            "=== System Instructions ===",
            self.default_context["system_role"],
            "Please respond in English with clear, actionable advice.",
            "If this involves code, provide specific examples.",
            "If asked about project files, use the file structure information provided above.",
            "",
            "=== User Query ===",
            message,
            "",
            "=== Response Guidelines ===",
            "- Be concise but thorough",
            "- Include code examples when relevant", 
            "- Consider the project context and file structure",
            "- Provide actionable next steps"
        ])
        
        return "\n".join(prompt_parts)
    
    def _detect_language(self, message: str) -> str:
        """
        Simple language detection (can be enhanced later)
        """
        # Simple heuristic - check for Lithuanian characters
        lithuanian_chars = set("ąčęėįšųūž")
        if any(char.lower() in lithuanian_chars for char in message):
            return "Lithuanian"
        return "English"
    
    def optimize_for_agent(self, prompt_data: Dict[str, Any], agent_type: str = "copilot") -> str:
        """
        Optimize prompt for specific AI agent type
        """
        enhanced_prompt = prompt_data.get("enhanced_prompt", "")
        
        if agent_type == "copilot":
            # Optimize for GitHub Copilot
            return f"# GitHub Copilot Request\n\n{enhanced_prompt}"
        elif agent_type == "openai":
            # Optimize for OpenAI API
            return enhanced_prompt
        else:
            return enhanced_prompt

# Global preprocessor instance
preprocessor = PromptPreprocessor()
