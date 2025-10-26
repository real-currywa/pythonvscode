import streamlit as st

st.title("TEMPERATUR CONVERTER")

temp_celcius = st.number_input("Enter temparature in celcius",0.0)
temp_fahrenheit = (temp_celcius * 9/5) + 32

st.subheader(f"Converted Temperature: {temp_fahrenheit}°F")