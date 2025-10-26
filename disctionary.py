import streamlit as st

#a dictionary is a data collection used to save data in their categories

#to save colors in a data collection, all you need is a list
colors = ['red', 'blue', 'yellow']

#but if you want to save top 5 players goals in a data collection, you need a dict
# you need a dict to save their goals to their various names

goals = [50, 'ronaldo', 40, 'messi', 30, 'haaland', 20, 'kane']

st.write(goals)

goalscored = {'ronaldo': [50], 'messi': [40], 'haaland': [30], 'kane': [20]}

st.write(goalscored)

st.table(goalscored)