#!/usr/bin/env python3
"""
Lesson 2: Integrating MCP Server with CrewAI

This lesson demonstrates:
- Creating custom tools for MCP server access
- Configuring authentication and connection settings
- Using MCP server data in agent tasks
- Handling errors and exceptions
"""

import os
import sys
import json
import requests
from typing import Dict, Any, Optional
from dotenv import load_dotenv

try:
    from crewai import Agent, Task, Crew
    from crewai_tools import BaseTool
    from pydantic import BaseModel, Field
except ImportError as e:
    print(f"Error importing dependencies: {e}")
    print("Please install required packages: pip install -r requirements.txt")
    sys.exit(1)

# Load environment variables
load_dotenv()


class MCPDataRequest(BaseModel):
    """Schema for MCP data requests."""
    endpoint: str = Field(..., description="MCP server endpoint to query")
    method: str = Field(default="GET", description="HTTP method (GET, POST, etc.)")
    params: Dict[str, Any] = Field(default_factory=dict, description="Query parameters")
    data: Optional[Dict[str, Any]] = Field(default=None, description="Request body data")


class FastMCPTool(BaseTool):
    """
    Custom tool for accessing FastMCP server data.
    This tool allows CrewAI agents to interact with MCP servers.
    """
    name: str = "FastMCP Data Access"
    description: str = "Access data from FastMCP servers for enhanced agent capabilities"
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        """Initialize the FastMCP tool with server configuration."""
        super().__init__()
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        
        # Set up authentication headers
        if self.api_key:
            self.session.headers.update({
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            })
        else:
            self.session.headers.update({
                'Content-Type': 'application/json'
            })
    
    def _run(self, endpoint: str, method: str = "GET", params: Dict[str, Any] = None, data: Dict[str, Any] = None) -> str:
        """
        Execute a request to the MCP server.
        
        Args:
            endpoint: API endpoint to call
            method: HTTP method
            params: Query parameters
            data: Request body data
            
        Returns:
            Response data as a string
        """
        try:
            url = f"{self.base_url}/{endpoint.lstrip('/')}"
            
            # For demo purposes, simulate MCP server responses
            if "demo" in endpoint or self.base_url == "http://localhost:8000":
                return self._simulate_mcp_response(endpoint, method, params, data)
            
            # Real MCP server request
            response = self.session.request(
                method=method.upper(),
                url=url,
                params=params,
                json=data,
                timeout=30
            )
            
            response.raise_for_status()
            result = response.json()
            
            return json.dumps(result, indent=2, ensure_ascii=False)
            
        except requests.exceptions.RequestException as e:
            error_msg = f"MCP server request failed: {e}"
            print(f"❌ {error_msg}")
            return json.dumps({"error": error_msg})
        except Exception as e:
            error_msg = f"Unexpected error accessing MCP server: {e}"
            print(f"❌ {error_msg}")
            return json.dumps({"error": error_msg})
    
    def _simulate_mcp_response(self, endpoint: str, method: str, params: Dict[str, Any] = None, data: Dict[str, Any] = None) -> str:
        """
        Simulate MCP server responses for demonstration purposes.
        This allows the lesson to run without a real MCP server.
        """
        endpoint_lower = endpoint.lower()
        
        # Simulate different MCP server endpoints
        if "weather" in endpoint_lower or "forecast" in endpoint_lower:
            return json.dumps({
                "location": params.get("location", "San Francisco, CA") if params else "San Francisco, CA",
                "temperature": "72°F",
                "conditions": "Partly cloudy",
                "humidity": "65%",
                "wind_speed": "8 mph",
                "source": "MCP Weather Service"
            }, indent=2)
        
        elif "news" in endpoint_lower or "headlines" in endpoint_lower:
            return json.dumps({
                "articles": [
                    {
                        "title": "AI Agents Revolutionize Healthcare Diagnostics",
                        "summary": "New AI agents are helping doctors diagnose diseases with 95% accuracy.",
                        "source": "Tech News Today",
                        "timestamp": "2024-01-15T10:30:00Z"
                    },
                    {
                        "title": "Multi-Agent Systems Transform Business Operations",
                        "summary": "Companies are adopting multi-agent systems to automate complex workflows.",
                        "source": "Business Weekly",
                        "timestamp": "2024-01-14T15:20:00Z"
                    }
                ],
                "source": "MCP News Aggregator"
            }, indent=2)
        
        elif "research" in endpoint_lower or "data" in endpoint_lower:
            return json.dumps({
                "query": params.get("query", "AI agents") if params else "AI agents",
                "results": [
                    {
                        "title": "The Rise of AI Agents in Modern Computing",
                        "author": "Dr. Sarah Chen",
                        "year": 2024,
                        "summary": "Comprehensive analysis of AI agent architectures and applications."
                    },
                    {
                        "title": "Multi-Agent Coordination Strategies",
                        "author": "Prof. Michael Rodriguez",
                        "year": 2023,
                        "summary": "Advanced techniques for coordinating multiple AI agents."
                    }
                ],
                "source": "MCP Research Database"
            }, indent=2)
        
        elif "health" in endpoint_lower or "medical" in endpoint_lower:
            return json.dumps({
                "symptoms": data.get("symptoms", ["headache", "fatigue"]) if data else ["headache", "fatigue"],
                "possible_conditions": [
                    "Tension headache",
                    "Migraine",
                    "Dehydration"
                ],
                "recommendations": [
                    "Stay hydrated",
                    "Get adequate rest",
                    "Consult a healthcare provider if symptoms persist"
                ],
                "source": "MCP Health Assistant",
                "disclaimer": "This is not medical advice. Please consult a healthcare professional."
            }, indent=2)
        
        else:
            # Default response
            return json.dumps({
                "message": f"MCP server received {method} request to {endpoint}",
                "timestamp": "2024-01-15T12:00:00Z",
                "status": "success",
                "data_source": "MCP Demo Server"
            }, indent=2)


