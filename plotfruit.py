import streamlit as st
import pandas as pd
import plotly.express as px


try: #iwant to do this
    databasefile = pd.read_csv('sales.csv')
except: #but if any error,DO NOT Crash, come and do the
    databasefile = pd.DataFrame() #create a empty table

menu = st.sidebar.selectbox('Menu',['Select','View Results'])
if menu == 'Select':
    st.header('Market Place')
    st.image('https://media.istockphoto.com/id/995518546/photo/assortment-of-colorful-ripe-tropical-fruits-top-view.jpg?s=612x612&w=0&k=20&c=bz2zksjSPikOYm9I-mG-f8SAQWVpFsR4M_u4K9soLQ0=')


    sold = st.selectbox('Choose the fruits that were sold:',['Grape','Pineapple','Apple','Banana','Orange','Lemon','Strawberries','Blueberries','Pear','Watermelon'])

    quantity = st.number_input(f"What is the number of {sold} sold ",0)
    if st.button('Check'):
        data = {'Fruit' : [sold], 'Quantity Sold' : [quantity]}
        st.table(data)

        table = pd.DataFrame(data)
        jointable = pd.concat([databasefile,table],ignore_index=True)
        jointable.to_csv("sales.csv",index=False)
        st.success("Information Saved!")


if menu == 'View Results':
    with st.expander('Open Sales Table'):
        st.table(databasefile)

    choosechart = st.radio('Choose Chart',['Bar Chart','Pie Chart'])

    if choosechart == 'Bar Chart':
        barchart = px.bar(databasefile,x='Fruit',y='Quantity Sold')
        st.plotly_chart(barchart)



    elif choosechart == 'Pie Chart':
        piechart = px.pie(databasefile,names='Fruit',values='Quantity Sold')
        st.plotly_chart(piechart)