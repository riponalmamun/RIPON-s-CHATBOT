from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq   # ✅ use Groq wrapper
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq model
model = ChatGroq(
    model="llama-3.1-8b-instant",   # You can change to "mixtral-8x7b-32768" or "gemma-7b-it"
    temperature=0.7
)

# Define the prompt template
template2 = PromptTemplate(
    template="Greet this person in 5 languages. The name of the person is {name}",
    input_variables=["name"]
)

# Fill the values of the placeholders
prompt = template2.invoke({"name": "nitish"})

# Get model response
result = model.invoke(prompt)

print(result.content)
