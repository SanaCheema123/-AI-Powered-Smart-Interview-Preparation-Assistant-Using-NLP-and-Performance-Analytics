import pandas as pd


def recommend_questions(df: pd.DataFrame, role='All', category='All', difficulty='All', n=5):
    data = df.copy()
    if role != 'All':
        data = data[data['role'] == role]
    if category != 'All':
        data = data[data['category'] == category]
    if difficulty != 'All':
        data = data[data['difficulty'] == difficulty]
    if data.empty:
        data = df.copy()
    return data.sample(min(n, len(data)), random_state=None).reset_index(drop=True)
