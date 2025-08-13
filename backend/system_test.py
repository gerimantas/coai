#!/usr/bin/env python3
import os
import sys

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=== COAI System Test ===")

# Test 1: Check if environment is loaded
print("\n1. Environment Test:")
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ dotenv loaded")
    
    openai_key = os.getenv('OPENAI_API_KEY', 'not_set')
    enable_real_ai = os.getenv('ENABLE_REAL_AI', 'false')
    print(f"✅ OPENAI_API_KEY: {'set' if openai_key != 'not_set' else 'not set'}")
    print(f"✅ ENABLE_REAL_AI: {enable_real_ai}")
except Exception as e:
    print(f"❌ Environment error: {e}")

# Test 2: Import modules
print("\n2. Import Test:")
try:
    from app.ai_agents_full import ai_agent_manager
    print("✅ AI agents imported successfully")
    
    status = ai_agent_manager.get_status()
    print(f"✅ AI Manager type: {status.get('manager_type')}")
    print(f"✅ Default agent: {status.get('default_agent')}")
except Exception as e:
    print(f"❌ Import error: {e}")

# Test 3: Test AI agent directly
print("\n3. AI Agent Test:")
try:
    request_data = {
        "message": "Hello, test message",
        "context": {
            "project": "test-project",
            "file": "test.py"
        }
    }
    
    response = ai_agent_manager.process_request(request_data)
    print(f"✅ AI response received")
    print(f"   Status: {response.get('status')}")
    print(f"   Agent: {response.get('agent_type')}")
    print(f"   Real AI: {response.get('real_ai', False)}")
    print(f"   Response: {response.get('response', '')[:100]}...")
    
except Exception as e:
    print(f"❌ AI Agent error: {e}")

print("\n=== Test Complete ===")
