import streamlit as st
from pathlib import Path

from pages import dashboard, mock_interview, technical_questions, hr_questions
from pages import answer_evaluation, performance_analytics, reports, about

st.set_page_config(
    page_title="InterviewAI Pro",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
css_path = Path(__file__).parent / "assets" / "style.css"
with open(css_path, "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Remove Streamlit default page/navbar style
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

PAGES = {
    "Dashboard": dashboard.show,
    "Mock Interview": mock_interview.show,
    "Technical Questions": technical_questions.show,
    "HR Questions": hr_questions.show,
    "Answer Evaluation": answer_evaluation.show,
    "Performance Analytics": performance_analytics.show,
    "Reports": reports.show,
    "About Project": about.show,
}

with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand">
            <div class="brand-icon">🎙️</div>
            <div>
                <h2>InterviewAI Pro</h2>
                <p>Smart interview preparation assistant</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="nav-title">Navigation</div>', unsafe_allow_html=True)

    selected = st.radio(
        label="",
        options=list(PAGES.keys()),
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="sidebar-tip">
            Practice HR and technical interviews with AI-based answer scoring.
        </div>
        """,
        unsafe_allow_html=True
    )

PAGES[selected]()