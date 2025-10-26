import streamlit as st

trump = 0
kamala = 0

st.header('VOTING APP US')

age = st.number_input("What is your age? ",value = 1)

col1,col2 = st.columns(2)

with col1:
    if age >= 18:
        vote = st.text_input('Who do you want to vote? Trump or Kamala')
        if vote == 'trump':
            trump += 1
            st.success("You have successfully voted trump")
        elif vote == 'kamala':
            kamala += 1
            st.success("You have successfully voted kamala")
        
    elif age < 18:
         st.warning("You are to young to vote")

with col2:
    st.subheader('Voting in progress')
    st.write('Trumps vote',trump)
    st.write("Kamala's vote",kamala)


