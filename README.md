# TalentScout - Intelligent Hiring Assistant 🤖

**TalentScout** is an AI-powered recruitment chatbot designed to automate the initial screening of technical candidates. Built with **Streamlit** and **Groq (Llama-3.1)**, it conducts natural language interviews, gathers candidate details, generates dynamic technical questions based on the user's tech stack, and stores responses for recruiter review.

---

## 📋 Project Overview
The goal of this project is to streamline the hiring process by:
1.  **Gathering Information:** Collecting candidate details (Name, Email, Exp, Stack).
2.  **Dynamic Screening:** Generating context-aware technical questions based on the declared tech stack (e.g., Python, AWS, React).
3.  **Data Persistence:** Saving interview transcripts to a local database for review.

---

## 🛠️ Technical Specifications
* **Frontend:** [Streamlit](https://streamlit.io/) (Python-based UI).
* **LLM Engine:** [Groq API](https://groq.com/) using `llama-3.1-8b-instant` for ultra-low latency responses.
* **Architecture:** Finite State Machine (FSM) via System Prompts to manage conversation flow.
* **Data Handling:** Local JSON storage (`candidates_database.json`) for simulated database persistence.
* **Security:** Environment variable management via `python-dotenv` to protect API keys.

---

## 🚀 Installation & Setup

Follow these steps to set up the project locally.

### Prerequisites
* Python 3.8 or higher
* A free API Key from [Groq Console](https://console.groq.com/)

### 1. Clone the Repository
```bash
git clone <your-repo-link-here>
cd talentscout-bot

#Create a Virtual Environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

#Install Dependencies
pip install -r requirements.txt

#Configure API Key
#Create a .env file in the root directory and add your Groq API key:

GROQ_API_KEY=gsk_your_actual_key_here

#Run the Application:
streamlit run app.py