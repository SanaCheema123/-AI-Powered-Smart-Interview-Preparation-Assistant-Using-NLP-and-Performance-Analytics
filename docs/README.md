# AI-Powered Smart Interview Preparation Assistant

This is a complete educational AI/NLP project for interview preparation using HR and technical interview questions. It includes a Streamlit dashboard, NLP answer scoring, question recommendation, performance analytics, and reports.

## Project Features

- Dashboard with dataset statistics
- HR and Technical question banks
- Mock interview question generator
- NLP answer evaluation using TF-IDF and cosine similarity
- Keyword coverage score
- Completeness score
- Interview history tracking
- Performance analytics dashboard
- CSV report download

## Dataset

The project is designed for the Kaggle dataset: **Interview Questions HR Technical**. A sample dataset is already included in:

```text
data/raw/interview_questions.csv
```

You can replace this file with the Kaggle dataset. Make sure the file contains or can be mapped to these columns:

```text
question, ideal_answer, category, difficulty, role, type, keywords
```

## Folder Structure

```text
ai_interview_preparation_assistant/
├── app/
│   ├── app.py
│   ├── pages/
│   ├── components/
│   └── assets/
├── data/
│   ├── raw/
│   ├── processed/
│   └── reports/
├── models/
├── src/
├── outputs/
├── docs/
├── requirements.txt
└── run_app.bat
```

## Installation

Open PowerShell inside the project folder and run:

```bash
py -m pip install -r requirements.txt
```

## Train Model

```bash
py src\train_model.py
```

## Run Dashboard

```bash
py -m streamlit run app\app.py
```

## Windows Shortcut

Double-click:

```text
run_app.bat
```

## Main Modules

### Preprocessing
Cleans dataset, standardizes columns, removes duplicates, and saves processed CSV.

### Question Recommendation
Filters and recommends questions based on role, category, and difficulty.

### Answer Scoring
Uses TF-IDF and cosine similarity to compare candidate answers with ideal answers. It also calculates keyword match and completeness score.

### Performance Analytics
Stores mock interview attempts and shows score trends, average score, and category-wise performance.

## Project Workflow

```text
Interview Dataset
        ↓
Data Cleaning
        ↓
Question Recommendation
        ↓
Mock Interview
        ↓
Answer Evaluation
        ↓
Performance Analytics
        ↓
Report Generation
```
