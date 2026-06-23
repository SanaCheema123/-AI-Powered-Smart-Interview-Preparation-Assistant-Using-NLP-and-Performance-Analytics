import streamlit as st
import plotly.express as px
from components.styles import hero, metric_card
from components.data_loader import load_history


def show():
    hero('Performance Analytics', 'Track interview attempts, readiness score, weak areas, and category-wise performance.', 'Analytics')
    history = load_history()
    if history.empty:
        st.warning('No interview attempts found. Complete a mock interview first.')
        return
    c1, c2, c3 = st.columns(3)
    with c1: metric_card('Total Attempts', len(history), '📝')
    with c2: metric_card('Average Score', f"{history['score'].mean():.1f}%", '🎯')
    with c3: metric_card('Best Score', f"{history['score'].max():.1f}%", '🏆')

    left, right = st.columns(2)
    with left:
        fig = px.line(history, x='timestamp', y='score', markers=True, title='Score Trend')
        st.plotly_chart(fig, use_container_width=True)
    with right:
        cat = history.groupby('category', as_index=False)['score'].mean()
        fig = px.bar(cat, x='category', y='score', text='score', title='Average Score by Category')
        st.plotly_chart(fig, use_container_width=True)

    st.dataframe(history, use_container_width=True, hide_index=True)
