import requests
import json

print("Testing COAI Chat API...")

url = "http://localhost:5000/api/chat"
data = {
    "message": "Hello, can you help me debug Python code?",
    "project": "test-project",
    "file": "main.py"
}

try:
    response = requests.post(url, json=data, timeout=10)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print("✅ SUCCESS!")
        print(f"Response: {result.get('response', 'No response')[:200]}...")
        print(f"Agent: {result.get('agent_type', 'unknown')}")
        print(f"Real AI: {result.get('real_ai', False)}")
    else:
        print(f"❌ ERROR: {response.text}")
except Exception as e:
    print(f"❌ EXCEPTION: {e}")

print("Test completed.")
