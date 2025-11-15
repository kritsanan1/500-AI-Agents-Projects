#!/usr/bin/env python3
"""
Lesson 3: Advanced CrewAI Patterns with MCP Server

This lesson demonstrates:
- Implementing multi-agent workflows
- Using hierarchical processes
- Sharing data between agents through the MCP server
- Storing and retrieving research findings
- Implementing quality assurance processes
"""

import os
import sys
import json
import time
from typing import Dict, Any, List, Optional
from datetime import datetime
from dotenv import load_dotenv

try:
    from crewai import Agent, Task, Crew
    from crewai.process import Process
    from crewai_tools import BaseTool
    from pydantic import BaseModel, Field
except ImportError as e:
    print(f"Error importing dependencies: {e}")
    print("Please install required packages: pip install -r requirements.txt")
    sys.exit(1)

# Load environment variables
load_dotenv()

# Import the MCP tool from lesson 2
from lesson2_mcp_integration import FastMCPTool, MCPDataRequest


class ResearchDataStore:
    """In-memory data store for sharing research findings between agents."""
    
    def __init__(self):
        self.data: Dict[str, Any] = {}
        self.timestamps: Dict[str, datetime] = {}
    
    def store(self, key: str, value: Any) -> None:
        """Store data with timestamp."""
        self.data[key] = value
        self.timestamps[key] = datetime.now()
    
    def retrieve(self, key: str) -> Optional[Any]:
        """Retrieve stored data."""
        return self.data.get(key)
    
    def get_all_keys(self) -> List[str]:
        """Get all stored keys."""
        return list(self.data.keys())
    
    def get_recent(self, minutes: int = 60) -> Dict[str, Any]:
        """Get data stored within the last N minutes."""
        recent_data = {}
        cutoff_time = datetime.now() - timedelta(minutes=minutes)
        
        for key, timestamp in self.timestamps.items():
            if timestamp > cutoff_time:
                recent_data[key] = self.data[key]
        
        return recent_data


class AdvancedMCPTool(FastMCPTool):
    """Enhanced MCP tool with advanced features for multi-agent workflows."""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None, data_store: Optional[ResearchDataStore] = None):
        super().__init__(base_url, api_key)
        self.data_store = data_store or ResearchDataStore()
    
    def store_research_data(self, key: str, data: Any) -> str:
        """Store research data for sharing between agents."""
        try:
            self.data_store.store(key, data)
            return f"✅ Data stored successfully with key: {key}"
        except Exception as e:
            return f"❌ Failed to store data: {str(e)}"
    
    def retrieve_research_data(self, key: str) -> str:
        """Retrieve stored research data."""
        try:
            data = self.data_store.retrieve(key)
            if data:
                return json.dumps(data, indent=2)
            else:
                return f"❌ No data found for key: {key}"
        except Exception as e:
            return f"❌ Failed to retrieve data: {str(e)}"
    
    def get_research_summary(self) -> str:
        """Get a summary of all stored research data."""
        try:
            all_keys = self.data_store.get_all_keys()
            if not all_keys:
                return "📊 No research data currently stored"
            
            summary = f"📊 Research Data Summary\n"
            summary += f"Total datasets: {len(all_keys)}\n"
            summary += f"Available keys: {', '.join(all_keys)}\n"
            
            return summary
        except Exception as e:
            return f"❌ Failed to generate summary: {str(e)}"


