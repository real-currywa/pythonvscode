import streamlit as st

#to use a variable to store more than one data we need data collection

#examples of data collections
#-List -Tuple -Dictionary -Set

#List
fruits = ['Apple','Banana','Orange','Pawpaw']

# st.write(fruits[3])
#list is known by the square bracket
#items in list are arranged in order of position starting from position 0 (1st Item)


#1.Selectbox
#This is used to show the user multiple options in a box, which they can select one from

bestgame = st.selectbox('Choose your best game',['Minecraft','Roblox','FC25','NFS','NFL'])

st.write('Your best game is',bestgame)



#2.Radio button
#This is also used to show users multiple options but not in a box. Very useful for short and few options
gender = st.radio('Select your gender',['Male','Female'],horizontal=True)

st.write('You are a',gender)


#3.Menu or Sidebar
#This is use to navigate from one page to another
menu = st.sidebar.selectbox('Choose your Menu',['Page1','Page2'])
