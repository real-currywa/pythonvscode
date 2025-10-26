import streamlit as st
import pandas as pd #this is used to read and write CSV on python
import plotly.express as px


#STEP1 FIND FILE OR CREATE TABLE
try: #iwant to do this
    databasefile = pd.read_csv('studentsdb.csv')
except: #but if any error,DO NOT Crash, come and do the
    databasefile = pd.DataFrame() #create a empty table


menu = st.sidebar.selectbox('Menu',['Input Scores','View Results'])


if menu == 'View Results':
    st.table(databasefile)

    subjects = ['P.H.E','Math','English','Art','French','Science','Religion','Social Studies']
    subjectave= databasefile[subjects].mean().reset_index()
    #st.table(subjectave)

    choosechart = st.radio('Choose Chart',['Bar Chart','Pie Chart'])

    if choosechart == 'Bar Chart':
        barchart = px.bar(subjectave,x='index',y=0,labels={'index':'Subject','0':'Average'})
        st.plotly_chart(barchart)


    elif choosechart == 'Pie Chart':
        piechart = px.pie(subjectave,names='index',values=0,labels={'index':'Subject','0':'Average'})
        st.plotly_chart(piechart)

if menu =='Input Scores':
    st.header('Student Report Card')


    name = st.text_input('Enter Student Name')

    col1,col2 = st.columns(2)

    with col1:
        Phe = st.number_input('Enter P.H.E score',0,100)
        Math = st.number_input('Enter Math Score',0,100)
        English = st.number_input('Enter English Score',0,100)
        Art = st.number_input('Enter Art Score',0,100)

    with col2:
        French = st.number_input('Enter French Score',0,100)
        Science = st.number_input('Enter Science Score',0,100)
        Religion = st.number_input('Enter Religion Score',0,100)
        Social_Studies = st.number_input('Enter Social Studies Score',0,100)

    totalscore = Phe+Math+English+Art+French+Science+Religion+Social_Studies
    Average = totalscore/8



    if st.button(f'Check {name} Grade'):
        if name:
            st.write(f'{name} total score is {totalscore}')
            st.write(f'{name} Average is {Average}')

            if Average >= 90:
                st.success('You got an A')
            elif Average >= 80 and Average < 90:
                st.success('You got a B')
            elif  Average >= 60 and Average < 80:
                st.success(f'{name} got a C')
            elif Average >= 50 and Average < 60:
                st.warning(f'{name} got a D')
            elif Average >= 40 and Average < 50:
                st.warning(f'{name} got a E')
            else:
                st.error(f"{name}got a F")

            #STEP2 STORE ALL DATA IN DICT
            data = {'Name' : [name],"P.H.E" : [Phe], "Math" : [Math], "English" : [English], "Art" : [Art], "French" : [French], "Science" : [Science], "Religion" : [Religion], "Social Studies" : [Social_Studies], "Average" : [Average]}
            st.table(data)


            #STEP3 CONVERT DICT TO TABLE
            studenttable = pd.DataFrame(data) #make a table using the diction

            #STEP4 SAVE
            studenttable.to_csv("studentsdb.csv",index=False)
            st.success("Information Saved!")

        else:
            st.error('Enter student name please')