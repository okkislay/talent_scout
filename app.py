import streamlit as st
from utils import get_ai_response
from prompts import SYSTEM_PROMPT

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="TalentScout - AI Recruiter",
    page_icon="🤖",
    layout="centered"
)

# --- HEADER ---
st.title("🤖 TalentScout Hiring Assistant")
st.markdown("Welcome! I am here to help screen your application for technical roles.")
st.markdown("---")

# --- SESSION STATE INITIALIZATION ---
# This preserves the chat history when the app reruns (Streamlit behavior)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "assistant", "content": "Hello! I am TalentScout. To get started, could you please tell me your full name?"}
    ]

# --- DISPLAY CHAT HISTORY ---
# We skip the first message (index 0) because it is the hidden system prompt
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- USER INPUT HANDLING ---
if prompt := st.chat_input("Type your answer here..."):
    # 1. Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 2. Append user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 3. Generate AI Response
    with st.chat_message("assistant"):
        # Create a placeholder to stream the response
        response_placeholder = st.empty()
        full_response = ""
        
        # Call the API
        stream = get_ai_response(st.session_state.messages)
        
        # Stream the chunks
        if isinstance(stream, str): # Error handling
            response_placeholder.markdown(stream)
            full_response = stream
        else:
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    content = chunk.choices[0].delta.content
                    full_response += content
                    response_placeholder.markdown(full_response + "▌") # Typing cursor effect
            
            response_placeholder.markdown(full_response)

    # 4. Append AI response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# --- SIDEBAR & SUBMISSION ---
with st.sidebar:
    st.header("🏁 Finish Interview")
    st.write("Click below to save your responses for the recruiter.")
    
    # Import the save function (ensure you added it to utils.py)
    from utils import save_candidate_data
    
    if st.button("End & Submit Interview"):
        if len(st.session_state.messages) > 2:
            msg = save_candidate_data(st.session_state.messages)
            st.success("✅ Interview Submitted!")
            st.info(f"Recruiter Note: {msg}")
        else:
            st.warning("Please start the conversation first.")

    st.markdown("---")
    st.header("Debug / Info")
    if st.button("Reset Conversation"):
        st.session_state.messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "assistant", "content": "Hello! I am TalentScout. To get started, could you please tell me your full name?"}
        ]
        st.rerun()