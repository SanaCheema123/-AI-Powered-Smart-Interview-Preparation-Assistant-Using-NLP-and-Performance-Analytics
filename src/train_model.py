from pathlib import Path
import sys
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / 'src'))
from preprocess import preprocess, PROCESSED_PATH

MODELS_DIR = ROOT / 'models'
OUTPUTS_DIR = ROOT / 'outputs'


def train():
    df = preprocess()
    df['combined_text'] = df['question'] + ' ' + df['ideal_answer'] + ' ' + df['keywords']

    vectorizer = TfidfVectorizer(stop_words='english', max_features=500)
    X_text = vectorizer.fit_transform(df['combined_text'])
    y = df['category']

    if y.nunique() < 2 or len(df) < 10:
        print('Dataset is too small for classifier training. Vectorizer saved only.')
        MODELS_DIR.mkdir(exist_ok=True)
        joblib.dump(vectorizer, MODELS_DIR / 'tfidf_vectorizer.pkl')
        return

    X_train, X_test, y_train, y_test = train_test_split(X_text, y, test_size=0.25, random_state=42, stratify=y)
    model = RandomForestClassifier(n_estimators=120, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)
    precision, recall, f1, _ = precision_recall_fscore_support(y_test, preds, average='weighted', zero_division=0)

    MODELS_DIR.mkdir(exist_ok=True)
    OUTPUTS_DIR.mkdir(exist_ok=True)
    joblib.dump(vectorizer, MODELS_DIR / 'tfidf_vectorizer.pkl')
    joblib.dump(model, MODELS_DIR / 'performance_model.pkl')

    report = pd.DataFrame([
        {'Model': 'TF-IDF + Random Forest', 'Accuracy': round(acc, 4), 'Precision': round(precision, 4), 'Recall': round(recall, 4), 'F1 Score': round(f1, 4)}
    ])
    report.to_csv(OUTPUTS_DIR / 'model_comparison.csv', index=False)
    print(f'Model trained successfully. Accuracy: {acc:.4f}')
    print(f'Model saved: {MODELS_DIR / "performance_model.pkl"}')


if __name__ == '__main__':
    train()
