import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Load API key from .env
load_dotenv()

# Initialize Groq model
model = ChatGroq(
    model="llama-3.1-8b-instant",  # Change to "mixtral-8x7b-32768" or "gemma-7b-it" if needed
    temperature=0.7
)

# Streamlit UI
st.header('🧑‍🔬 Research Tool')

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# Directly create the prompt template (no template.json needed)
template = PromptTemplate.from_template(
    "Explain the research paper '{paper_input}' in a {style_input} style. "
    "The explanation should be {length_input}."
)

if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    })
    
    st.subheader("📑 Explanation")
    st.write(result.content)
