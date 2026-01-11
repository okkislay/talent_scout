import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq Client
# Ensure you have GROQ_API_KEY in your .env file or Streamlit Secrets
try:
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
except Exception as e:
    client = None

def get_ai_response(messages):
    """
    Sends the conversation history to the Groq API and retrieves the response.
    Using Llama-3 for high speed and accuracy.
    """
    if not client:
        return "Error: API Key not found. Please configure your settings."

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Free, fast model ideal for chat
            messages=messages,
            temperature=0.6,         # Slightly lower temperature for more focused Q&A
            max_tokens=1024,
            top_p=1,
            stream=True,             # Enable streaming for real-time feel
            stop=None,
        )
        return completion
    except Exception as e:
        return f"Error communicating with AI: {str(e)}"

import json
from datetime import datetime

def save_candidate_data(messages):
    """
    Saves the interview transcript and metadata to a local JSON file.
    This acts as our 'database'.
    """
    # 1. Extract basic info (Simple extraction for demo purposes)
    # In a real app, you'd use the LLM to extract this structurally.
    # Here we just save the full conversation.
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Structure the record
    record = {
        "timestamp": timestamp,
        "conversation_history": [
            {"role": m["role"], "content": m["content"]} 
            for m in messages if m["role"] != "system"
        ]
    }

    # 2. Append to a local file (database.json)
    file_name = "candidates_database.json"
    
    # Read existing data
    try:
        with open(file_name, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    # Add new record
    data.append(record)

    # Save back to file
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)
        
    return f"Data successfully saved to {file_name}"