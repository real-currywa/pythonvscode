import streamlit as st

st.write("SCHOOL REGISTERATION APP")
st.write("Welcome to Zenith Schools")
st.divider()
MENU = st.sidebar.selectbox("Menu", ["Home", "Registeration", "About us", "Contact us"])
if MENU == "Registeration":
    st.write("BIO DATA")
    st.divider()
    fullname = st.text_input("Enter your full name", placeholder="Fullname")
    Parentname = st.text_input("Enter your Parents name", placeholder="Parent name")
    Age = st.number_input("Enter your Age", min_value=5, max_value=14)
    Gender = st.radio("Select Gender", ["Male", "Female"])
    Address = st.text_input("Enter your Address", placeholder="Address")

    if st.button("submit", type = 'primary'):
        if  Age >= 5 and Age <= 14:
            st.write(fullname, "You are Eligible for registeration")
        st.write("Call our school secretary for more enquires")

if MENU =="Contact us":
    st.write("Contact us")
    st.write("For more info call +2349845678445")
    st.write("Email us at Zenith38@gmail.com")

if MENU == "Home":
    st.write("Welcome to Zenith Schools")
    st.write("We are glad to have to have you here")
    st.write("We are the best school in the world")
    st.write("We have the best teachers in the world")
    st.write("We are located at 1234 Zenith Street, Lagos, Nigeria")
    st.image("https://upload.wikimedia.org/wikipedia/commons/8/8e/Staples_High_School%2C_Westport%2C_CT.jpg", width = 800)