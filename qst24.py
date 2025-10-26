import streamlit as st

circuit_name = st.text_input("What is the circuit name?")

voltage = st.number_input("What is the voltage of the circuit?")

resistance = st.number_input("What is the resistance of the circuit?")

current =  voltage / resistance

if current > 15:
    st.warning(f"Warning, {circuit_name}! Your current is {current} amps, which exceeds safe operating limits!")

elif 10 <= current <=15:
    st.warning(f"Caution, {circuit_name}! Your current is {current} amps. You're nearing the limit. Monitor closely!")

elif 0 < current < 10:
    st.success(f"Safe, {circuit_name}! Your current is {current} amps. The circuit is operating within limits.")

else:
    st.warning(f"Error: Resistance cannot be zero. Please check the input values for {circuit_name}.")