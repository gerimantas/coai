# Test Python Project

This project contains Python files with intentional issues for testing COAI's AI-powered code assistance capabilities.

## Files Description

### calculator.py
- **Purpose**: Mathematical operations with various bugs
- **Issues**: Division by zero, inefficient algorithms, missing error handling
- **Test scenarios**: Code review, bug fixing, optimization suggestions

### data_processor.py  
- **Purpose**: Data processing and transformation
- **Issues**: Missing validation, inefficient algorithms, error-prone operations
- **Test scenarios**: Debugging assistance, performance optimization

### api_client.py
- **Purpose**: HTTP API client with authentication
- **Issues**: Poor error handling, missing async operations, no retry logic
- **Test scenarios**: Architecture improvements, error handling suggestions

## How to Use for Testing

1. Load any file in COAI
2. Ask for code review: "Can you review this code and suggest improvements?"
3. Report bugs: "This code crashes with division by zero, how to fix?"
4. Request optimizations: "How can I make this code more efficient?"
5. Ask for documentation: "Generate documentation for this module"

## Expected COAI Responses

The AI should be able to:
- Identify specific bugs and security issues
- Suggest performance improvements
- Recommend better error handling
- Provide code refactoring suggestions
- Generate comprehensive documentation
- Explain complex algorithms
- Suggest testing strategies

## Test Scenarios

### Bug Finding
- Division by zero in calculator.py
- Missing key access in data_processor.py
- File not found errors in api_client.py

### Code Review
- Missing type hints
- Inefficient algorithms (O(n²) operations)
- Poor error handling patterns

### Optimization
- Recursive vs iterative implementations
- List comprehensions vs loops
- Async/await for I/O operations

### Documentation
- Missing docstrings
- Unclear variable names  
- Complex logic without comments
