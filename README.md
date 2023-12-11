# TypingTestAnalyzer.py - README
## By  Angelina Mom, Fernando Magallon-Romero, John Paul Minimo
## Overview
TypingTestAnalyzer.py is a Python script designed for analyzing typing tests. It leverages opencv2 and mediapipe for its operations, and has 3 other files that are needed to run properly, FingerDetection.py, TestStats.py, and TypingTest.py.
Prerequisites
Python 3.x
Pip (Python package installer)
## Installation
### Step 1: Setting up Python Environment
Ensure Python 3.x is installed on your system. Check this with:
via bash terminal:
`python --version`
If not installed, get it from python.org.
### Step 2: Installing Dependencies
TypingTestAnalyzer.py requires opencv2, mediapipe, and keyboard installable via pip:
via bash terminal:
`pip install opencv-python`
`pip install mediapipe`
`pip install keyboard`
### Step 3: Downloading TypingTestAnalyzer.py
Download our typing test project to a directory of your choice.
Usage
## Running the Script
Run TypingTestAnalyzer.py from its directory:
`python TypingTestAnalyzer.py`
Then follow instructions in the terminal.
## Features
### Typing Test Analysis 
Evaluates typing speed and accuracy.
### Video Processing
Uses opencv2 and mediapipe for video analysis, producing the number of times movement was spotted.
## Customization
Modify the script for customization. Users can adjust sensitivity and how many words are in the typing test by changing these values in TypingTestAnalyzer.py.

`num_words = 5` **Changes the amount of words in typing test.**

`fingerDetectionInstance = FingerDetection.FingerDetection(0.15)`  **A greater number makes it less sensitive (more finger travel distance to count as movement)**
### Known Issues
C++ Error on Apple Silicon
Running the script on Apple Silicon (M1/M2 chips) may result in a C++ error, as documented in this issue. This is due to compatibility issues with opencv2. The script works fine on Windows and Intel Mac platforms.
### Troubleshooting
Dependency Issues: Verify the correct installation of dependencies.
Python Version: Use Python 3.x for compatibility.
