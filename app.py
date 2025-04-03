import streamlit as st
from transformers import pipeline, Conversation

# Load AI Model
chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

# Streamlit UI
st.title("AI Personal Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You: ")

if st.button("Send"):
    if user_input:
        st.session_state.history.append(user_input)
        conversation = Conversation(" ".join(st.session_state.history))
        response = chatbot(conversation)
        st.session_state.history.append(response.generated_responses[-1])
        st.write(f"🤖: {response.generated_responses[-1]}")

st.write("### Chat History")
for i in range(0, len(st.session_state.history), 2):
    st.write(f"**You:** {st.session_state.history[i]}")
    if i+1 < len(st.session_state.history):
        st.write(f"**Bot:** {st.session_state.history[i+1]}")
