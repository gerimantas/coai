#!/usr/bin/env python3
"""
Test real API functionality after enabling ENABLE_REAL_AI
"""
import requests
import json
import sys
import os

# Add the app directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

def test_chat_endpoint():
    """Test the chat endpoint with real AI"""
    url = "http://127.0.0.1:5000/api/chat"
    headers = {"Content-Type": "application/json"}
    data = {
        "message": "Hello! Please respond with exactly: 'AI INTEGRATION WORKING'",
        "rules_file": "backend/app/rules.txt",
        "project_path": "."
    }
    
    try:
        print("Testing chat endpoint...")
        response = requests.post(url, headers=headers, json=data, timeout=30)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            response_data = response.json()
            if "response" in response_data:
                print(f"AI Response: {response_data['response']}")
                return True
        return False
    except Exception as e:
        print(f"Error testing chat endpoint: {e}")
        return False

def test_usage_stats():
    """Test usage stats endpoint"""
    url = "http://127.0.0.1:5000/api/usage-stats"
    
    try:
        print("\nTesting usage stats endpoint...")
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error testing usage stats: {e}")
        return False

def test_plans_endpoint():
    """Test action plans endpoint"""
    url = "http://127.0.0.1:5000/api/plans"
    headers = {"Content-Type": "application/json"}
    data = {
        "goal": "Test action plan generation"
    }
    
    try:
        print("\nTesting plans endpoint...")
        response = requests.post(url, headers=headers, json=data, timeout=20)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error testing plans endpoint: {e}")
        return False

if __name__ == "__main__":
    print("=== COAI Stage 6: End-to-End API Testing ===\n")
    
    # Test chat (most important)
    chat_success = test_chat_endpoint()
    
    # Test other endpoints
    usage_success = test_usage_stats()
    plans_success = test_plans_endpoint()
    
    print("\n=== TEST RESULTS ===")
    print(f"Chat Endpoint: {'✅ PASS' if chat_success else '❌ FAIL'}")
    print(f"Usage Stats: {'✅ PASS' if usage_success else '❌ FAIL'}")
    print(f"Action Plans: {'✅ PASS' if plans_success else '❌ FAIL'}")
    
    if chat_success and usage_success:
        print("\n🎉 Stage 6 Tests: SUCCESSFUL! Real AI is working!")
    else:
        print("\n⚠️ Some tests failed. Check logs for details.")
