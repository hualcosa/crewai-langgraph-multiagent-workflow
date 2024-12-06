# AI Workflow Assistant

An intelligent workflow system that processes user queries, handles email responses, and provides weather information using LangGraph and CrewAI. This project is based on the [comprehensive LangGraph guide](https://www.ionio.ai/blog/a-comprehensive-guide-about-langgraph-code-included#mini-project-let%E2%80%99s-create-a-multi-purpose-ai-agent) by Shivam Danawale and Pranav Patel at Ionio.ai, with modifications to use Claude 3.5 Sonnet via AWS Bedrock instead of OpenAI's GPT models.

## 🌟 Features

- **Email Processing**
  - Automatic email classification (Important/Casual)
  - Context-aware email response generation
  - Professional/casual tone adaptation based on email category

- **Weather Information**
  - Location-based weather data retrieval
  - Integration with OpenWeatherMap API
  - Natural language weather query processing

- **General Query Handling**
  - Intelligent query categorization
  - State-based workflow management
  - Flexible response generation

## 🛠 How It Works

The system uses LangGraph to create a flexible, state-based workflow that can:

1. **Analyze Input**: Categorizes user queries into email, weather, or general inquiries
2. **Route Requests**: Directs queries to specialized nodes based on category
3. **Process Tasks**: Uses CrewAI to orchestrate multiple AI agents for complex tasks
4. **Maintain Context**: Manages conversation state throughout the interaction

The workflow is visualized as a directed graph, making it easy to understand and modify the system's behavior.

## 🛠️ Technology Stack

- Python 3.11+
- LangGraph for workflow management
- CrewAI for agent orchestration
- Claude 3.5 Sonnet (via AWS Bedrock)
- OpenWeatherMap API
- Poetry for dependency management

## 📋 Prerequisites

- Python 3.11 or higher
- AWS account with Bedrock access
- OpenWeatherMap API key
- Poetry package manager

## 🚀 Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <project-directory>
```

2. Install dependencies using Poetry:

```bash
poetry install
```

3. Set up environment variables:

```bash
cp .env.example .env
```

Edit `.env` file with your credentials:
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-west-2
OPENWEATHERMAP_API_KEY=your_api_key
```

## 💻 Usage

```python
# Example: Process an email query
query = """
Can you reply to this email:

Hello,
Thank you for applying to xyz company.
Can you share your previous CTC?
Thanks,
HR
"""
inputs = {"query": query, "messages": [query]}
result = app.invoke(inputs)
print("Agent Response:", result['messages'][-1])
```

## 🏗️ Project Structure

```
.
├── src/
│   ├── agents/          # Agent definitions
│   ├── crews/           # Crew configurations
│   ├── nodes/           # Workflow nodes
│   ├── tasks/           # Task definitions
│   └── workflows/       # Workflow configurations
├── main.py             # Application entry point
└── config.py           # Configuration settings
```

## 🙏 Acknowledgments

This project is based on the excellent work by:
- [Shivam Danawale](https://www.ionio.ai/blog/a-comprehensive-guide-about-langgraph-code-included) - Original tutorial author
- [Pranav Patel](https://www.ionio.ai) - Editor of the original tutorial
- The teams behind LangGraph and CrewAI

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
