import streamlit as st
from transformers import pipeline

# Load AI Model
chatbot = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

# Streamlit UI
st.title("AI Personal Chatbot ")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You: ")

if st.button("Send"):
    if user_input:
        st.session_state.history.append(user_input)
        response = chatbot(user_input, max_length=100, truncation=True)
        bot_response = response[0]["generated_text"]
        st.session_state.history.append(bot_response)
        st.write(f": {bot_response}")

st.write("### Chat History")
for i in range(0, len(st.session_state.history), 2):
    st.write(f"**Bot:** {st.session_state.history[i]}")
    if i+1 < len(st.session_state.history):
        st.write(f"**You:** {st.session_state.history[i+1]}")
