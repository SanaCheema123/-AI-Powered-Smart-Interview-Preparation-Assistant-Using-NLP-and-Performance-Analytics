import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def normalize_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def keyword_score(answer: str, keywords: str) -> float:
    answer_tokens = set(normalize_text(answer).split())
    key_tokens = set(normalize_text(keywords).split())
    if not key_tokens:
        return 0.0
    return len(answer_tokens.intersection(key_tokens)) / len(key_tokens) * 100


def completeness_score(answer: str) -> float:
    words = normalize_text(answer).split()
    count = len(words)
    if count >= 80:
        return 100.0
    if count >= 50:
        return 85.0
    if count >= 30:
        return 70.0
    if count >= 15:
        return 55.0
    return 35.0


def evaluate_answer(candidate_answer: str, ideal_answer: str, keywords: str = '') -> dict:
    candidate_answer = str(candidate_answer).strip()
    ideal_answer = str(ideal_answer).strip()
    if not candidate_answer:
        return {'similarity_score': 0, 'keyword_score': 0, 'completeness_score': 0, 'final_score': 0, 'feedback': 'Please write a complete answer.'}

    vectorizer = TfidfVectorizer(stop_words='english')
    matrix = vectorizer.fit_transform([ideal_answer, candidate_answer])
    similarity = cosine_similarity(matrix[0:1], matrix[1:2])[0][0] * 100
    key_score = keyword_score(candidate_answer, keywords)
    comp_score = completeness_score(candidate_answer)
    final_score = (0.55 * similarity) + (0.25 * key_score) + (0.20 * comp_score)

    if final_score >= 85:
        feedback = 'Excellent answer. Strong relevance, good keyword coverage, and clear explanation.'
    elif final_score >= 70:
        feedback = 'Good answer. Add more role-specific examples and key terms to improve further.'
    elif final_score >= 50:
        feedback = 'Average answer. Improve structure, include important keywords, and explain with examples.'
    else:
        feedback = 'Needs improvement. Answer is short or not aligned with the expected response.'

    return {
        'similarity_score': round(similarity, 2),
        'keyword_score': round(key_score, 2),
        'completeness_score': round(comp_score, 2),
        'final_score': round(final_score, 2),
        'feedback': feedback
    }
