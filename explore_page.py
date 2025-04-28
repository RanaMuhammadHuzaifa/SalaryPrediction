import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_explore_page():
    st.title("Explore Salary Data")

    df = pd.read_csv('dataset.csv')  # You can rename if you have a different dataset

    st.write("### Based on StackOverflow Developer Survey 2020")

    # Clean for visualization
    df = df[['Country', 'ConvertedCompYearly']]
    df = df.dropna()

    country_salary = df.groupby('Country')['ConvertedCompYearly'].mean().sort_values(ascending=False)

    st.write("#### Average Salary by Country")
    st.bar_chart(country_salary)

    st.write("#### Raw Data Sample")
    st.dataframe(df.sample(10))