class AdvancedCrewAIWorkflows:
    """Advanced CrewAI workflows with MCP server integration."""
    
    def __init__(self):
        """Initialize the advanced workflow system."""
        self.setup_environment()
        self.data_store = ResearchDataStore()
        self.mcp_tool = self.create_advanced_mcp_tool()
    
    def setup_environment(self):
        """Set up the environment for advanced workflows."""
        self.mcp_url = os.getenv("FASTMCP_URL", "http://localhost:8000")
        self.mcp_api_key = os.getenv("FASTMCP_API_KEY", "")
        
        print(f"✅ Advanced workflow environment configured")
        print(f"   MCP URL: {self.mcp_url}")
    
    def create_advanced_mcp_tool(self) -> AdvancedMCPTool:
        """Create the advanced MCP tool with data store."""
        return AdvancedMCPTool(
            base_url=self.mcp_url,
            api_key=self.mcp_api_key,
            data_store=self.data_store
        )
    
    def create_researcher_agent(self) -> Agent:
        """Create a researcher agent that gathers information."""
        print("🔬 Creating researcher agent...")
        
        return Agent(
            role="AI Research Specialist",
            goal="Conduct thorough research on AI agents, their applications, and latest developments",
            backstory="You are an expert AI researcher with deep knowledge of artificial intelligence, machine learning, and multi-agent systems. You excel at finding relevant information and analyzing trends.",
            tools=[self.mcp_tool],
            verbose=True,
            allow_delegation=False
        )
    
    def create_data_analyst_agent(self) -> Agent:
        """Create a data analyst agent that processes information."""
        print("📊 Creating data analyst agent...")
        
        return Agent(
            role="Data Analysis Expert",
            goal="Analyze research data, identify patterns, and extract meaningful insights",
            backstory="You are a skilled data analyst who can process complex information, identify trends, and create actionable insights from research findings.",
            tools=[self.mcp_tool],
            verbose=True,
            allow_delegation=False
        )
    
    def create_writer_agent(self) -> Agent:
        """Create a writer agent that creates reports."""
        print("✍️ Creating writer agent...")
        
        return Agent(
            role="Technical Writer",
            goal="Create comprehensive, well-structured reports based on research and analysis",
            backstory="You are an experienced technical writer who can transform complex research findings into clear, engaging, and informative reports for various audiences.",
            tools=[self.mcp_tool],
            verbose=True,
            allow_delegation=False
        )
    
    def create_reviewer_agent(self) -> Agent:
        """Create a quality assurance reviewer agent."""
        print("👀 Creating quality reviewer agent...")
        
        return Agent(
            role="Quality Assurance Reviewer",
            goal="Review and validate the quality, accuracy, and completeness of reports",
            backstory="You are a meticulous reviewer who ensures all reports meet high standards of quality, accuracy, and completeness. You check for factual accuracy and provide constructive feedback.",
            tools=[self.mcp_tool],
            verbose=True,
            allow_delegation=False
        )
    
    def create_research_task(self, researcher: Agent) -> Task:
        """Create a comprehensive research task."""
        print("🔍 Creating comprehensive research task...")
        
        return Task(
            description="""
            Conduct comprehensive research on AI agents using the MCP server. Your research should cover:
            
            1. Current state of AI agent technology
            2. Key applications across different industries
            3. Latest developments and breakthroughs
            4. Challenges and limitations
            5. Future trends and opportunities
            
            Use the MCP server to gather data from multiple sources including:
            - Recent research papers and publications
            - Industry reports and case studies
            - News articles and press releases
            - Technical documentation and specifications
            
            Store all research findings in the shared data store for other agents to access.
            """,
            agent=researcher,
            expected_output="Comprehensive research data stored in the shared data store covering all aspects of AI agents"
        )
    
    def create_analysis_task(self, analyst: Agent) -> Task:
        """Create a data analysis task."""
        print("📈 Creating data analysis task...")
        
        return Task(
            description="""
            Analyze the research data gathered by the researcher agent. Your analysis should include:
            
            1. Key trends and patterns in AI agent development
            2. Most significant applications by industry
            3. Technological breakthroughs and their impact
            4. Market opportunities and growth areas
            5. Technical challenges that need to be addressed
            
            Access the research data from the shared data store, process it thoroughly, and provide
            actionable insights that can be used to create a comprehensive report.
            
            Store your analysis results back in the data store for the writer agent to use.
            """,
            agent=analyst,
            expected_output="Detailed analysis of AI agent trends, patterns, and insights stored in the shared data store"
        )
    
    def create_writing_task(self, writer: Agent) -> Task:
        """Create a report writing task."""
        print("📝 Creating report writing task...")
        
        return Task(
            description="""
            Create a comprehensive report on "The State of AI Agents in 2024" based on the research and analysis data.
            
            Your report should be structured as follows:
            
            1. Executive Summary
               - Key findings and insights
               - Major trends and developments
               - Recommendations for stakeholders
            
            2. Current Landscape
               - Technology overview
               - Market size and growth
               - Key players and ecosystems
            
            3. Industry Applications
               - Healthcare applications
               - Financial services
               - Manufacturing and automation
               - Customer service
               - Other significant sectors
            
            4. Technical Developments
               - Recent breakthroughs
               - Emerging architectures
               - Performance improvements
            
            5. Challenges and Limitations
               - Technical challenges
               - Ethical considerations
               - Regulatory landscape
            
            6. Future Outlook
               - Predicted developments
               - Market opportunities
               - Investment trends
            
            7. Recommendations
               - For businesses
               - For developers
               - For policymakers
            
            Access the research data and analysis results from the shared data store
            to ensure your report is comprehensive and accurate.
            
            The report should be professional, well-structured, and suitable for
            executive-level readers while being technically accurate.
            """,
            agent=writer,
            expected_output="Comprehensive professional report on AI agents with all sections completed"
        )
    
    def create_review_task(self, reviewer: Agent) -> Task:
        """Create a quality review task."""
        print("🔍 Creating quality review task...")
        
        return Task(
            description="""
            Review the comprehensive report on AI agents created by the writer agent.
            
            Your review should check for:
            
            1. Content Accuracy
               - All facts and data points are correct
               - Sources are properly attributed
               - Technical details are accurate
            
            2. Structure and Flow
               - Logical organization of sections
               - Smooth transitions between topics
               - Clear and coherent narrative
            
            3. Completeness
               - All required sections are present
               - Key topics are adequately covered
               - No significant omissions
            
            4. Professional Quality
               - Appropriate tone and language
               - Suitable for target audience
               - Consistent formatting and style
            
            5. Actionable Insights
               - Practical recommendations
               - Strategic insights
               - Forward-looking perspectives
            
            Provide detailed feedback on any issues found and suggest improvements.
            If the report meets quality standards, approve it for final delivery.
            """,
            agent=reviewer,
            expected_output="Quality review report with feedback, suggestions, and approval status"
        )
    
    def run_hierarchical_workflow(self) -> Dict[str, Any]:
        """Run a hierarchical multi-agent workflow."""
        print("🏗️ Running hierarchical multi-agent workflow...")
        
        # Create agents
        researcher = self.create_researcher_agent()
        analyst = self.create_data_analyst_agent()
        writer = self.create_writer_agent()
        reviewer = self.create_reviewer_agent()
        
        # Create tasks
        research_task = self.create_research_task(researcher)
        analysis_task = self.create_analysis_task(analyst)
        writing_task = self.create_writing_task(writer)
        review_task = self.create_review_task(reviewer)
        
        # Create crew with hierarchical process
        crew = Crew(
            agents=[researcher, analyst, writer, reviewer],
            tasks=[research_task, analysis_task, writing_task, review_task],
            process=Process.hierarchical,
            manager_agent=None,  # Let CrewAI manage the workflow
            verbose=True
        )
        
        print("🚀 Executing hierarchical workflow...")
        result = crew.kickoff()
        
        return {
            "result": str(result),
            "agents": [researcher.role, analyst.role, writer.role, reviewer.role],
            "tasks_executed": len([research_task, analysis_task, writing_task, review_task])
        }
    
    def run_sequential_workflow(self) -> Dict[str, Any]:
        """Run a sequential multi-agent workflow."""
        print("🔄 Running sequential multi-agent workflow...")
        
        # Create agents
        researcher = self.create_researcher_agent()
        analyst = self.create_data_analyst_agent()
        writer = self.create_writer_agent()
        
        # Create tasks with dependencies
        research_task = self.create_research_task(researcher)
        analysis_task = self.create_analysis_task(analyst)
        writing_task = self.create_writing_task(writer)
        
        # Set up task dependencies
        analysis_task.context = [research_task]
        writing_task.context = [research_task, analysis_task]
        
        # Create crew with sequential process
        crew = Crew(
            agents=[researcher, analyst, writer],
            tasks=[research_task, analysis_task, writing_task],
            process=Process.sequential,
            verbose=True
        )
        
        print("🚀 Executing sequential workflow...")
        result = crew.kickoff()
        
        return {
            "result": str(result),
            "workflow_type": "sequential",
            "agents_involved": 3
        }
    
    def demonstrate_data_sharing(self) -> None:
        """Demonstrate data sharing between agents."""
        print("📊 Demonstrating data sharing between agents...")
        
        # Simulate data sharing
        sample_research_data = {
            "ai_agents_market_size": "$15.7 billion in 2024",
            "growth_rate": "37.3% CAGR",
            "key_applications": ["Healthcare", "Finance", "Manufacturing", "Customer Service"],
            "major_players": ["OpenAI", "Anthropic", "Google", "Microsoft"]
        }
        
        # Store data
        self.mcp_tool.store_research_data("market_research", sample_research_data)
        self.mcp_tool.store_research_data("technical_analysis", {"architecture": "multi-agent", "performance": "high"})
        
        # Retrieve data
        market_data = self.mcp_tool.retrieve_research_data("market_research")
        summary = self.mcp_tool.get_research_summary()
        
        print("✅ Data sharing demonstration completed")
        print(f"Market data retrieved: {market_data}")
        print(f"Research summary: {summary}")
    
    def run_advanced_demo(self) -> Dict[str, Any]:
        """Run the complete advanced lesson demo."""
        print("=" * 70)
        print("🎯 CrewAI Lesson 3: Advanced Multi-Agent Patterns")
        print("=" * 70)
        
        # Demonstrate data sharing
        self.demonstrate_data_sharing()
        
        print("\n🔄 SEQUENTIAL WORKFLOW:")
        print("-" * 40)
        sequential_result = self.run_sequential_workflow()
        
        print("\n🏗️ HIERARCHICAL WORKFLOW:")
        print("-" * 40)
        hierarchical_result = self.run_hierarchical_workflow()
        
        # Final summary
        final_summary = f"""
        📋 ADVANCED WORKFLOW SUMMARY
        
        Sequential Workflow Results:
        - Status: Completed
        - Agents involved: {sequential_result['agents_involved']}
        - Workflow type: {sequential_result['workflow_type']}
        
        Hierarchical Workflow Results:
        - Status: Completed
        - Agents involved: {len(hierarchical_result['agents'])}
        - Tasks executed: {hierarchical_result['tasks_executed']}
        
        Key Achievements:
        ✅ Multi-agent coordination implemented
        ✅ Data sharing between agents established
        ✅ Quality assurance processes integrated
        ✅ Both sequential and hierarchical workflows tested
        
        Advanced Features Demonstrated:
        🔄 Agent collaboration and communication
        📊 Data persistence and sharing
        🎯 Task dependencies and workflow orchestration
        🔍 Quality control and review processes
        🏗️ Complex multi-step processes
        
        This implementation showcases production-ready patterns for building
        sophisticated AI agent systems with MCP server integration.
        """
        
        print(final_summary)
        
        return {
            "sequential_workflow": sequential_result,
            "hierarchical_workflow": hierarchical_result,
            "data_sharing_demo": "completed"
        }


def main():
    """Main function to run lesson 3."""
    print("🚀 Starting CrewAI Lesson 3: Advanced Multi-Agent Patterns...")
    
    try:
        lesson = AdvancedCrewAIWorkflows()
        results = lesson.run_advanced_demo()
        
        print("\n🎉 Lesson 3 completed successfully!")
        print("🚀 You've learned advanced CrewAI patterns with MCP integration!")
        print("\n📚 Next steps:")
        print("   1. Experiment with different agent roles and workflows")
        print("   2. Implement custom tools for specific use cases")
        print("   3. Deploy your multi-agent systems to production")
        print("   4. Explore monitoring and observability tools")
        
        return results
        
    except Exception as e:
        print(f"❌ Lesson 3 failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()