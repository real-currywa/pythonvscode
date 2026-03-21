import streamlit as st
menu = st.sidebar.selectbox('Share feedback',['Greetings','Feedback'])
if menu == 'Greetings':
    st.title("👋 User Greeting App")

    name = st.text_input("Enter your name:")

    if name:
        st.success(f"Hello, {name}! Welcome back to Streamlit! 🎉")
if menu == 'Feedback':
    if st.text_input('Please give your feedback on why you stopped using our app'):
        st.success("Thank you for your feedback")