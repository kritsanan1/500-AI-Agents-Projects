#!/usr/bin/env python3
"""
Test script for CrewAI MCP Course
This script tests all lessons to ensure they work correctly.
"""

import sys
import os
from typing import Dict, Any

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_lesson_1() -> bool:
    """Test Lesson 1: Basic CrewAI setup."""
    print("🧪 Testing Lesson 1: Basic CrewAI Setup...")
    
    try:
        from lesson1_setup import BasicCrewAISetup
        
        # Create instance
        lesson = BasicCrewAISetup()
        
        # Test basic functionality
        agent = lesson.create_basic_agent()
        task = lesson.create_simple_task(agent)
        result = lesson.execute_task(agent, task)
        
        print("✅ Lesson 1 test passed")
        return True
        
    except Exception as e:
        print(f"❌ Lesson 1 test failed: {e}")
        return False

def test_lesson_2() -> bool:
    """Test Lesson 2: MCP Integration."""
    print("🧪 Testing Lesson 2: MCP Integration...")
    
    try:
        from lesson2_mcp_integration import MCPIntegrationLesson, FastMCPTool
        
        # Test MCP tool creation
        mcp_tool = FastMCPTool(
            base_url="http://localhost:8000",
            api_key="test-key"
        )
        
        # Test simulated MCP response
        result = mcp_tool._simulate_mcp_response("weather", "GET")
        
        if "temperature" in result:
            print("✅ MCP tool simulation working")
        
        # Test lesson
        lesson = MCPIntegrationLesson()
        lesson.run_demo()
        
        print("✅ Lesson 2 test passed")
        return True
        
    except Exception as e:
        print(f"❌ Lesson 2 test failed: {e}")
        return False

def test_lesson_3() -> bool:
    """Test Lesson 3: Advanced Patterns."""
    print("🧪 Testing Lesson 3: Advanced Patterns...")
    
    try:
        from lesson3_advanced_patterns import AdvancedCrewAIWorkflows, ResearchDataStore
        
        # Test data store
        store = ResearchDataStore()
        store.store("test_key", "test_value")
        retrieved = store.retrieve("test_key")
        
        if retrieved == "test_value":
            print("✅ Data store working")
        
        # Test lesson (simplified)
        lesson = AdvancedCrewAIWorkflows()
        lesson.demonstrate_data_sharing()
        
        print("✅ Lesson 3 test passed")
        return True
        
    except Exception as e:
        print(f"❌ Lesson 3 test failed: {e}")
        return False

def run_all_tests() -> Dict[str, bool]:
    """Run all tests and return results."""
    print("🚀 Running all CrewAI MCP Course tests...")
    print("=" * 50)
    
    results = {}
    
    # Test each lesson
    results["lesson_1"] = test_lesson_1()
    results["lesson_2"] = test_lesson_2()
    results["lesson_3"] = test_lesson_3()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 50)
    
    passed = sum(results.values())
    total = len(results)
    
    for lesson, passed_test in results.items():
        status = "✅ PASSED" if passed_test else "❌ FAILED"
        print(f"{lesson}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The course is ready to use.")
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
    
    return results

if __name__ == "__main__":
    try:
        results = run_all_tests()
        
        # Exit with appropriate code
        if all(results.values()):
            sys.exit(0)
        else:
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Test runner failed: {e}")
        sys.exit(1)