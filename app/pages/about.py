import streamlit as st
from components.styles import hero


def show():
    hero('About Project', 'AI-Powered Smart Interview Preparation Assistant Using NLP and Performance Analytics.', 'Project Overview')
    st.markdown("""
    <div class='content-card'>
    <h3>Project Objective</h3>
    <p>This project helps students and job seekers practice HR and technical interview questions. It uses NLP methods to evaluate candidate answers and provides performance analytics.</p>
    <h3>Main Features</h3>
    <ul>
        <li>HR and technical question bank</li>
        <li>Mock interview question generator</li>
        <li>TF-IDF and cosine similarity based answer evaluation</li>
        <li>Keyword coverage and completeness scoring</li>
        <li>Performance analytics and CSV reports</li>
    </ul>
    <h3>Technology Stack</h3>
    <p>Python, Streamlit, Pandas, Scikit-learn, Plotly, Joblib</p>
    </div>
    """, unsafe_allow_html=True)
