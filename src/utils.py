from pathlib import Path
import pandas as pd
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
HISTORY_PATH = ROOT / 'data' / 'reports' / 'interview_history.csv'


def save_attempt(question, category, difficulty, role, answer, score, feedback):
    HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    row = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'question': question,
        'category': category,
        'difficulty': difficulty,
        'role': role,
        'answer': answer,
        'score': score,
        'feedback': feedback
    }
    if HISTORY_PATH.exists():
        df = pd.read_csv(HISTORY_PATH)
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    else:
        df = pd.DataFrame([row])
    df.to_csv(HISTORY_PATH, index=False)
    return df
