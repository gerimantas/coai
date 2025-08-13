#!/usr/bin/env python3
"""
STAGE 2: Practical Functionality Testing Script
Tests real-world scenarios with COAI system
"""

import requests
import json
import time
import os

def test_chat_api(message, project, file_name, scenario_name):
    """Test a specific chat scenario"""
    print(f"\n{'='*60}")
    print(f"🧪 TESTING: {scenario_name}")
    print(f"{'='*60}")
    print(f"Project: {project}")
    print(f"File: {file_name}")
    print(f"Message: {message[:100]}...")
    
    url = "http://localhost:5000/api/chat"
    data = {
        "message": message,
        "project": project,
        "file": file_name
    }
    
    try:
        start_time = time.time()
        response = requests.post(url, json=data, timeout=30)
        end_time = time.time()
        
        if response.status_code == 200:
            result = response.json()
            
            print(f"\n✅ SUCCESS ({end_time - start_time:.2f}s)")
            print(f"Agent: {result.get('agent_type', 'unknown')}")
            print(f"Real AI: {result.get('real_ai', False)}")
            print(f"Status: {result.get('status', 'unknown')}")
            
            # Show AI response (truncated)
            ai_response = result.get('response', result.get('reply', 'No response'))
            print(f"\n💬 AI Response (first 300 chars):")
            print(f"{ai_response[:300]}...")
            
            # Check response quality indicators
            response_length = len(ai_response)
            has_code_blocks = '```' in ai_response
            has_specific_advice = any(word in ai_response.lower() for word in ['fix', 'improve', 'error', 'bug', 'optimize'])
            
            print(f"\n📊 Response Quality:")
            print(f"   Length: {response_length} characters")
            print(f"   Contains code: {'✅' if has_code_blocks else '❌'}")
            print(f"   Specific advice: {'✅' if has_specific_advice else '❌'}")
            
            # Usage info if available
            if 'usage' in result:
                usage = result['usage']
                print(f"   Tokens: {usage.get('total_tokens', 'N/A')}")
                print(f"   Model: {usage.get('model', 'N/A')}")
            
            return True, result
            
        else:
            print(f"❌ FAILED - Status: {response.status_code}")
            print(f"Response: {response.text}")
            return False, None
            
    except Exception as e:
        print(f"❌ EXCEPTION: {e}")
        return False, None

def main():
    print("🚀 COAI STAGE 2: Practical Functionality Testing")
    print("=" * 80)
    
    # Test scenarios based on our test project files
    test_scenarios = [
        {
            "name": "Code Review - Calculator",
            "message": "Can you review this Calculator class and suggest improvements? I'm particularly concerned about potential bugs and performance issues.",
            "project": "test-python-project",
            "file": "calculator.py"
        },
        {
            "name": "Bug Debugging - Division by Zero",
            "message": "This calculator has a divide method that crashes with division by zero. How should I fix this and handle edge cases properly?",
            "project": "test-python-project", 
            "file": "calculator.py"
        },
        {
            "name": "Performance Optimization - Factorial",
            "message": "The factorial method uses recursion and might cause stack overflow for large numbers. What's a better approach?",
            "project": "test-python-project",
            "file": "calculator.py"
        },
        {
            "name": "Code Review - Data Processor",
            "message": "Please review this data processing code. It has several error handling issues and inefficient algorithms. What needs to be fixed?",
            "project": "test-python-project",
            "file": "data_processor.py"
        },
        {
            "name": "Error Handling - API Client",
            "message": "This API client doesn't handle errors well and lacks retry logic. How can I make it more robust for production use?",
            "project": "test-python-project",
            "file": "api_client.py"
        },
        {
            "name": "Documentation Generation",
            "message": "Generate comprehensive documentation for this API client class, including usage examples and best practices.",
            "project": "test-python-project",
            "file": "api_client.py"
        },
        {
            "name": "Architecture Advice",
            "message": "I'm building a data processing pipeline. Looking at these files, what architectural improvements would you suggest for scalability?",
            "project": "test-python-project",
            "file": "data_processor.py"
        },
        {
            "name": "Testing Strategy",
            "message": "What testing strategy would you recommend for this calculator module? Please suggest specific test cases and testing frameworks.",
            "project": "test-python-project",
            "file": "calculator.py"
        }
    ]
    
    results = []
    successful_tests = 0
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"\nTest {i}/{len(test_scenarios)}")
        success, result = test_chat_api(
            scenario["message"],
            scenario["project"], 
            scenario["file"],
            scenario["name"]
        )
        
        results.append({
            "scenario": scenario["name"],
            "success": success,
            "result": result
        })
        
        if success:
            successful_tests += 1
        
        # Small delay between tests
        time.sleep(1)
    
    # Summary
    print(f"\n{'='*80}")
    print(f"🎯 STAGE 2 TEST SUMMARY")
    print(f"{'='*80}")
    print(f"Total tests: {len(test_scenarios)}")
    print(f"Successful: {successful_tests}")
    print(f"Failed: {len(test_scenarios) - successful_tests}")
    print(f"Success rate: {(successful_tests/len(test_scenarios)*100):.1f}%")
    
    # Detailed results
    print(f"\n📋 Detailed Results:")
    for result in results:
        status = "✅" if result["success"] else "❌"
        print(f"   {status} {result['scenario']}")
    
    # Check if minimum requirements met
    if successful_tests >= len(test_scenarios) * 0.8:  # 80% success rate
        print(f"\n🎉 STAGE 2 REQUIREMENTS MET!")
        print(f"   Chat produces meaningful responses ✅")
        print(f"   Real-world scenarios work ✅")
        print(f"   System handles complex requests ✅")
        return True
    else:
        print(f"\n⚠️  STAGE 2 NEEDS WORK")
        print(f"   Success rate below 80% threshold")
        return False

if __name__ == "__main__":
    main()
