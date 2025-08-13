#!/usr/bin/env python3
"""
Stage 6: End-to-End API Testing
"""
import requests
import json
import time

def test_chat_endpoint():
    """Test the main chat functionality"""
    url = "http://127.0.0.1:5000/api/chat"
    
    test_data = {
        "message": "Hello! Please tell me what COAI system can do.",
        "project": "coai",
        "file": "main.py"
    }
    
    try:
        print("📞 Testing Chat Endpoint...")
        response = requests.post(url, json=test_data, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Chat API Working!")
            print(f"Response: {data.get('response', 'No response')[:100]}...")
            return True
        else:
            print(f"❌ Chat failed with status {response.status_code}")
            print(f"Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Chat test error: {e}")
        return False

def test_usage_stats():
    """Test usage statistics"""
    url = "http://127.0.0.1:5000/api/usage-stats"
    
    try:
        print("\n📊 Testing Usage Stats...")
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Usage Stats Working!")
            print(f"Total requests: {data.get('total_requests', 0)}")
            return True
        else:
            print(f"❌ Usage stats failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Usage stats error: {e}")
        return False

def test_project_files():
    """Test project files listing"""
    url = "http://127.0.0.1:5000/api/files"
    test_data = {"path": "."}
    
    try:
        print("\n📁 Testing Files API...")
        response = requests.post(url, json=test_data, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Files API Working!")
            print(f"Found {len(data.get('files', []))} files")
            return True
        else:
            print(f"❌ Files API failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Files test error: {e}")
        return False

def test_rules_endpoint():
    """Test rules management"""
    url = "http://127.0.0.1:5000/api/rules"
    
    try:
        print("\n📋 Testing Rules API...")
        # Get rules
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            print("✅ Rules API Working!")
            data = response.json()
            print(f"Rules length: {len(data.get('content', ''))}")
            return True
        else:
            print(f"❌ Rules API failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Rules test error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 COAI Stage 6: End-to-End Testing")
    print("=" * 50)
    
    # Wait for server to be ready
    print("⏳ Waiting for server...")
    time.sleep(2)
    
    tests = [
        test_chat_endpoint,
        test_usage_stats, 
        test_project_files,
        test_rules_endpoint
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"🏆 STAGE 6 RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! COAI is ready for production!")
    elif passed >= 3:
        print("⚠️ Most tests passed. System is functional with minor issues.")
    else:
        print("❌ Multiple failures. System needs debugging.")
