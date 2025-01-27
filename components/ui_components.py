
import streamlit as st

def render_ui():
    st.title("Chat with Your Document")
    uploaded_file = st.file_uploader("Upload your PDF document", type=["pdf"])
    col1, col2 = st.columns(2)
    difficulty = col1.selectbox("Response Difficulty", ["Simple", "Standard", "Advanced"], index=1)
    response_type = col2.selectbox("Response Type", ["Bullet Points", "Short Answer", "Paragraph"], index=1)
    return uploaded_file, difficulty, response_type
