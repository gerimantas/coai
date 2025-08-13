import requests
import json

print("Quick COAI API Test")
print("=" * 30)

# Test basic endpoint
try:
    r = requests.get("http://localhost:5000/", timeout=3)
    print(f"✅ Basic endpoint: {r.status_code}")
except Exception as e:
    print(f"❌ Basic endpoint failed: {e}")
    exit(1)

# Test chat endpoint
try:
    data = {
        "message": "Help me debug Python code",
        "project": "test",
        "file": "main.py"
    }
    r = requests.post("http://localhost:5000/api/chat", json=data, timeout=10)
    print(f"✅ Chat endpoint: {r.status_code}")
    
    if r.status_code == 200:
        resp = r.json()
        print(f"Status: {resp.get('status')}")
        reply = resp.get('reply', '')
        print(f"Reply: {reply[:100]}...")
        
        if resp.get('real_ai'):
            print("🤖 Real AI")
        else:
            print("🎭 Mock AI")
    else:
        print(f"Error: {r.text}")
        
except Exception as e:
    print(f"❌ Chat endpoint failed: {e}")

print("=" * 30)
print("Test completed!")
