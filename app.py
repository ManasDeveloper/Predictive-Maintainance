import streamlit as st
import pickle


model = pickle.load(open('model.h5','rb'))
scaler = pickle.load(open('scaler.h5','rb'))

st.title("Predictive Machine Maintainance")

air_temperature = st.number_input("Air temperature")
proecess_temperature = st.number_input("Process temperature")
Rotational_speed = st.number_input("Rotational speed")
torque = st.number_input("Torque")

if st.button("Predict"):
    if(air_temperature and proecess_temperature and Rotational_speed and torque):
        prediction = model.predict(scaler.transform([[air_temperature,proecess_temperature,Rotational_speed,torque]]))
        
        if(prediction[0] == 0):
            st.write("No Failure in the machine")
        else:
            st.write("Failure in the machine")
    else:
        st.write("Please provide all parameters")