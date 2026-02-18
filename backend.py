# backend.py

# Step 1: Setup Pydantic model (schema validation)
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES = ["llama-3-70b-8192", "llama-3.3-70b-versatile", "gpt-4o-mini"]

app = FastAPI(title="LangGraph AI Agent")

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in request.
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}

    llm_id = request.model_name
    query = request.messages[-1]  # take last message as string
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    response = get_response_from_ai_agent(
        llm_id,
        query,
        allow_search,
        system_prompt,
        provider
    )

    return {"response": response}


if __name__ == "__main__":
    import uvicorn
    # ⚡ Make sure host is 127.0.0.1 and port matches frontend
    uvicorn.run(app, host="127.0.0.1", port=9999, reload=True)
