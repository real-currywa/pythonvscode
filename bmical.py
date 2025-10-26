import streamlit as st

st.set_page_config(layout='wide')
menu = st.sidebar.selectbox('BMI Menu', ['Children BMI' ,'Adult BMI'])

if menu == 'Children BMI':
    st.subheader('Height')
    metre,inch= st.columns(2)
    with metre:
        metres = st.number_input("Metres")
    with inch:
        inch = st.number_input('Inches')

    st.divider()
    st.subheader("Weight")
    KG,Pound = st.columns(2)
    with KG:
        kg = st.number_input('Kilograms')
    with Pound:
        Pound = st.number_input('Pounds')
    st.divider()

    if st.button("Submit"):
        if(metre,inch,kg,Pound):
            height = metres * metres
            bmi = kg / metres
        if bmi < 18.5:
            st.success("Underweight")
        elif bmi >= 18.5 and bmi < 24.9:
                st.success("Normal weight")
        elif bmi >+ 25 and bmi < 29.9:
                st.sucess("Overweight")
        else:
                st.warning("Obesity")




            
if menu == 'Adult BMI':
    st.subheader('Height')
    metre,inch= st.columns(2)
    with metre:
        metres = st.number_input("Metres")
    with inch:
        inch = st.number_input('Inches')

    st.divider()
    st.subheader("Weight")
    KG,Pound = st.columns(2)
    with KG:
        kg = st.number_input('Kilograms')
    with Pound:
        Pound = st.number_input('Pounds')
    st.divider()
    if st.button("Submit"):
        if(metre,inch,kg,Pound):
            height = metres * metres
            bmi = kg / metres
        if bmi < 30.0:
            st.success("Underweight")
        elif bmi >= 30.1 and bmi < 70:
                st.success("Normal weight")
        elif bmi >= 70 and bmi < 80:
                st.success("Overweight")
        else:
                st.warning("Obesity")

