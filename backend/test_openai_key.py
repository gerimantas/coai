#!/usr/bin/env python3
"""
OpenAI API Key Validation Script
Tests if the configured API key works with real OpenAI API
"""

import os
import sys
from dotenv import load_dotenv
import openai

def test_openai_key():
    """Test OpenAI API key functionality"""
    
    # Load environment variables
    load_dotenv()
    
    api_key = os.getenv('OPENAI_API_KEY')
    enable_real_ai = os.getenv('ENABLE_REAL_AI', 'false').lower() == 'true'
    fallback_to_mock = os.getenv('FALLBACK_TO_MOCK', 'true').lower() == 'true'
    
    print("🔍 OpenAI API Configuration Check")
    print("=" * 40)
    
    if not api_key:
        print("❌ No API key found in environment")
        return False
    
    print(f"🔑 API Key: {api_key[:20]}..." if len(api_key) > 20 else api_key)
    print(f"🤖 ENABLE_REAL_AI: {enable_real_ai}")
    print(f"🔄 FALLBACK_TO_MOCK: {fallback_to_mock}")
    
    # Check configuration
    if not enable_real_ai:
        print("⚠️  WARNING: ENABLE_REAL_AI=false - system will use mock responses")
        print("   Set ENABLE_REAL_AI=true in .env file to use real AI")
        return False
    
    # Check if it's a demo key
    if 'demo' in api_key.lower() or 'test' in api_key.lower():
        print("⚠️  WARNING: This appears to be a demo/test key")
        print("   Real OpenAI API calls will fail")
        return False
    
    # Test real API call
    try:
        print("🧪 Testing API connection...")
        
        client = openai.OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say 'API connection successful' if you can read this."}
            ],
            max_tokens=10
        )
        
        reply = response.choices[0].message.content
        tokens_used = response.usage.total_tokens
        
        print("✅ API Connection: SUCCESS")
        print(f"🤖 AI Response: {reply}")
        print(f"🔢 Tokens Used: {tokens_used}")
        print(f"💰 Model: {response.model}")
        
        return True
        
    except openai.AuthenticationError:
        print("❌ Authentication Error: Invalid API key")
        return False
    except openai.RateLimitError:
        print("⚠️  Rate limit exceeded (but key is valid)")
        return True
    except openai.APIError as e:
        print(f"❌ OpenAI API Error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        return False

if __name__ == "__main__":
    success = test_openai_key()
    
    print("\n" + "=" * 40)
    
    if success:
        print("🎉 RESULT: Ready for real AI testing!")
        print("   Your COAI system will use actual OpenAI responses")
    else:
        print("🚨 RESULT: Still in demo mode")
        print("   COAI will use intelligent mock responses")
    
    print("\n📋 Next Steps:")
    if success:
        print("   1. Restart COAI backend server")
        print("   2. Test chat interface")
        print("   3. All responses will be real AI-generated")
    else:
        print("   1. Get valid OpenAI API key from platform.openai.com")
        print("   2. Update backend/.env file")
        print("   3. Run this script again to verify")
