import streamlit as st
name = st.text_input("What is your name? ")
venue_cost = st.number_input("What is the venue rental? ",0)
catering_cost = st.number_input("What is the catering cost? ",0)
decoration_cost = st.number_input("What is the decoration cost? ",0)
photography_cost = st.number_input("What is the photography cost? ",0)
music_cost = st.number_input("What is the music cost? ",0)
total_cost = venue_cost+catering_cost+decoration_cost+photography_cost+music_cost
st.write(f"Hi {name}! You spent a total of ${total_cost} on your wedding reception preperations.")