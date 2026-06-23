import streamlit as st
from components.styles import hero
from components.data_loader import load_history, load_model_report


def show():
    hero('Reports and Downloads', 'Export interview history, performance report, and model training summary.', 'Reports')
    history = load_history()
    model = load_model_report()

    st.markdown("<div class='content-card'><h3>Interview History Report</h3>", unsafe_allow_html=True)
    st.dataframe(history, use_container_width=True, hide_index=True)
    st.download_button('Download Interview History CSV', history.to_csv(index=False), 'interview_history.csv', 'text/csv')
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div class='content-card'><h3>Model Report</h3>", unsafe_allow_html=True)
    st.dataframe(model, use_container_width=True, hide_index=True)
    st.download_button('Download Model Report CSV', model.to_csv(index=False), 'model_report.csv', 'text/csv')
    st.markdown('</div>', unsafe_allow_html=True)
