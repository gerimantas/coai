"""
COAI AI Agents Module - Full Implementation with OpenAI Integration
Handles real AI agents with actual OpenAI API integration
"""

import os
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

class OpenAIAgent:
    """
    Real OpenAI integration for COAI system
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.agent_type = "openai"
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
        self.max_tokens = int(os.getenv('OPENAI_MAX_TOKENS', '2000'))
        self.temperature = float(os.getenv('OPENAI_TEMPERATURE', '0.7'))
        self.fallback_to_mock = os.getenv('FALLBACK_TO_MOCK', 'true').lower() == 'true'
        
        # Initialize OpenAI client
        if self.api_key and self.api_key != 'your_openai_api_key_here':
            try:
                openai.api_key = self.api_key
                self.client = openai.OpenAI(api_key=self.api_key)
                self.is_configured = True
                logger.info("OpenAI client initialized successfully")
            except Exception as e:
                logger.warning(f"Failed to initialize OpenAI client: {e}")
                self.is_configured = False
        else:
            self.is_configured = False
            logger.warning("OpenAI API key not configured - will use mock responses")
    
    def process_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process request using real OpenAI API or fallback to mock
        """
        try:
            message = request.get('message', '')
            context = request.get('context', {})
            project = context.get('project', 'unknown')
            file_path = context.get('file', 'unknown')
            
            # Check if real AI is enabled and configured
            enable_real_ai = os.getenv('ENABLE_REAL_AI', 'false').lower() == 'true'
            
            if enable_real_ai and self.is_configured:
                return self._process_with_openai(message, context, project, file_path)
            else:
                logger.info("Using mock response (real AI disabled or not configured)")
                return self._process_with_mock(message, context, project, file_path)
                
        except Exception as e:
            logger.error(f"Error in OpenAI agent: {e}")
            if self.fallback_to_mock:
                logger.info("Falling back to mock response due to error")
                return self._process_with_mock(message, context, project, file_path)
            else:
                return {
                    "status": "error",
                    "agent_type": self.agent_type,
                    "error": str(e),
                    "timestamp": datetime.now().isoformat()
                }
    
    def _process_with_openai(self, message: str, context: Dict[str, Any], project: str, file_path: str) -> Dict[str, Any]:
        """Process request using real OpenAI API"""
        try:
            # Build system prompt based on context
            system_prompt = self._build_system_prompt(context, project, file_path)
            
            # Make OpenAI API call
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            ai_response = response.choices[0].message.content
            
            # Calculate usage metrics
            usage_info = {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens,
                "model": self.model
            }
            
            logger.info(f"OpenAI API call successful. Tokens used: {usage_info['total_tokens']}")
            
            return {
                "status": "success",
                "agent_type": self.agent_type,
                "response": ai_response,
                "timestamp": datetime.now().isoformat(),
                "usage": usage_info,
                "model": self.model,
                "real_ai": True
            }
            
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            raise e
    
    def _process_with_mock(self, message: str, context: Dict[str, Any], project: str, file_path: str) -> Dict[str, Any]:
        """Process request using mock responses"""
        
        # Intelligent mock responses based on message content
        response_text = self._generate_mock_response(message, project, file_path)
        
        return {
            "status": "success",
            "agent_type": self.agent_type,
            "response": response_text,
            "timestamp": datetime.now().isoformat(),
            "usage": {
                "prompt_tokens": len(message.split()),
                "completion_tokens": len(response_text.split()),
                "total_tokens": len(message.split()) + len(response_text.split()),
                "model": "mock"
            },
            "model": "mock",
            "real_ai": False
        }
    
    def _build_system_prompt(self, context: Dict[str, Any], project: str, file_path: str) -> str:
        """Build system prompt based on context and rules"""
        
        base_prompt = """You are COAI (Code-Oriented AI), an expert programming assistant focused on helping developers with code analysis, debugging, optimization, and development tasks.

Context:
- Project: {project}
- Current file: {file_path}
- You have access to project context and can help with multi-file scenarios
- Always provide practical, actionable advice
- Include code examples when relevant
- Be concise but thorough

Your capabilities include:
- Code review and suggestions
- Bug finding and debugging help
- Code optimization recommendations
- Documentation generation
- Testing strategy advice
- Architecture guidance"""
        
        # Add rules from context if available
        global_rules = context.get('global_rules', [])
        agent_rules = context.get('agent_rules', {}).get('openai', [])
        
        rules_text = ""
        if global_rules or agent_rules:
            rules_text = "\n\nAdditional rules to follow:\n"
            for rule in global_rules:
                rules_text += f"- {rule}\n"
            for rule in agent_rules:
                rules_text += f"- {rule}\n"
        
        return base_prompt.format(
            project=project,
            file_path=file_path
        ) + rules_text
    
    def _generate_mock_response(self, message: str, project: str, file_path: str) -> str:
        """Generate intelligent mock responses"""
        
        message_lower = message.lower()
        
        if any(word in message_lower for word in ['debug', 'error', 'bug', 'issue', 'problem']):
            return f"""I can help you debug the issue in {file_path}! Here's my analysis:

🔍 **Debugging Approach for {project}:**

1. **Check Common Issues:**
   - Verify imports and dependencies
   - Look for typos in variable names
   - Check indentation and syntax

2. **Add Logging:**
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   logger = logging.getLogger(__name__)
   logger.debug("Debug point reached")
   ```

3. **Test Incrementally:**
   - Isolate the problematic section
   - Test with simple inputs first
   - Use print statements for quick debugging

Would you like me to analyze specific error messages or code sections?"""

        elif any(word in message_lower for word in ['code', 'implement', 'function', 'class']):
            return f"""I'll help you implement that in {file_path}! Here's a structured approach:

💡 **Implementation for {project}:**

```python
# Example implementation
def your_function():
    '''
    Implement your functionality here
    '''
    pass

class YourClass:
    def __init__(self):
        self.initialized = True
    
    def process(self):
        # Your logic here
        return "Success"
```

**Best Practices:**
- Use descriptive variable names
- Add docstrings for documentation
- Include error handling
- Write unit tests

Need help with specific implementation details?"""

        elif any(word in message_lower for word in ['review', 'improve', 'optimize']):
            return f"""Let me review the code in {file_path} for {project}! 

🔧 **Code Review Insights:**

**Potential Improvements:**
- Consider using type hints for better code clarity
- Add error handling for robustness
- Look for opportunities to reduce complexity
- Ensure proper resource cleanup

**Performance Considerations:**
- Profile bottlenecks if performance is critical
- Consider caching for repeated operations
- Use appropriate data structures

**Code Quality:**
- Follow PEP 8 style guidelines
- Add comprehensive docstrings
- Consider breaking large functions into smaller ones

Share your code for more specific feedback!"""

        elif any(word in message_lower for word in ['test', 'testing', 'pytest']):
            return f"""I'll help you with testing for {project}! 

🧪 **Testing Strategy for {file_path}:**

```python
import pytest
import unittest

def test_your_function():
    # Arrange
    input_data = "test_input"
    expected = "expected_output"
    
    # Act
    result = your_function(input_data)
    
    # Assert
    assert result == expected

class TestYourClass(unittest.TestCase):
    def setUp(self):
        self.instance = YourClass()
    
    def test_basic_functionality(self):
        result = self.instance.process()
        self.assertIsNotNone(result)
```

**Testing Best Practices:**
- Write tests before or alongside code (TDD)
- Test edge cases and error conditions
- Maintain good test coverage
- Use descriptive test names

What specific functionality would you like to test?"""

        else:
            return f"""Hello! I'm COAI, ready to help with {project}. 

I can assist you with:
- **Code Review**: Analyze and improve your code
- **Debugging**: Find and fix issues
- **Implementation**: Write new functions and classes  
- **Testing**: Create comprehensive test suites
- **Documentation**: Generate clear documentation
- **Architecture**: Design system structure

Current context: `{file_path}`

How can I help you today? Feel free to share code, describe problems, or ask for implementation guidance!"""

    def get_capabilities(self) -> List[str]:
        """Return list of agent capabilities"""
        capabilities = [
            "code_review",
            "debugging_assistance", 
            "code_generation",
            "documentation_generation",
            "testing_guidance",
            "architecture_advice",
            "performance_optimization"
        ]
        
        if self.is_configured:
            capabilities.append("real_ai_integration")
        else:
            capabilities.append("mock_responses")
            
        return capabilities
    
    def get_status(self) -> Dict[str, Any]:
        """Get current agent status"""
        return {
            "agent_type": self.agent_type,
            "status": "active",
            "configured": self.is_configured,
            "model": self.model if self.is_configured else "mock",
            "capabilities": self.get_capabilities(),
            "fallback_enabled": self.fallback_to_mock
        }


class AIAgentManagerFull:
    """
    AI Agent Manager with full OpenAI integration
    """
    
    def __init__(self):
        self.agents = {
            "openai": OpenAIAgent()
        }
        self.default_agent = os.getenv('DEFAULT_AI_AGENT', 'openai')
        logger.info("AI Agent Manager (Full) initialized")
    
    def get_agent(self, agent_type: str = None) -> OpenAIAgent:
        """Get AI agent by type"""
        agent_type = agent_type or self.default_agent
        return self.agents.get(agent_type, self.agents['openai'])
    
    def process_request(self, request: Dict[str, Any], agent_type: str = None) -> Dict[str, Any]:
        """Process request through specified agent"""
        agent = self.get_agent(agent_type)
        return agent.process_request(request)
    
    def get_status(self) -> Dict[str, Any]:
        """Get status of all agents"""
        return {
            "manager_type": "full",
            "default_agent": self.default_agent,
            "agents": {name: agent.get_status() for name, agent in self.agents.items()}
        }


# Create global instance
ai_agent_manager = AIAgentManagerFull()
