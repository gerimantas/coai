import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Test imports first
print("=== COAI System Test ===")
print("Testing imports...")

try:
    from app.routes import bp
    print("✅ Routes import: OK")
except Exception as e:
    print(f"❌ Routes import failed: {e}")

try:
    from app.orchestrator import COAIOrchestrator
    print("✅ Orchestrator import: OK")
except Exception as e:
    print(f"❌ Orchestrator import failed: {e}")

try:
    from app.ai_agents_full import ai_agent_manager
    print("✅ Full AI agents import: OK")
except Exception as e:
    print(f"❌ Full AI agents import failed: {e}")
    try:
        from app.ai_agents import ai_agent_manager
        print("✅ Basic AI agents import: OK (fallback)")
    except Exception as e2:
        print(f"❌ Basic AI agents import failed: {e2}")

# Test orchestrator creation
print("\nTesting orchestrator creation...")
try:
    orch = COAIOrchestrator()
    print("✅ Orchestrator created successfully")
    
    # Test chat processing
    test_message = "Hello, can you help me with Python debugging?"
    test_context = {
        "project": "test-project",
        "file": "main.py",
        "timestamp": "2025-01-01T12:00:00"
    }
    
    print(f"\nTesting chat processing...")
    print(f"Message: {test_message}")
    print(f"Context: {test_context}")
    
    response = orch.process_chat_request(test_message, test_context)
    print(f"\n✅ Chat processing successful!")
    print(f"Response status: {response.get('status')}")
    print(f"Reply preview: {response.get('reply', '')[:100]}...")
    
    if response.get('real_ai'):
        print("🤖 Using REAL AI")
    else:
        print("🎭 Using MOCK AI")
        
except Exception as e:
    print(f"❌ Orchestrator test failed: {e}")
    import traceback
    traceback.print_exc()

print("\n=== Test Completed ===")
