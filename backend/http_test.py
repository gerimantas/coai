#!/usr/bin/env python3
import requests
import json
import sys

print("=== COAI HTTP API Test ===")

# Test chat endpoint
url = "http://localhost:5000/api/chat"
test_data = {
    "message": "Can you help me debug a Python function?",
    "project": "my-project",
    "file": "debug.py"
}

print(f"\nTesting: {url}")
print(f"Data: {json.dumps(test_data, indent=2)}")

try:
    print("\nSending request...")
    response = requests.post(url, json=test_data, timeout=15)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        print("✅ SUCCESS!")
        result = response.json()
        
        print(f"\n📊 Response Summary:")
        print(f"   Request ID: {result.get('request_id', 'N/A')}")
        print(f"   Status: {result.get('status', 'N/A')}")
        print(f"   Agent Type: {result.get('agent_type', 'N/A')}")
        print(f"   Real AI: {result.get('real_ai', 'N/A')}")
        
        # Show response content (truncated)
        response_text = result.get('response', result.get('reply', 'No response'))
        print(f"\n💬 AI Response:")
        print(f"   {response_text[:200]}...")
        
        print(f"\n🔧 Technical Details:")
        print(f"   Timestamp: {result.get('timestamp', 'N/A')}")
        if 'usage' in result:
            usage = result['usage']
            print(f"   Tokens: {usage.get('total_tokens', 'N/A')}")
            print(f"   Model: {usage.get('model', 'N/A')}")
        
    else:
        print(f"❌ ERROR - Status: {response.status_code}")
        print(f"Response: {response.text}")
        
except requests.exceptions.ConnectionError:
    print("❌ CONNECTION ERROR - Server not running or not accessible")
except requests.exceptions.Timeout:
    print("❌ TIMEOUT ERROR - Request took too long")
except Exception as e:
    print(f"❌ UNEXPECTED ERROR: {e}")

print("\n=== HTTP API Test Complete ===")

# Test status endpoint
print("\n=== Testing Status Endpoint ===")
try:
    status_url = "http://localhost:5000/api/orchestrator/status"
    response = requests.get(status_url, timeout=5)
    
    if response.status_code == 200:
        print("✅ Status endpoint working")
        status_data = response.json()
        print(f"   Orchestrator: {status_data.get('orchestrator_status', 'N/A')}")
    else:
        print(f"⚠️ Status endpoint returned: {response.status_code}")
        
except Exception as e:
    print(f"⚠️ Status endpoint error: {e}")

print("\n🎯 All tests completed!")
