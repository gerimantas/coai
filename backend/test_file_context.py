#!/usr/bin/env python3
"""
Test file context functionality
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from app.file_context_manager import file_context_manager
from app.preprocessor import preprocessor

def test_file_context():
    print("=== TESTING FILE CONTEXT FUNCTIONALITY ===\n")
    
    # Test 1: File context detection
    message = 'What files are in this project?'
    print("Test 1: File context detection")
    print(f"Message: '{message}'")
    should_include = file_context_manager.should_include_file_context(message)
    print(f"Should include file context: {should_include}")
    print("✅ PASS" if should_include else "❌ FAIL")
    print()
    
    # Test 2: File listing
    print("Test 2: File listing")
    file_data = file_context_manager.get_project_file_listing()
    print(f"File listing status: {file_data['status']}")
    print(f"Total files found: {file_data['file_summary']['total_files']}")
    print("✅ PASS" if file_data['status'] == 'success' and file_data['file_summary']['total_files'] > 0 else "❌ FAIL")
    print()
    
    # Test 3: Formatted output
    print("Test 3: Formatted output")
    formatted = file_context_manager.format_file_context_for_ai(file_data)
    print("First 300 chars of formatted output:")
    print("-" * 50)
    print(formatted[:300])
    print("...")
    print("-" * 50)
    print("✅ PASS" if len(formatted) > 100 else "❌ FAIL")
    print()
    
    # Test 4: Full preprocessor integration
    print("Test 4: Preprocessor integration")
    context = {"project": "demo-project", "file": "main.py"}
    processed = preprocessor.process_prompt(message, context)
    enhanced_prompt = processed['enhanced_prompt']
    
    print("Enhanced prompt includes file context:")
    includes_file_info = "PROJECT FILE INFORMATION" in enhanced_prompt
    print(f"File information included: {includes_file_info}")
    print("✅ PASS" if includes_file_info else "❌ FAIL")
    print()
    
    print("=== TEST SUMMARY ===")
    print("File context manager: READY")
    print("Preprocessor integration: READY") 
    print("🎯 Next step: Test with live backend")

if __name__ == "__main__":
    test_file_context()
