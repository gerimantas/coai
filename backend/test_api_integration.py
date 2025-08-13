#!/usr/bin/env python3
"""
COAI API Integration Test
Tests the actual HTTP endpoints
"""

import requests
import json
import time

BASE_URL = "http://localhost:5000"

def test_basic_endpoint():
    """Test basic endpoint"""
    print("Testing basic endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        print(f"✅ Basic endpoint: {response.status_code} - {response.text}")
        return True
    except Exception as e:
        print(f"❌ Basic endpoint failed: {e}")
        return False

def test_chat_endpoint():
    """Test chat endpoint with various scenarios"""
    print("\nTesting chat endpoint...")
    
    test_cases = [
        {
            "name": "Basic debugging question",
            "data": {
                "message": "Hello, can you help me debug this Python error?",
                "project": "test-project",
                "file": "main.py"
            }
        },
        {
            "name": "Code review request", 
            "data": {
                "message": "Please review my code for best practices",
                "project": "my-app",
                "file": "app.py"
            }
        },
        {
            "name": "Function implementation",
            "data": {
                "message": "Help me implement a sorting function",
                "project": "algorithms",
                "file": "sort.py"
            }
        },
        {
            "name": "Testing guidance",
            "data": {
                "message": "How should I test this function?",
                "project": "testing-demo", 
                "file": "utils.py"
            }
        }
    ]
    
    results = []
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n--- Test {i}: {test_case['name']} ---")
        try:
            response = requests.post(
                f"{BASE_URL}/api/chat",
                json=test_case['data'],
                timeout=10,
                headers={'Content-Type': 'application/json'}
            )
            
            print(f"Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print("✅ Success!")
                print(f"Request ID: {data.get('request_id', 'N/A')}")
                print(f"Status: {data.get('status', 'N/A')}")
                
                reply = data.get('reply', '')
                if reply:
                    print(f"Reply preview: {reply[:150]}...")
                
                # Check AI type
                if 'debug' in data and data['debug'].get('stub'):
                    print("🎭 Using STUB response")
                elif data.get('real_ai'):
                    print("🤖 Using REAL AI")
                else:
                    print("🎭 Using MOCK AI")
                    
                results.append(True)
            else:
                print(f"❌ Failed with status {response.status_code}")
                print(f"Response: {response.text}")
                results.append(False)
                
        except Exception as e:
            print(f"❌ Exception: {e}")
            results.append(False)
    
    return results

def test_orchestrator_status():
    """Test orchestrator status endpoint"""
    print("\n\nTesting orchestrator status...")
    try:
        response = requests.get(f"{BASE_URL}/api/orchestrator/status", timeout=5)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Orchestrator status received:")
            print(json.dumps(data, indent=2))
            return True
        else:
            print(f"❌ Status endpoint error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Status endpoint exception: {e}")
        return False

def test_error_handling():
    """Test error handling"""
    print("\n\nTesting error handling...")
    
    error_tests = [
        {
            "name": "Empty message",
            "data": {"message": "", "project": "test", "file": "test.py"}
        },
        {
            "name": "Very long message",
            "data": {
                "message": "x" * 15000,  # Exceed max length
                "project": "test", 
                "file": "test.py"
            }
        },
        {
            "name": "Missing required fields",
            "data": {"message": "test"}
        }
    ]
    
    for test_case in error_tests:
        print(f"\n--- {test_case['name']} ---")
        try:
            response = requests.post(
                f"{BASE_URL}/api/chat",
                json=test_case['data'],
                timeout=5
            )
            
            print(f"Status: {response.status_code}")
            if response.status_code >= 400:
                print("✅ Error handled correctly")
            else:
                print("⚠️ Expected error, but got success")
                
        except Exception as e:
            print(f"❌ Exception: {e}")

def main():
    print("=" * 60)
    print("COAI API Integration Test")
    print("=" * 60)
    
    # Test 1: Basic connectivity
    if not test_basic_endpoint():
        print("❌ Cannot connect to server. Make sure it's running on localhost:5000")
        return
    
    # Test 2: Chat functionality
    chat_results = test_chat_endpoint()
    
    # Test 3: Status endpoint  
    status_result = test_orchestrator_status()
    
    # Test 4: Error handling
    test_error_handling()
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    chat_success = sum(chat_results)
    chat_total = len(chat_results)
    
    print(f"Chat endpoint: {chat_success}/{chat_total} tests passed")
    print(f"Status endpoint: {'✅' if status_result else '❌'}")
    
    if chat_success == chat_total and status_result:
        print("\n🎉 ALL TESTS PASSED! COAI system is working correctly.")
    else:
        print("\n⚠️ Some tests failed. Check the output above for details.")

if __name__ == "__main__":
    main()
