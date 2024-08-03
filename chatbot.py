import streamlit as st
import datetime

# Initialize session state
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []

# Function to handle sending a message
def send_message():
    if st.session_state.user_message:
        st.session_state.conversation.append({
            "sender": "User", 
            "message": st.session_state.user_message, 
            "timestamp": datetime.datetime.now()
        })
        st.session_state.user_message = ""

        # Simulated bot response
        st.session_state.conversation.append({
            "sender": "Bot", 
            "message": "This is a response from DoctorAI.", 
            "timestamp": datetime.datetime.now()
        })

# Streamlit layout
st.set_page_config(page_title="DoctorAI Chatbot", page_icon="🤖", layout="centered")
st.title("DoctorAI Chatbot")

# Settings
with st.sidebar:
    st.header("Settings")
    st.text_input("Your Name", key="user_name")
    st.selectbox("Language", ["English", "Spanish", "French"], key="language")
    st.slider("Response Speed", 1, 5, key="response_speed")

# Conversation history
st.subheader("Conversation")
scrollable_container = st.container()
with scrollable_container:
    for entry in st.session_state['conversation']:
        if entry["sender"] == "User":
            st.markdown(f"**You ({entry['timestamp'].strftime('%Y-%m-%d %H:%M:%S')})**: {entry['message']}")
        else:
            st.markdown(f"**DoctorAI ({entry['timestamp'].strftime('%Y-%m-%d %H:%M:%S')})**: {entry['message']}")

# Message input and buttons
st.text_input("Type your message here...", key="user_message", on_change=send_message)
st.button("Send", on_click=send_message)
st.file_uploader("Attach a file", type=['jpg', 'jpeg', 'png', 'pdf'])
