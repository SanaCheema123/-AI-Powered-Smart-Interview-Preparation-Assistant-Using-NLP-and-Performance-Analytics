from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / 'data' / 'raw' / 'interview_questions.csv'
PROCESSED_PATH = ROOT / 'data' / 'processed' / 'cleaned_questions.csv'

REQUIRED_COLUMNS = ['question', 'ideal_answer', 'category', 'difficulty', 'role', 'type', 'keywords']


def load_dataset(path=RAW_PATH):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f'Dataset not found at {path}')
    return pd.read_csv(path)


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            df[col] = 'General'

    df = df[REQUIRED_COLUMNS]
    df = df.drop_duplicates(subset=['question'])

    for col in REQUIRED_COLUMNS:
        df[col] = df[col].astype(str).str.strip()
        df[col] = df[col].replace({'': 'General', 'nan': 'General', 'None': 'General'})

    df['category'] = df['category'].str.title()
    df['difficulty'] = df['difficulty'].str.title()
    df['type'] = df['type'].str.title()
    return df


def preprocess(path=RAW_PATH):
    df = load_dataset(path)
    df = clean_dataset(df)
    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)
    return df


if __name__ == '__main__':
    df = preprocess()
    print(f'Processed dataset saved: {PROCESSED_PATH}')
    print(f'Total questions: {len(df)}')