class MCPIntegrationLesson:
    """Lesson 2: MCP Server Integration with CrewAI."""
    
    def __init__(self):
        """Initialize the lesson with environment setup."""
        self.setup_environment()
        self.mcp_tool = self.create_mcp_tool()
    
    def setup_environment(self):
        """Set up environment variables for MCP integration."""
        self.mcp_url = os.getenv("FASTMCP_URL", "http://localhost:8000")
        self.mcp_api_key = os.getenv("FASTMCP_API_KEY", "")
        
        print(f"✅ MCP Environment configured:")
        print(f"   MCP URL: {self.mcp_url}")
        print(f"   API Key configured: {'Yes' if self.mcp_api_key else 'No'}")
    
    def create_mcp_tool(self) -> FastMCPTool:
        """Create the MCP tool for agent integration."""
        print("🔧 Creating FastMCP tool...")
        tool = FastMCPTool(
            base_url=self.mcp_url,
            api_key=self.mcp_api_key
        )
        print("✅ FastMCP tool created successfully")
        return tool
    
    def create_mcp_agent(self) -> Agent:
        """Create an agent with MCP server access capabilities."""
        print("🤖 Creating MCP-enabled agent...")
        
        agent = Agent(
            role="Data Research Specialist",
            goal="Gather and analyze information from various data sources using MCP servers",
            backstory="You are an experienced researcher who can access multiple data sources through MCP servers. You gather information, analyze it, and provide comprehensive reports.",
            tools=[self.mcp_tool],
            verbose=True,
            allow_delegation=False
        )
        
        print("✅ MCP-enabled agent created successfully")
        return agent
    
    def create_weather_task(self, agent: Agent) -> Task:
        """Create a task to fetch weather information."""
        print("🌤️ Creating weather information task...")
        
        task = Task(
            description="Get the current weather information for San Francisco, CA using the MCP server. Analyze the data and provide a brief summary of the conditions.",
            agent=agent,
            expected_output="A brief weather summary including temperature, conditions, and any relevant details"
        )
        
        print("✅ Weather task created successfully")
        return task
    
    def create_research_task(self, agent: Agent) -> Task:
        """Create a task to conduct research using MCP data."""
        print("🔍 Creating research task...")
        
        task = Task(
            description="Use the MCP server to research the latest developments in AI agents. Gather information from multiple sources and provide a comprehensive summary of current trends and applications.",
            agent=agent,
            expected_output="A comprehensive summary of AI agent developments including trends, applications, and key insights"
        )
        
        print("✅ Research task created successfully")
        return task
    
    def execute_with_error_handling(self, agent: Agent, task: Task) -> str:
        """Execute a task with comprehensive error handling."""
        print("🚀 Executing task with error handling...")
        
        try:
            crew = Crew(
                agents=[agent],
                tasks=[task],
                verbose=True
            )
            
            result = crew.kickoff()
            return str(result)
            
        except Exception as e:
            error_msg = f"Task execution failed: {e}"
            print(f"❌ {error_msg}")
            
            # Provide helpful error information
            return f"""
            Error occurred during task execution: {str(e)}
            
            Troubleshooting steps:
            1. Verify MCP server is running and accessible
            2. Check API key configuration
            3. Ensure network connectivity
            4. Review agent permissions and tool access
            
            For this demo, here's a sample response:
            The MCP server integration allows agents to access external data sources and services.
            This enables more powerful and informed decision-making by agents.
            """
    
    def run_demo(self):
        """Run the complete lesson 2 demo."""
        print("=" * 60)
        print("🎯 CrewAI Lesson 2: MCP Server Integration")
        print("=" * 60)
        
        # Create MCP-enabled agent
        agent = self.create_mcp_agent()
        
        # Execute weather task
        print("\n🌤️ WEATHER TASK:")
        print("-" * 30)
        weather_task = self.create_weather_task(agent)
        weather_result = self.execute_with_error_handling(agent, weather_task)
        
        print(f"\nWeather Task Result:\n{weather_result}")
        
        # Execute research task
        print("\n🔍 RESEARCH TASK:")
        print("-" * 30)
        research_task = self.create_research_task(agent)
        research_result = self.execute_with_error_handling(agent, research_task)
        
        print(f"\nResearch Task Result:\n{research_result}")
        
        print("\n✅ Lesson 2 completed successfully!")
        print("📝 Next steps:")
        print("   1. Set up a real MCP server for actual data access")
        print("   2. Experiment with different endpoints and data sources")
        print("   3. Move to Lesson 3 for advanced multi-agent patterns")
        
        return {
            "weather_task": weather_result,
            "research_task": research_result
        }


def main():
    """Main function to run lesson 2."""
    print("🚀 Starting CrewAI Lesson 2: MCP Server Integration...")
    
    try:
        lesson = MCPIntegrationLesson()
        results = lesson.run_demo()
        
        print("\n🎉 Lesson 2 completed successfully!")
        return results
        
    except Exception as e:
        print(f"❌ Lesson 2 failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()