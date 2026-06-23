import streamlit as st
from components.styles import hero
from components.data_loader import load_data
from src.answer_scoring import evaluate_answer


def show():
    hero('AI Answer Evaluation', 'Compare your answer with an ideal answer using TF-IDF similarity, keyword coverage, and completeness scoring.', 'NLP Scoring')
    df = load_data()
    question = st.selectbox('Choose a question', df['question'].tolist())
    row = df[df['question'] == question].iloc[0]
    st.markdown(f"<div class='info-box'><b>Expected Area:</b> {row['role']} | <b>Difficulty:</b> {row['difficulty']}</div>", unsafe_allow_html=True)
    answer = st.text_area('Candidate Answer', height=180)
    if st.button('Evaluate Answer'):
        result = evaluate_answer(answer, row['ideal_answer'], row['keywords'])
        c1, c2, c3, c4 = st.columns(4)
        c1.metric('Final Score', f"{result['final_score']}%")
        c2.metric('Similarity', f"{result['similarity_score']}%")
        c3.metric('Keyword Match', f"{result['keyword_score']}%")
        c4.metric('Completeness', f"{result['completeness_score']}%")
        st.success(result['feedback'])
        with st.expander('Show ideal answer'):
            st.write(row['ideal_answer'])
