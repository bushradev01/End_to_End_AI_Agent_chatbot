# ai_agent.py

import os
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
openai_apikey = os.getenv("OPENAI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

print("Groq:", groq_api_key)
print("OpenAI:", openai_apikey)
print("Tavily:", tavily_api_key)

# LLMs and tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

# Main function to call from FastAPI
def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if isinstance(query, list):
        query = query[-1]

    # Select LLM provider
    if provider == "Groq":
        llm = ChatGroq(model=llm_id, api_key=groq_api_key)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id, api_key=openai_apikey)
    else:
        raise ValueError("Unsupported provider. Use 'Groq' or 'OpenAI'")

    # Select tools
    tools = []
    if allow_search:
        tools = [TavilySearchResults(tavily_api_key=tavily_api_key, max_results=2)]

    # Create LangGraph agent
    agent = create_react_agent(model=llm, tools=tools)

    # Create state
    state = {"messages": [("system", system_prompt), ("user", query)]}

    response = agent.invoke(state)
    messages = response.get("messages", [])

    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]

    return ai_messages[-1] if ai_messages else "No response generated."
