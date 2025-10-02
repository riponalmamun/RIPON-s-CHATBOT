import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Load Groq API key
load_dotenv()

# Initialize Groq model
model = ChatGroq(
    model="llama-3.1-8b-instant",  # or "mixtral-8x7b-32768" / "gemma-7b-it"
    temperature=0.7
)

st.header("💬 Ask Anything")

# User input
user_input = st.text_area("Type your question or request:")

if st.button("Ask"):
    if not user_input.strip():
        st.warning("Please enter a question or request.")
    else:
        # Prompt template for a general assistant
        template = PromptTemplate.from_template(
            "You are a helpful and knowledgeable assistant. Answer the following question or request:\n\n\"\"\"\n{user_input}\n\"\"\"\n"
        )
        
        prompt = template.invoke({"user_input": user_input})
        
        # Get model response
        result = model.invoke(prompt)
        
        st.subheader("🤖 Response")
        st.write(result.content)
