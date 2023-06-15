@echo off

echo Setting up Virtual environment to not pollute your system...
python -m venv venv
call venv\scripts\activate.bat

echo Setting up dependencies...
pip install -r requirements.txt
