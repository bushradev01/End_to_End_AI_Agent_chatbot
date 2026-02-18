🤖 End-to-End AI Agent Chatbot

An intelligent AI-powered chatbot built using FastAPI, Streamlit, and LangGraph with support for multiple LLM providers and optional web search.

🚀 What This Project Can Do

This chatbot supports:

🔁 Dynamic model switching (Groq / OpenAI)

🧠 Custom system prompts

🌍 Optional live web search using Tavily

⚡ FastAPI backend for API handling

🎨 Streamlit frontend with interactive UI

🔐 Secure API key management using .env

🧩 LangGraph ReAct Agent architecture

🏗️ Project Architecture

User → Streamlit UI → FastAPI Backend → LangGraph Agent → LLM → (Optional Search Tool)

🖥️ How To Open and Run This Project Locally

Follow these steps:

1️⃣ Clone the Repository
git clone https://github.com/bushradev01/End_to_End_AI_Agent_chatbot.git
cd End_to_End_AI_Agent_chatbot

2️⃣ Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

Mac/Linux
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies

If using Pipfile:

pip install pipenv
pipenv install


Or if using requirements.txt:

pip install -r requirements.txt

4️⃣ Setup Environment Variables

Create a .env file in the root directory:

GROQ_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here


⚠️ Important: Do NOT upload your .env file to GitHub.

▶️ Running The Application
Step 1 — Start Backend
python backend.py


Backend runs at:

http://127.0.0.1:9999

Step 2 — Start Frontend

Open a new terminal:

streamlit run frontend.py


Frontend runs at:

http://localhost:8501
