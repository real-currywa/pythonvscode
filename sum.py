import streamlit as st
import pandas as pd
import plotly.express as px

try:
    db = pd.read_csv('sum.csv')
except:
    db = pd.DataFrame()

st.text_input("Enter the students name.")
col1,col2 = st.columns(2)
with col1:
    python = st.number_input('Enter the Python score.',0,100)
    web = st.number_input('Enter the Web-Development score.',0,100)
with col2:
    robotic = st.number_input('Enter the Robotics score.',0,100)
    problem = st.number_input('Enter the Problem-Solving score.',0,100)


total = python+web+robotic+problem
average = total/4




if st.button('Submit Students Score'):

    st.write(f'Your Total Score is {total}/400 ')
    st.write(f'Your average is {average}.')
    if average >= 90:
        st.success('You earned a Platinum Badge🏅.')
    elif average >= 80 and average < 90:
        st.success('You earned a Gold Badge🥇.')
    elif average >= 70 and average < 80:
        st.success('You earned a Silver Badge🥈.')
    elif average >= 60 and average < 70:
        st.write('You earned a Bronze Badge🥉.')
    else:
        st.warning('You got a Badge for being a Participant〽️.')

    st.balloons()

    data = {'Python' : [python],'Web-Development' : [web],'Robotics' : [robotic],'Problem-Solving' : [problem]}
    st.table(data)

    stu = pd.DataFrame(data)
    join = pd.concat([db,stu],ignore_index=True)
    join.to_csv("sum.csv",index=False )




    
        