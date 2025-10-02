import os
import gradio as gr
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Load Groq API key from environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq model
model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    api_key=GROQ_API_KEY
)

# Chat function
def chat_with_groq(user_input):
    if not user_input.strip():
        return "Please enter a message."
    template = PromptTemplate.from_template(
        "You are a helpful assistant. Answer the following:\n\n\"\"\"\n{user_input}\n\"\"\""
    )
    prompt = template.invoke({"user_input": user_input})
    result = model.invoke(prompt)
    return result.content

# Gradio UI
demo = gr.Interface(
    fn=chat_with_groq,
    inputs="text",
    outputs="text",
    title="Groq Chatbot",
    description="Ask me anything! Powered by Groq + LangChain."
)

demo.launch()
