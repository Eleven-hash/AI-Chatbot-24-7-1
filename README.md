# 🤖 AI Chatbot 24/7

> **A production-ready AI chatbot powered by LangGraph, LangChain, and multiple LLM providers with web search capabilities**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-009688.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.41.1-FF4B4B.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.14-orange.svg)](https://www.langchain.com/)


---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

**AI Chatbot 24/7** is a fully functional, production-ready chatbot application that provides 24/7 automated customer support using state-of-the-art Large Language Models (LLMs). The system leverages **LangGraph** for agentic workflows, **LangChain** for orchestration, and supports multiple AI providers including **HuggingFace** and **Google Gemini**.

### Problem Statement
Users expect immediate, accurate responses to their queries at any time of day. Traditional support teams cannot provide consistent 24/7 availability at scale without significant costs.

### Solution
This chatbot leverages Generative AI to understand user intent, generate contextually relevant responses, and optionally search the web for up-to-date information—all without human intervention.

---

## ✨ Features

- 🌐 **Multi-Provider Support**: Choose between HuggingFace (Llama, Mistral, Flan-T5) and Google Gemini models
- 🔍 **Web Search Integration**: Real-time web search powered by Tavily Search API
- 🤖 **ReAct Agent Architecture**: Intelligent reasoning and action using LangGraph
- 🎨 **Beautiful UI**: Modern Streamlit frontend with neon-themed design
- ⚡ **FastAPI Backend**: High-performance REST API with automatic documentation
- 🔐 **Secure Configuration**: Environment-based API key management
- 🛠️ **Flexible Model Selection**: Dynamically switch between multiple LLM models
- 💬 **Custom System Prompts**: Define agent behavior and persona
- 📊 **Request Validation**: Pydantic-based schema validation

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface Layer                     │
│                    (Streamlit Frontend)                      │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP POST /chat
                     ↓
┌─────────────────────────────────────────────────────────────┐
│                     API Gateway Layer                        │
│                   (FastAPI Backend)                          │
│  • Request Validation (Pydantic)                             │
│  • Model Selection & Routing                                 │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────────┐
│                    AI Agent Layer                            │
│                  (LangGraph ReAct Agent)                     │
│  ┌──────────────────────────────────────────┐                │
│  │         LLM Provider Router              │                │
│  │  ┌──────────────┐  ┌──────────────┐     │                │
│  │  │ HuggingFace  │  │Google Gemini │     │                │
│  │  └──────────────┘  └──────────────┘     │                │
│  └──────────────────────────────────────────┘                │
│                                                               │
│  ┌──────────────────────────────────────────┐                │
│  │            Tool Integration              │                │
│  │  • Tavily Web Search (Optional)          │                │
│  └──────────────────────────────────────────┘                │
└─────────────────────────────────────────────────────────────┘
                     │
                     ↓
            ┌────────────────┐
            │   Final Response│
            └────────────────┘
```

### Component Flow

1. **User Interface** (Streamlit): Collects user input, system prompts, model preferences
2. **API Gateway** (FastAPI): Validates requests and routes to appropriate AI agent
3. **AI Agent** (LangGraph): Creates ReAct agent with selected LLM and tools
4. **Response Generation**: Agent reasons, optionally searches web, and generates response

---

## 🛠️ Tech Stack

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework for building APIs
- **[Pydantic](https://docs.pydantic.dev/)** - Data validation using Python type annotations
- **[Uvicorn](https://www.uvicorn.org/)** - Lightning-fast ASGI server

### Frontend
- **[Streamlit](https://streamlit.io/)** - Rapid UI development framework

### AI/ML Stack
- **[LangChain](https://www.langchain.com/)** - LLM orchestration framework
- **[LangGraph](https://langchain-ai.github.io/langgraph/)** - Agent workflow management
- **[HuggingFace](https://huggingface.co/)** - Open-source LLM provider
- **[Google Gemini](https://deepmind.google/technologies/gemini/)** - Google's multimodal AI
- **[Tavily](https://tavily.com/)** - AI-optimized search API

### Utilities
- **python-dotenv** - Environment variable management
- **requests** - HTTP library for API calls

---

## 📦 Prerequisites

- **Python 3.9+** installed on your system
- **pip** package manager
- API Keys for:
  - [HuggingFace](https://huggingface.co/settings/tokens) (for HuggingFace models)
  - [Google AI Studio](https://makersuite.google.com/app/apikey) (for Gemini models)
  - [Tavily](https://tavily.com/) (for web search functionality)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Chatbot-24-7.git
cd AI-Chatbot-24-7
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### 1. Create Environment File

Create a `.env` file in the project root:

```bash
# .env
TAVILY_API_KEY=your_tavily_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
```

### 2. Get API Keys

| Provider | Sign Up Link | Key Location |
|----------|-------------|--------------|
| **Tavily** | [tavily.com](https://tavily.com/) | Dashboard → API Keys |
| **Gemini** | [Google AI Studio](https://makersuite.google.com/app/apikey) | Get API Key button |
| **HuggingFace** | [HuggingFace Settings](https://huggingface.co/settings/tokens) | Access Tokens → New Token |

> ⚠️ **Security Note**: Never commit your `.env` file to version control. It's already in `.gitignore`.

---

## 🎮 Usage

### Running the Application

You need to run **two separate terminals**:

#### Terminal 1: Start Backend API

```bash
python backend.py
```

Expected output:
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:9999
```

#### Terminal 2: Start Frontend UI

```bash
streamlit run frontend.py
```

Expected output:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

### Accessing the Application

- **Frontend UI**: Open [http://localhost:8501](http://localhost:8501) in your browser
- **API Docs**: Visit [http://127.0.0.1:9999/docs](http://127.0.0.1:9999/docs) for interactive Swagger documentation
- **ReDoc**: Alternative docs at [http://127.0.0.1:9999/redoc](http://127.0.0.1:9999/redoc)

### Using the Chatbot

1. **Navigate** to the Streamlit frontend at `http://localhost:8501`
2. **Define System Prompt** (optional): Set the agent's behavior and persona
3. **Select Provider**: Choose between HuggingFace or Gemini
4. **Select Model**: Pick a specific model from the dropdown
5. **Enable Web Search** (optional): Check the box to allow real-time web searches
6. **Enter Query**: Type your question or request
7. **Click "Ask Agent!"**: Submit and receive AI-generated response

---

## 📡 API Documentation

### POST `/chat`

Send a query to the chatbot and receive an AI-generated response.

#### Request Body

```json
{
  "model_name": "gemini-1.5-flash",
  "model_provider": "gemini",
  "system_prompt": "You are a helpful assistant.",
  "messages": ["What is the capital of France?"],
  "allow_search": false
}
```

#### Parameters

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `model_name` | string | Yes | Model identifier (must be from allowed list) |
| `model_provider` | string | Yes | `huggingFace` or `gemini` |
| `system_prompt` | string | Yes | Instructions for agent behavior |
| `messages` | array[string] | Yes | List of user queries |
| `allow_search` | boolean | Yes | Enable/disable web search |

#### Allowed Models

**HuggingFace:**
- `meta-llama/Llama-3.1-8B-Instruct`
- `google/flan-t5-large`
- `tiiuae/falcon-7b-instruct`
- `zai-org/GLM-4.7-Flash`

**Gemini:**
- `gemini-1.5-flash`
- `gemini-2.5-flash-lite`
- `gemini-1.5-extended`

#### Response

```json
"Paris is the capital of France."
```

#### Error Response

```json
{
  "error": "Invalid model name. Kindly select a valid AI model"
}
```

---

## 📁 Project Structure

```
AI-Chatbot-24-7/
│
├── 📄 ai_agent.py           # Core AI agent logic with LangGraph
├── 📄 backend.py            # FastAPI server & API endpoints
├── 📄 frontend.py           # Streamlit web interface
│
├── 📄 requirements.txt      # Python dependencies
├── 📄 Pipfile              # Pipenv configuration
├── 📄 Pipfile.lock         # Locked dependencies
│
├── 📄 .env                 # Environment variables (not in repo)
├── 📄 .gitignore           # Git ignore rules
│
├── 📁 venv/                # Virtual environment (gitignored)
├── 📁 __pycache__/         # Python cache (gitignored)
│
└── 📄 README.md            # This file
```

### File Descriptions

| File | Description |
|------|-------------|
| **ai_agent.py** | Contains `get_response_from_ai_agent()` function that creates LangGraph ReAct agents with specified LLM and tools |
| **backend.py** | FastAPI application with `/chat` endpoint, request validation, and model routing |
| **frontend.py** | Streamlit UI with model selection, web search toggle, and response display |
| **requirements.txt** | All Python package dependencies with pinned versions |

---

## 🐛 Troubleshooting

### Common Issues

#### 1. "Module not found" Error

**Problem**: Missing dependencies

**Solution**:
```bash
pip install -r requirements.txt
```

#### 2. "Connection Error" in Frontend

**Problem**: Backend not running

**Solution**: 
- Ensure `backend.py` is running on port 9999
- Check for error messages in the backend terminal

#### 3. API Key Errors

**Problem**: Missing or invalid API keys

**Solution**:
- Verify `.env` file exists in project root
- Check that all required keys are present and valid
- Restart both backend and frontend after adding keys

#### 4. "Unsupported provider" Error

**Problem**: Provider name mismatch

**Solution**:
- Ensure provider is exactly `huggingFace` or `gemini` (case-sensitive)
- Check for extra whitespace in model_provider field

#### 5. Model Not Responding (HuggingFace)

**Problem**: Some models don't support tool calling

**Solution**:
- Try a different model (Llama-3.1 recommended)
- Disable web search for unsupported models
- Check model compatibility with `ChatHuggingFace`

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [LangChain](https://www.langchain.com/) for the excellent LLM orchestration framework
- [LangGraph](https://langchain-ai.github.io/langgraph/) for agent workflow capabilities
- [Tavily](https://tavily.com/) for the AI-optimized search API
- [FastAPI](https://fastapi.tiangolo.com/) for the high-performance web framework
- [Streamlit](https://streamlit.io/) for making beautiful UIs simple

---

## 📞 Support

For questions, issues, or suggestions:
- **Open an Issue**: [GitHub Issues](https://github.com/yourusername/AI-Chatbot-24-7/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/AI-Chatbot-24-7/discussions)

---

**Built with ❤️ using LangGraph, LangChain, and modern AI technologies**
