# messages.py

# This module manages chat messages for a session

def init_history(session_state):
    """Initialize chat history in Streamlit session_state"""
    if "history" not in session_state:
        session_state.history = []

def add_message(session_state, role, content):
    """
    Add a message to the chat history.
    role: "user" or "bot"
    content: string
    """
    session_state.history.append({"role": role, "content": content})

def get_history(session_state):
    """Return the full chat history"""
    return session_state.history

def clear_history(session_state):
    """Clear all messages"""
    session_state.history = []
