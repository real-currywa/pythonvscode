import streamlit as st

name = st.text_input('What is you name?')

matches = 10

goals_per_matches = 2

yellow_cards = 3

total = matches*goals_per_matches

diff = total-yellow_cards

avrg = total/matches
if name:
    if st.button('View stats'):
        st.write(f'{name} has a total of {total} goals,{diff} goal difference and {avrg} average goals per match')