import streamlit as st
import requests

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="🌈 AI Chat Agent",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Custom CSS for aesthetics
# -------------------------------
st.markdown("""
<style>
/* Background gradient */
body {
    background: linear-gradient(120deg, #f6d365, #fda085);
}

/* Title style */
h1 {
    color: #4B0082;
    font-family: 'Comic Sans MS', cursive, sans-serif;
    font-size: 3rem;
}

/* Text area styling */
textarea {
    border: 2px solid #4B0082;
    border-radius: 10px;
    padding: 10px;
}

/* Button style */
div.stButton > button:first-child {
    background-color: #4B0082;
    color:white;
    height: 3em;
    width: 100%;
    border-radius: 10px;
    font-size: 1.2em;
}

div.stButton > button:first-child:hover {
    background-color: #8A2BE2;
    color:white;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar for settings
# -------------------------------
with st.sidebar:
    st.header("🤖 AI Agent Settings")
    provider = st.radio("Select Provider:", {"Groq", "OpenAI"})
    
    if provider == "Groq":
        selected_model = st.selectbox(
            "Select Groq model:",
            ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
        )
    elif provider == "OpenAI":
        selected_model = st.selectbox(
            "Select OpenAI model:",
            ["gpt-4o-mini"]
        )
        
    allow_web_search = st.checkbox("Allow Web Search")

# -------------------------------
# Main page
# -------------------------------
st.title("🌟 Chat with Your AI Agent")
st.write("Type your query and let the AI answer you!")

system_prompt = st.text_area(
    "Define your AI Agent:",
    height=70,
    placeholder="Type your system prompt here..."
)

user_query = st.text_area(
    "Enter your query:",
    height=150,
    placeholder="Ask anything..."
)

api_url = "http://127.0.0.1:9999/chat"

if st.button("💬 Ask Agent!"):
    if user_query.strip():
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        try:
            response = requests.post(api_url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if "error" in data:
                    st.error(data["error"])
                else:
                    st.subheader("🧠 AI Response")
                    st.markdown(f"**{data['response']}**")
            else:
                st.error("⚠️ Error connecting to backend.")
        except requests.exceptions.ConnectionError:
            st.error("⚠️ Backend server is not running. Start your backend first.")
