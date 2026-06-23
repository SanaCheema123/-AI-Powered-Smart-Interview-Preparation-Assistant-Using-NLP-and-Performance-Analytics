from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]


def load_css():
    css_path = ROOT / 'assets' / 'style.css'
    if css_path.exists():
        st.markdown(f'<style>{css_path.read_text()}</style>', unsafe_allow_html=True)


def hero(title, subtitle, badge='InterviewAI Pro'):
    st.markdown(f"""
    <div class='hero-box'>
        <span class='hero-badge'>{badge}</span>
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def metric_card(title, value, icon='📊'):
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-icon'>{icon}</div>
        <p>{title}</p>
        <h2>{value}</h2>
    </div>
    """, unsafe_allow_html=True)
