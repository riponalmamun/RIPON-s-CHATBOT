# 🤖 Ripon’s Chatbot (Groq + Gradio + Hugging Face Spaces)

This is an AI-powered chatbot built using LangChain (https://www.langchain.com/) , Groq (https://groq.com/), and Gradio (https://gradio.app/) 
The chatbot is deployed on Hugging Face Spaces and supports natural language conversations with models like LLaMA-3.1-8B-Instant.

# 🚀 Features

💬 Interactive chatbot with a clean Gradio UI

⚡ Powered by Groq API for fast inference

🔒 Secure API key handling with Hugging Face Secrets

🔄 Supports different prompts via templates (prompt_template.py)

🧩 Modular codebase (chatbot.py, messages.py, prompt_ui.py)

# 🛠️ Installation (Local Setup)

Clone the repository: 
```bash
git clone https://github.com/your-username/RIPON-s-CHATBOT.git
cd RIPON-s-CHATBOT

```
Create a virtual environment:


```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

```
Install dependencies:

```bash
pip install -r requirements.txt

```

Set your Groq API Key:

```bash
export GROQ_API_KEY="your_api_key_here"   # Mac/Linux
setx GROQ_API_KEY "your_api_key_here"     # Windows

```

Run the app:
```bash
python app.py

```
Or with Streamlit (if using chatbot.py):

```bash
streamlit run chatbot.py
```
# Screen short DEMO :  
<img width="1722" height="901" alt="chatbot1" src="https://github.com/user-attachments/assets/3e7e8e7a-d841-47bf-a8d8-272a453cc757" />
<img width="1666" height="895" alt="chatbot2" src="https://github.com/user-attachments/assets/8b680f7e-e496-4959-bc9d-1bec15ba4adf" />
<img width="1441" height="874" alt="chatbot3" src="https://github.com/user-attachments/assets/8251ed34-53c0-49d5-8fea-cb3c1c159e15" />


# 🌐 Deployment on Hugging Face Spaces

Upload all project files (app.py, requirements.txt, etc.) to your Hugging Face Space repo.

Go to Settings → Secrets and add:

Key: GROQ_API_KEY

Value: your actual Groq API key

Hugging Face will auto-build and deploy your chatbot.


# 📂 Project Structure

<img width="682" height="202" alt="image" src="https://github.com/user-attachments/assets/4dc6ba17-00d2-48cc-bed4-5006e48edf24" />

# 🖼️ Demo

👉 Try it on Hugging Face Spaces : https://huggingface.co/spaces/Ripon2/Ripon-Chatbot

#🤝 Contributing

Feel free to fork this repo, open issues, and submit pull requests to improve the chatbot.

# 📜 License

This project is licensed under the MIT License.

# ⚡ Built with ❤️ by Ripon Al Mamun : https://github.com/riponalmamun

# Huggingface DEMO: 
<img width="1919" height="910" alt="image" src="https://github.com/user-attachments/assets/2b713873-b4ee-48d8-9a6a-90d1ea4938b6" />

