# chatbot.py
import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from messages import init_history, add_message, get_history, clear_history

# Load Groq API key from .env
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.header("🤖 RIPON's Chatbot")
st.write("Ask me anything! I can answer questions, generate text, or summarize content.")

# Initialize chat history
init_history(st.session_state)

# User input
user_input = st.text_area("Type your question or request:")

# Temperature slider
temperature = st.slider("Creativity (Temperature)", 0.0, 1.0, 0.7, 0.05)

# Model selection
model_choice = st.selectbox(
    "Choose AI Model",
    ["llama-3.1-8b-instant", "mixtral-8x7b-32768", "gemma-7b-it"]
)

# Clear chat button
if st.button("Clear Chat"):
    clear_history(st.session_state)
    st.experimental_rerun()

# Send button
if st.button("Send"):
    if not user_input.strip():
        st.warning("Please type a question or request.")
    else:
        # Add user message to history
        add_message(st.session_state, "user", user_input)

        # Create a new ChatGroq instance for this query
        model_instance = ChatGroq(
            model=model_choice,
            temperature=temperature
        )

        # Build prompt
        template = PromptTemplate.from_template(
            "You are a helpful assistant. Answer the following:\n\n\"\"\"\n{user_input}\n\"\"\""
        )
        prompt = template.invoke({"user_input": user_input})

        # Get model response
        result = model_instance.invoke(prompt)

        # Add bot response to history
        add_message(st.session_state, "bot", result.content)

# Display chat history
for msg in get_history(st.session_state):
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}\n")
