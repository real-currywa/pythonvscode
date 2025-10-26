import streamlit as st
import pandas as pd

try:
   table = pd.read_csv("cw.csv")
except:
   table = pd.DataFrame()
   


col1,col2 = st.columns(2)

with col1:

 first_name = st.text_input("",placeholder="First name")
 st.divider()

with col2:
   
   lastname = st.text_input("",placeholder="Last Name")
   st.divider()

email = st.text_input("",placeholder="Email",type="password")
st.divider()

password = st.text_input("",placeholder="Password",type="password")
st.divider()




co1,co2,co3 = st.columns(3)


with co1:
   st.write("  ")
   
   




with co3:
   st.write("  ")

if st.checkbox("I agree to the terms and conditions"):
  with co2:
     
      if st.button("Sign Me Up",):
         data = pd.DataFrame({"First Name" : [first_name], "Last Name" : [lastname],"Email":[email],"Password":[password]})
         #st.table(data)
         #cvdict = {}
         jointable = pd.concat([table,data],ignore_index=True)
         jointable.to_csv("cw.csv",index=False)
         st.success("Information Saved!")