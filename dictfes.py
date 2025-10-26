import streamlit as st

name = st.text_input("What is your name? ")
kids1 = st.number_input("How many kids do you have for elementary school? ",0)
kids2 = st.number_input("How many kids do you have for college? ",0)


el_fee = kids1 * 5000
col_fee = kids2 * 15000

tot_fee = el_fee + col_fee

if st.button("Submit"):
    data = {'Name' : [name], 'Elementary children' : [kids1], 'Elementary fee' : [el_fee] ,'College children' : [kids2], 'College fee' : [col_fee], 'Total fee' : [tot_fee]}
    st.table(data)

