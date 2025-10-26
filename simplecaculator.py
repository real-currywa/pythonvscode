import streamlit as st

name = st.text_input("What is your name? ")

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")

operation = st.selectbox("Enter an operation", ["Addition(+)" ,'Subtraction(-)' ,'Multiplication(*)' ,'Division(/)'])

if operation == 'Addition(+)':
    result = num1+num2
    st.success(result)
elif operation == 'Subtraction(-)':
    result = num1-num2
    st.success(result)
elif operation == 'Multiplication(*)':
    result = num1*num2
    st.success(result)
elif operation == 'Division(/)':
    result = num1/num2
    st.success(result)