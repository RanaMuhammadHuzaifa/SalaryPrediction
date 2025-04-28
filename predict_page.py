import streamlit as st
import pandas as pd
import numpy as np
import joblib

def load_model():
    model = joblib.load('salary_predictor_rf.pkl')
    return model

def show_predict_page():
    st.title("Salary Prediction")

    st.write("### Please provide your information:")

    countries = [
        "United States", "India", "Germany", "United Kingdom", "Canada",
        "France", "Brazil", "Spain", "Australia", "Netherlands", "Other"
    ]
    
    education_levels = [
        "Less than a Bachelors", "Bachelor’s degree", "Master’s degree", "Post grad"
    ]

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education_levels)
    experience = st.slider("Years of Professional Experience", 0, 50, 1)

    ok = st.button("Predict Salary")
    if ok:
        # Encoding inputs manually based on training setup
        country_map = {name: idx for idx, name in enumerate(countries)}
        education_map = {name: idx for idx, name in enumerate(education_levels)}

        input_data = np.array([[country_map.get(country, len(countries)-1), 
                                education_map.get(education, 0),
                                experience]])
        
        model = load_model()
        salary = model.predict(input_data)
        st.subheader(f"Estimated Salary: ${salary[0]:,.2f} USD")
