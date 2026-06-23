import streamlit as st
from components.styles import hero
from components.data_loader import load_data


def show():
    hero('Technical Question Bank', 'Browse and filter technical interview questions by role and difficulty.', 'Technical Module')
    df = load_data()
    tech = df[df['category'].str.lower() == 'technical']
    c1, c2 = st.columns(2)
    with c1: role = st.selectbox('Role / Skill Area', ['All'] + sorted(tech['role'].unique().tolist()))
    with c2: difficulty = st.selectbox('Difficulty', ['All'] + sorted(tech['difficulty'].unique().tolist()))
    data = tech.copy()
    if role != 'All': data = data[data['role'] == role]
    if difficulty != 'All': data = data[data['difficulty'] == difficulty]
    st.dataframe(data[['question','ideal_answer','role','difficulty','keywords']], use_container_width=True, hide_index=True)
