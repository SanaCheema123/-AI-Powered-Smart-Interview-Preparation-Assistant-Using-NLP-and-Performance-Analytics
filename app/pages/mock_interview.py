import streamlit as st
from components.styles import hero
from components.data_loader import load_data
from src.question_recommender import recommend_questions
from src.answer_scoring import evaluate_answer
from src.utils import save_attempt


def show():
    hero('Mock Interview Practice', 'Select role, category, and difficulty, then answer a generated interview question.', 'Practice Mode')
    df = load_data()

    c1, c2, c3 = st.columns(3)
    with c1: role = st.selectbox('Select Role', ['All'] + sorted(df['role'].unique().tolist()))
    with c2: category = st.selectbox('Question Category', ['All'] + sorted(df['category'].unique().tolist()))
    with c3: difficulty = st.selectbox('Difficulty', ['All'] + sorted(df['difficulty'].unique().tolist()))

    if 'current_question' not in st.session_state:
        st.session_state.current_question = None

    if st.button('Generate Interview Question'):
        rec = recommend_questions(df, role, category, difficulty, n=1)
        st.session_state.current_question = rec.iloc[0].to_dict()

    q = st.session_state.current_question
    if q:
        st.markdown(f"""
        <div class='content-card'>
            <h3>Interview Question</h3>
            <p><b>Role:</b> {q['role']} &nbsp; | &nbsp; <b>Category:</b> {q['category']} &nbsp; | &nbsp; <b>Difficulty:</b> {q['difficulty']}</p>
            <h2>{q['question']}</h2>
        </div>
        """, unsafe_allow_html=True)
        answer = st.text_area('Write your answer here', height=180)
        if st.button('Submit Answer and Evaluate'):
            result = evaluate_answer(answer, q['ideal_answer'], q['keywords'])
            save_attempt(q['question'], q['category'], q['difficulty'], q['role'], answer, result['final_score'], result['feedback'])
            st.markdown(f"""
            <div class='result-box'>
                <h3>Evaluation Result</h3>
                <h2>Final Score: {result['final_score']}%</h2>
                <p><b>Similarity:</b> {result['similarity_score']}% | <b>Keyword Match:</b> {result['keyword_score']}% | <b>Completeness:</b> {result['completeness_score']}%</p>
                <p><b>Feedback:</b> {result['feedback']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info('Click Generate Interview Question to start your mock interview.')
