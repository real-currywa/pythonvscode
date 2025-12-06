import streamlit as st

bizlogo = 'bizlogo.png'

img1,img2 = st.columns(2)

with img1:
    st.image(bizlogo,width=150)
    
with img2:
    st.subheader('INVOICE')

