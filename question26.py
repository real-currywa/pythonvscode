import streamlit as st

car_name = st.text_input('What is your cars name? ')

distance = st.number_input('What is the distance travelled in the car? ')

time = st.number_input("What is the time taken? ")


speed = distance/time

if speed > 30:
    st.error(f"Warning, {car_name}! Your speed is {speed} m/s, which is too fast!")

elif 20 <= speed <= 30:
    st.warning(f"Caution, {car_name}! Your speed is {speed} m/s. Drive carefully!")

elif speed < 20:
    st.success(f"Safe, {car_name}! Your speed is {speed} m/s. You are driving safely.")

else:
    st.error(f"Error: Time cannot be zero. Please check the input values for {car_name}.")
