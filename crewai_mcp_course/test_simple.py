#!/usr/bin/env python3
"""
Simple test script for CrewAI MCP Course
Tests basic functionality without complex dependencies.
"""

import os
import sys

def test_basic_imports():
    """Test that basic imports work."""
    print("🧪 Testing basic imports...")
    
    try:
        import requests
        import json
        import datetime
        print("✅ Basic imports successful")
        return True
    except ImportError as e:
        print(f"❌ Basic import failed: {e}")
        return False

def test_file_structure():
    """Test that all required files exist."""
    print("🧪 Testing file structure...")
    
    required_files = [
        "requirements.txt",
        "metadata.yaml",
        "README.md",
        "lesson1_setup.py",
        "lesson2_mcp_integration.py",
        "lesson3_advanced_patterns.py",
        "test_course.py"
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} missing")
            all_exist = False
    
    return all_exist

def test_lesson_1_syntax():
    """Test that lesson 1 has valid Python syntax."""
    print("🧪 Testing Lesson 1 syntax...")
    
    try:
        with open("lesson1_setup.py", "r") as f:
            code = f.read()
        
        compile(code, "lesson1_setup.py", "exec")
        print("✅ Lesson 1 syntax is valid")
        return True
    except SyntaxError as e:
        print(f"❌ Lesson 1 syntax error: {e}")
        return False

def test_lesson_2_syntax():
    """Test that lesson 2 has valid Python syntax."""
    print("🧪 Testing Lesson 2 syntax...")
    
    try:
        with open("lesson2_mcp_integration.py", "r") as f:
            code = f.read()
        
        compile(code, "lesson2_mcp_integration.py", "exec")
        print("✅ Lesson 2 syntax is valid")
        return True
    except SyntaxError as e:
        print(f"❌ Lesson 2 syntax error: {e}")
        return False

def test_lesson_3_syntax():
    """Test that lesson 3 has valid Python syntax."""
    print("🧪 Testing Lesson 3 syntax...")
    
    try:
        with open("lesson3_advanced_patterns.py", "r") as f:
            code = f.read()
        
        compile(code, "lesson3_advanced_patterns.py", "exec")
        print("✅ Lesson 3 syntax is valid")
        return True
    except SyntaxError as e:
        print(f"❌ Lesson 3 syntax error: {e}")
        return False

def test_metadata_syntax():
    """Test that metadata.yaml has valid YAML syntax."""
    print("🧪 Testing metadata.yaml syntax...")
    
    try:
        import yaml
        with open("metadata.yaml", "r") as f:
            data = yaml.safe_load(f)
        
        if data and "title" in data:
            print("✅ metadata.yaml is valid YAML")
            return True
        else:
            print("❌ metadata.yaml missing required fields")
            return False
    except ImportError:
        print("⚠️  PyYAML not available, skipping YAML validation")
        return True
    except Exception as e:
        print(f"❌ metadata.yaml syntax error: {e}")
        return False

def run_simple_tests():
    """Run simple tests that don't require complex dependencies."""
    print("🚀 Running simple validation tests...")
    print("=" * 50)
    
    tests = [
        ("Basic Imports", test_basic_imports),
        ("File Structure", test_file_structure),
        ("Lesson 1 Syntax", test_lesson_1_syntax),
        ("Lesson 2 Syntax", test_lesson_2_syntax),
        ("Lesson 3 Syntax", test_lesson_3_syntax),
        ("Metadata Syntax", test_metadata_syntax),
    ]
    
    results = {}
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        results[test_name] = test_func()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 SIMPLE TEST RESULTS SUMMARY")
    print("=" * 50)
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, passed_test in results.items():
        status = "✅ PASSED" if passed_test else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All simple tests passed! The course structure is valid.")
        print("📚 Note: Full functionality requires installing all dependencies from requirements.txt")
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
    
    return results

if __name__ == "__main__":
    try:
        results = run_simple_tests()
        
        # Exit with appropriate code
        if all(results.values()):
            sys.exit(0)
        else:
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Simple test runner failed: {e}")
        sys.exit(1)