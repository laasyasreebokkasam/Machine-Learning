from model import model, scaler
import streamlit as st
import pandas as pd
import numpy as np
columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

st.title("Heart Disease Diagnostic App")
st.text("Find out whether you have heart disease")
st.subheader("Fill out below details")
age = st.number_input("Person Age")
sex = st.radio("Sex",["male","female"])
sex = 1 if sex == "Male" else 0
cp = st.selectbox("Chest Pain Type", options=[0, 1, 2, 3])
trestbps = st.slider("Resting Blood Pressure", min_value=80, max_value=220, value=120, step=1)
chol = st.slider("Resting Blood Pressure", min_value=126, max_value=564, value=235, step=1)
fbs = st.radio("Fasting Blood Sugar",["120 mg/sl and under","Over 120 mg/sl"])
fbs = 1 if fbs == "Over 120 mg/sl" else 0
restecg = st.selectbox("Resting Electrocardiographic Results", options=[0, 1, 2, 3])
thalach = st.number_input("Maximum Heart Rate", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina: 0=No, 1=Yes", [0, 1])
oldpeak = st.number_input("ST Depression", 0.0, 10.0, 1.0, step=0.1)
slope = st.selectbox("Slope: 0, 1, 2", [0, 1, 2])
ca = st.selectbox("Major Vessels: 0-4", [0, 1, 2, 3, 4])
thal = st.selectbox("Thal: 0, 1, 2, 3", [0, 1, 2, 3])

if st.button("Diagnose"):
    df = pd.DataFrame({
        'age': [age], 
        'sex': [sex], 
        'cp': [cp], 
        'trestbps': [trestbps], 
        'chol': [chol], 
        'fbs': [fbs], 
        'restecg': [restecg], 
        'thalach': [thalach], 
        'exang': [exang], 
        'oldpeak': [oldpeak], 
        'slope': [slope], 
        'ca': [ca], 
        'thal': [thal], 
    })

    scaled_data = scaler.transform(df)
    prediction = model.predict(scaled_data)[0]

    if prediction == 1:
        st.error("You have heart disease")
    else:
        st.success("You do not have heart disease")