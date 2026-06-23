from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / 'src'))
from preprocess import preprocess, PROCESSED_PATH


def load_data():
    if not PROCESSED_PATH.exists():
        preprocess()
    return pd.read_csv(PROCESSED_PATH)


def load_history():
    path = ROOT / 'data' / 'reports' / 'interview_history.csv'
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame(columns=['timestamp','question','category','difficulty','role','answer','score','feedback'])


def load_model_report():
    path = ROOT / 'outputs' / 'model_comparison.csv'
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame()
