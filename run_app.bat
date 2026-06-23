@echo off
cd /d %~dp0
py src\train_model.py
py -m streamlit run app\app.py
pause
