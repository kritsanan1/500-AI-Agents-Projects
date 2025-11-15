# CrewAI with FastMCP Server Integration Course

A comprehensive course teaching beginners how to integrate CrewAI with FastMCP servers through step-by-step programming examples.

## 🎯 Course Overview

This course is designed for beginner developers with basic Python knowledge who want to learn how to integrate CrewAI agents with FastMCP servers. The course covers fundamental concepts, practical implementation, and advanced patterns for building intelligent agent workflows.

## 📚 Lessons

### Lesson 1: Setting up CrewAI with MCP Server Access
- Install required packages
- Set up environment variables
- Create a basic CrewAI agent
- Execute simple tasks

### Lesson 2: Integrating MCP Server with CrewAI
- Create custom tools for MCP server access
- Configure authentication and connection settings
- Use MCP server data in agent tasks
- Handle errors and exceptions

### Lesson 3: Advanced CrewAI Patterns with MCP Server
- Implement multi-agent workflows
- Use hierarchical processes
- Share data between agents through the MCP server
- Store and retrieve research findings
- Implement quality assurance processes

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key
- Basic understanding of Python programming

### Installation

1. **Clone or download this course**
```bash
cd crewai_mcp_course
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
export OPENAI_API_KEY="your-openai-api-key"
export FASTMCP_URL="http://your-fastmcp-server:port"
export FASTMCP_API_KEY="your-mcp-api-key"  # Optional
```

4. **Run the lessons**
```bash
# Lesson 1
python lesson1_setup.py

# Lesson 2
python lesson2_mcp_integration.py

# Lesson 3
python lesson3_advanced_patterns.py
```

## 📋 Running Each Lesson

### Lesson 1: Basic Setup
```bash
python lesson1_setup.py
```
This lesson introduces CrewAI basics and creates your first agent.

### Lesson 2: MCP Integration
```bash
python lesson2_mcp_integration.py
```
This lesson shows how to integrate MCP servers with CrewAI agents.

### Lesson 3: Advanced Patterns
```bash
python lesson3_advanced_patterns.py
```
This lesson demonstrates advanced multi-agent workflows.

## 🧪 Testing

Run the test suite to verify everything is working:

```bash
python test_course.py
```

This will test all three lessons and provide a summary of results.

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the course directory:

```env
OPENAI_API_KEY=your-openai-api-key-here
FASTMCP_URL=http://localhost:8000
FASTMCP_API_KEY=your-mcp-api-key-here
```

### MCP Server Setup

For production use, you'll need to set up a FastMCP server. For learning purposes, the lessons include simulation capabilities.

## 📖 Learning Path

1. **Start with Lesson 1** to understand CrewAI fundamentals
2. **Proceed to Lesson 2** to learn MCP server integration
3. **Complete Lesson 3** to master advanced patterns
4. **Experiment** with the code and customize for your use cases

## 🛠️ What You'll Learn

By completing this course, you'll be able to:

- ✅ Create and configure CrewAI agents
- ✅ Integrate MCP servers with agent workflows
- ✅ Build complex multi-agent systems
- ✅ Implement data sharing between agents
- ✅ Design robust error handling for production systems
- ✅ Use both sequential and hierarchical workflow patterns

## 📝 Features

- **Step-by-step tutorials** with clear explanations
- **Working code examples** for immediate use
- **Error handling** and best practices
- **Data sharing** mechanisms between agents
- **Quality assurance** processes
- **Production-ready** patterns and practices

## 🔍 Code Structure

```
crewai_mcp_course/
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
├── metadata.yaml                      # Project metadata
├── lesson1_setup.py                   # Lesson 1: Basic setup
├── lesson2_mcp_integration.py       # Lesson 2: MCP integration
├── lesson3_advanced_patterns.py       # Lesson 3: Advanced patterns
└── test_course.py                     # Test suite
```

## 🚨 Important Notes

- **Demo Mode**: The lessons include simulation capabilities for learning without a real MCP server
- **API Keys**: You'll need an OpenAI API key to run the examples
- **Security**: Never commit your API keys to version control
- **Error Handling**: All lessons include comprehensive error handling

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are installed
2. **API Key Issues**: Verify your OpenAI API key is set correctly
3. **MCP Server Connection**: Check your MCP server URL and connectivity
4. **Permission Errors**: Ensure you have write permissions in the course directory

### Getting Help

- Check the error messages in the console output
- Review the code comments and docstrings
- Verify your environment variables are set correctly
- Run the test suite to identify specific issues

## 🎯 Next Steps

After completing this course:

1. **Build your own multi-agent systems** using the patterns learned
2. **Integrate with real MCP servers** for production applications
3. **Explore monitoring and observability** tools for your agents
4. **Deploy your solutions** to cloud platforms
5. **Contribute to the community** by sharing your implementations

## 📄 License

This course is licensed under the MIT License. See the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, improvements, or additional lessons.

## 📞 Support

For questions or support:
- Open an issue in this repository
- Check the existing documentation and comments in the code
- Review the troubleshooting section above

---

**Happy Learning!** 🚀

Start with Lesson 1 and work your way through the course to master CrewAI and MCP server integration!