#!/bin/bash

# Check if the virtual environment directory exists
if [ -d "venv" ]; then
    # Check if we are on Windows
    if [[ "$OS" == "Windows_NT" ]]; then
        # Activate virtual environment for Windows
        source venv/Scripts/activate
    else
        # Activate virtual environment for Unix-based systems (Linux, macOS)
        source venv/bin/activate
    fi
    streamlit run src/streamlit_app.py
else
    echo "Virtual environment not found. Please run install.sh before running this script."
    exit 1
fi
