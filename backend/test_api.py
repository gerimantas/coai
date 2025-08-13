#!/usr/bin/env python3
"""
Test script for COAI API functionality
"""

import requests
import json
import sys

def test_chat_api():
    """Test the chat API endpoint"""
    url = "http://localhost:5000/api/chat"
    
    test_data = {
        "message": "Hello, can you help me debug Python code?",
        "project": "test-project", 
        "file": "main.py"
    }
    
    print("Testing COAI Chat API...")
    print(f"URL: {url}")
    print(f"Data: {json.dumps(test_data, indent=2)}")
    print("-" * 50)
    
    try:
        response = requests.post(url, json=test_data, timeout=10)
        
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print("-" * 50)
        
        if response.status_code == 200:
            data = response.json()
            print("✅ SUCCESS - Response received:")
            print(json.dumps(data, indent=2))
            
            # Check if it's using real AI or mock
            if data.get('real_ai'):
                print("\n🤖 Using REAL AI integration")
            else:
                print("\n🎭 Using MOCK AI responses")
                
        else:
            print(f"❌ ERROR - Status: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ ERROR - Cannot connect to server. Is it running?")
    except requests.exceptions.Timeout:
        print("❌ ERROR - Request timeout")
    except Exception as e:
        print(f"❌ ERROR - {str(e)}")

def test_status_endpoint():
    """Test the orchestrator status endpoint"""
    url = "http://localhost:5000/api/orchestrator/status"
    
    print("\nTesting Orchestrator Status...")
    print(f"URL: {url}")
    
    try:
        response = requests.get(url, timeout=5)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Orchestrator Status:")
            print(json.dumps(data, indent=2))
        else:
            print(f"❌ Status endpoint error: {response.text}")
            
    except Exception as e:
        print(f"❌ Status endpoint error: {str(e)}")

if __name__ == "__main__":
    print("COAI System Test")
    print("=" * 50)
    
    test_chat_api()
    test_status_endpoint()
    
    print("\n" + "=" * 50)
    print("Test completed!")
