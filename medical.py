import streamlit as st
import pandas as pd
import plotly.express as px

try:
    dbf =  pd.read_csv('medical.csv')
except:
    dbf = pd.DataFrame()

st.set_page_config(layout='wide')
st.subheader(' :green[Medical Quiz Awareness Test]')

points = 0

menu = st.sidebar.selectbox('Menu',['Write Exam','View Results'])


if menu == 'Write Exam':
    name = st.text_input('What is your name')
    col1,col2,col3,col4= st.columns(4)

    with col1:
        st.info('Question 1')
        q1 = st.radio('What is the main job of your heart?',['Choose','A) Pumping blood', 'B) Digesting food' ,'C) Storing energy','D) Breathing air'])

        st.info('Question 5')
        q5 = st.radio('What does a doctor do?',['Choose','A) Fix cars','B) Help people stay healthy','C) Teach math,','D) None of the above'])

        st.info('Question 9')
        q9 = st.radio('Why is it important to eat breakfast?',['Choose','A) It’s the best meal of the day','B) It gives you energy for school','C) You can skip it','D) None of the above'])

        st.info('Question 13')
        q13 = st.radio('What is a common symptom of a cold?',['Choose','A) Runny nose','B) Happy thoughts','C) Dancing','D) None of the above'])

        st.info('Question 17')
        q17 = st.radio('What should you do if you feel dizzy?',['Choose','A) Keep running','B) Sit down and tell an adult','C) Eat a lot of candy','D) None of the above'])


    with col2:
        st.info('Question 2')
        q2 = st.radio('What do vaccines help protect you from?',['Choose','A) Common cold','B) Diseases like measles and flu','C) Cuts and bruises','D) None of the above'])

        st.info('Question 6')
        q6 = st.radio('What is a healthy snack?',['Choose','A) Candy','B) Fruits and vegetable','C) Chips','D) Soda'])

        st.info('Question 10')
        q10 = st.radio('What is one way to keep your bones strong?',['Choose','A) Eating junk food','B) Drinking milk or eating dairy','C) Avoiding exercise','D) None of the above'])

        st.info('Question 14')
        q14 = st.radio('Why should you cover your mouth when you cough?',['Choose','A) To look funny',
    'B) To prevent spreading germs',
    'C) To make a sound',
    'D) None of the above'])
        
        st.info('Question 18')
        q18 = st.radio('What is the main function of your lungs?',['Choose','A) To pump blood',
    'B) To help you breathe',
    'C) To digest food',
    'D) None of the above'])


    with col3:
        st.info('Question 3')
        q3 = st.radio('Why is it important to wash your hands?',['Choose','A) To smell nice',
    'B) To prevent getting sick',
    'C) To look clean',
    'D) None of the above'])

        st.info('Question 7')
        q7 = st.radio('What does it mean to be allergic to something?',['Choose','A) You like it a lot',
    'B) Your body reacts badly to it',
    "C) You can't eat it",
    'D) None of the above'
    ])

        st.info('Question 11')
        q11 = st.radio('What is the purpose of first aid?',['Choose','A) To help with homework',
    'B) To give immediate care in emergencies',
    'C) To make food',
    'D) None of the above'
    ])

        st.info('Question 15')
        q15 = st.radio('What is a safe way to exercise?',['Choose','A) Jumping on the bed',
    'B) Playing sports or riding a bike',
    'C) Sitting all day',
    'D) None of the above'])

        st.info('Question 19')
        q19 = st.radio('What can help you stay healthy during cold and flu season?',['Choose','A) Washing hands frequently',
    'B) Eating more sweets',
    'C) Skipping sleep',
    'D) None of the above'])


    with col4:
        st.info('Question 4')
        q4 = st.radio('What should you do if you have a fever?',['Choose','A) Go play outside',
    'B) Tell an adult and rest',
    'C) Eat a lot of candy',
    'D) Stay up late'])

        st.info('Question 8')
        q8 = st.radio('What should you do if you get a cut?',['Choose','A) Ignore it',
    'B) Wash it and put a bandage on it',
    'C) Show it to your friends',
    'D) None of the above'
    ])

        st.info('Question 12')
        q12 = st.radio('What can help you breathe better when you’re sick?',['Choose','A) Eating ice cream',
    'B) Drinking warm fluids',
    'C) Running around',
    'D) None of the above'])

        st.info('Question 16')
        q16 = st.radio('What does a dentist check?',['Choose','A) Your eyes',
    'B) Your teeth',
    'C) Your hair',
    'D) None of the above'])

        st.info('Question 20')
        q20 = st.radio('What does it mean if someone has a headache?',['Choose','A) They are happy',
    'B) They might need rest or water',
    'C) They want to play',
    'D) None of the above'])


    if st.button('Submit Your Quiz'):
        if name == None:
            st.error('Enter your name please')
        if q1 == 'Choose':
            st.error('Question 1 not yet answered')
        elif q1 == "A) Pumping blood":
            points +=1
        if q2 == 'Choose':
            st.error('Question 2 not yet answered')
        elif q2 == "B) Diseases like measles and flu":
            points +=1
        if q3 == 'Choose':
            st.error('Question 3 not yet answered')
        elif q3 == "B) To prevent getting sick":
            points +=1    
        if q4 == 'Choose':
            st.error('Question 4 not yet answered')
        elif q4 == "B) Tell an adult and rest":
            points +=1    
        if q5 == 'Choose':
            st.error('Question 5 not yet answered')
        elif q5 == "B) Help people stay healthy":
            points +=1
        if q6 == 'Choose':
            st.error('Question 6 not yet answered')
        elif q6 == "B) Fruits and vegetable":
            points +=1
        if q7 == 'Choose':
            st.error('Question 7 not yet answered')
        elif q7 == "B) Your body reacts badly to it":
            points +=1    
        if q8 == 'Choose':
            st.error('Question 8 not yet answered')
        elif q8 == "B) Wash it and put a bandage on it":
            points +=1    
        if q9 == 'Choose':
            st.error('Question 9 not yet answered')
        elif q9 == "B) It gives you energy for school":
            points +=1
        if q10 == 'Choose':
            st.error('Question 10 not yet answered')
        elif q10 == "B) Drinking milk or eating dairy":
            points +=1
        if q11 == 'Choose':
            st.error('Question 11 not yet answered')
        elif q11 == "B) To give immediate care in emergencies":
            points +=1    
        if q12 == 'Choose':
            st.error('Question 12 not yet answered')
        elif q12 == "B) Drinking warm fluids:":
            points +=1    
        if q13 == 'Choose':
            st.error('Question 13 not yet answered')
        elif q13 == "A) Runny nose":
            points +=1
        if q14 == 'Choose':
            st.error('Question 14 not yet answered')
        elif q14 == "B) To prevent spreading germs":
            points +=1
        if q15 == 'Choose':
            st.error('Question 15 not yet answered')
        elif q15 == "B) Playing sports or riding a bike":
            points +=1    
        if q16 == 'Choose':
            st.error('Question 16 not yet answered')
        elif q16 == "B) Your teeth":
            points +=1    
        if q17 == 'Choose':
            st.error('Question 17 not yet answered')
        elif q17 == "B) Sit down and tell an adult":
            points +=1
        if q18 == 'Choose':
            st.error('Question 18 not yet answered')
        elif q18 == "B) To help you breathe":
            points +=1
        if q19 == 'Choose':
            st.error('Question 19 not yet answered')
        elif q19 == "A) Washing hands frequently":
            points +=1    
        if q20 == 'Choose':
            st.error('Question 20 not yet answered')
        elif q20 == "B) They might need rest or water":
            points +=1    

        #grade system
        if points <=9:
            st.error('You have failed this test.')
        elif points == 10:
            st.warning('You barely passed this test')
        elif points > 10 and points <= 15:
            st.success('You did well!!!')
        elif points >15 and points <=20:
            st.success('Good Job!! You scored in the top 20%')
        if points:
            st.success(f'You scored aproximatelly {points} points.')


        #saving
        data = {'Name' : [name],'Points' : [points]}
        st.table(data)

        table = pd.DataFrame(data)
        jointable = pd.concat([dbf,table],ignore_index=True)
        jointable.to_csv('medical.csv',index=False)
        st.success("Information Saved!")
        

if menu == 'View Results':
    choosechart = st.radio('Choose Chart',['Bar Chart','Pie Chart'])
    if choosechart == 'Bar Chart':
        barchart = px.bar(dbf,x='Name',y='Points')
        st.plotly_chart(barchart)

    elif choosechart == 'Pie Chart':
        piechart = px.pie(dbf,names='Name',values='Points')
        st.plotly_chart(piechart)


#hello
