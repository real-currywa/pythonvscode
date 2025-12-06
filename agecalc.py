import streamlit as st

st.header('Korewa,s Age Calculator')

name = st.text_input('Enter Your Name')

dob = st.number_input('Enter Your DOB',0,2025)

yr = st.number_input('Enter the current year',1)

age = yr-dob

if st.button('Check your age'):
    if name:
        if dob:
            if yr:
                st.success(f'Your age is {age}')
else:
    st.error('All fields must be filled')

