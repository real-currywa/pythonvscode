import streamlit as st

name = st.text_input("What is your name?")
age = st.number_input("How old are you?")
gender = st.radio("Choose your gender",["Male","Female"])
volunteerunit = st.selectbox("Choose your unit:",["Cleaning","Greeting","Music Team","Footballer"])

if age >= 0 and age < 12:
    ageGroup = ('Child')
elif age >= 12 and age < 19:
    ageGroup = ('Teen')
elif age >= 19 and age < 35:
    ageGroup = ("Youth")
elif age >= 35 and age < 64:
    ageGroup = ("Adult")
else:
    ageGroup = ("Unc💀💀")
if st.button("Enter your data"):
    data = {"name" : [name], 'age' : [age], 'gender': [gender], 'volunteerunit' : [volunteerunit] }
    st.table(data)