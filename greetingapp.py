
import streamlit as st

st.title("👋 User Greeting App")

name = st.text_input("Enter your name:")

if name:
    st.success(f"Hello, {name}! Welcome to Streamlit! 🎉")
else:
    st.warning("⚠️ Please enter your name to proceed.")
