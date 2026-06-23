import streamlit as st
from components.styles import hero
from components.data_loader import load_data


def show():
    hero('HR and Behavioral Questions', 'Practice communication, leadership, teamwork, and confidence-based interview questions.', 'HR Module')
    df = load_data()
    hr = df[df['category'].str.lower().isin(['hr', 'behavioral']) | (df['type'].str.lower() == 'behavioral')]
    search = st.text_input('Search HR questions')
    data = hr.copy()
    if search:
        data = data[data['question'].str.contains(search, case=False, na=False)]
    st.dataframe(data[['question','ideal_answer','difficulty','keywords']], use_container_width=True, hide_index=True)
