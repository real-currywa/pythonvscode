import streamlit as st

num1 = st.number_input("Enter a number")
num2 = st.number_input("Enter a second number")

operation = st.selectbox("Enter an operation", ["Addition(+)" ,'Multiplication(*)'])


if operation == 'Addition(+)':
    result = num1+num2
    

elif operation == 'Multiplication(*)':
    result = num1*num2
    

st.table(result)