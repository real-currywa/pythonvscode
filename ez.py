import streamlit as st
name = st.text_input('What is your name?')
time = st.number_input('How much time did it take for you to complete the race?',0)


if st.button('submit'):
    if time < 30:
        print(f'Well done {name} you ran very fast')
    else:
        print(f'That was too slow {name} keep training and run faster.')