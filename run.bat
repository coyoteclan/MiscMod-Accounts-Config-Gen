@echo off
REM Update Python and pip
python -m pip install --upgrade pip setuptools wheel

REM Install the required Python packages
pip install pysimplegui==4.60.5

REM Run the Python script
python main.py
