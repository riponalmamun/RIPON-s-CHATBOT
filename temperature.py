import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

model_id = "llama-3.1-8b-instant"
prompt = "Write a 5 line poem on cricket"

chat_completion = client.chat.completions.create(
    model=model_id,
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": prompt}
    ]
)

# Access the content properly
print(chat_completion.choices[0].message.content)
