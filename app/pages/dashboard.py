import streamlit as st
import plotly.express as px
from components.styles import hero, metric_card
from components.data_loader import load_data, load_history, load_model_report


def show():
    hero('AI-Powered Smart Interview Preparation Assistant', 'NLP-based mock interview practice, question recommendation, answer scoring, and performance analytics.', 'NLP + Performance Analytics')
    df = load_data()
    history = load_history()
    model_report = load_model_report()

    counts = df['category'].value_counts()
    diff_counts = df['difficulty'].value_counts()

    c1, c2, c3, c4, c5 = st.columns(5)
    with c1: metric_card('Total Questions', len(df), '📚')
    with c2: metric_card('Technical', int(counts.get('Technical', 0)), '💻')
    with c3: metric_card('HR', int(counts.get('Hr', counts.get('HR', 0))), '👥')
    with c4: metric_card('Attempts', len(history), '📝')
    avg = f"{history['score'].mean():.1f}%" if not history.empty else '0%'
    with c5: metric_card('Avg Score', avg, '🎯')

    left, right = st.columns([1.1, 1])
    with left:
        st.markdown("<div class='content-card'><h3>Question Category Distribution</h3>", unsafe_allow_html=True)
        chart_df = counts.reset_index(); chart_df.columns = ['Category','Questions']
        fig = px.pie(chart_df, names='Category', values='Questions', hole=0.42)
        fig.update_layout(height=420, margin=dict(l=10,r=10,t=20,b=10))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        st.markdown("<div class='content-card'><h3>Difficulty Distribution</h3>", unsafe_allow_html=True)
        ddf = diff_counts.reset_index(); ddf.columns = ['Difficulty','Questions']
        fig = px.bar(ddf, x='Difficulty', y='Questions', text='Questions')
        fig.update_layout(height=420, showlegend=False, margin=dict(l=10,r=10,t=20,b=10))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div class='content-card'><h3>Dataset Preview</h3>", unsafe_allow_html=True)
    st.dataframe(df.head(12), use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if not model_report.empty:
        st.markdown("<div class='content-card'><h3>Model Training Summary</h3>", unsafe_allow_html=True)
        st.dataframe(model_report, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)
