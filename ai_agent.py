# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#Step1: Setup API Keys for Groq, OpenAI and Tavily
import os
from dotenv import load_dotenv

# Ensure load_dotenv() is called before anything else
load_dotenv()

# Fetch keys - use GEMINI_API_KEY as per your variable name
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage, HumanMessage

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    # 1. Initialize the correct LLM based on provider
    if provider == "Groq":
        # ChatGroq automatically looks for GROQ_API_KEY in environment
        llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=GROQ_API_KEY)
    elif provider == "gemini":
        # Standardize the parameter to api_key
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", google_api_key=GEMINI_API_KEY)
    else:
        raise ValueError(f"Unsupported provider: {provider}")

    # 2. Setup Tools
    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    # 3. Create the ReAct Agent
    agent = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )

    # 4. Prepare state - LangGraph expects a list of messages
    state = {"messages": [HumanMessage(content=query)]}
    
    # 5. Invoke and Parse
    response = agent.invoke(state)
    messages = response.get("messages")
    
    # Return the last AI Message content
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1] if ai_messages else "No response generated."
print("AI Agent module loaded successfully.")