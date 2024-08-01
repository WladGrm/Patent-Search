#!/bin/bash
if ! command -v pip &> /dev/null
then
    echo "pip is not installed. Please install pip and try again. or use: sudo apt-get install python3-pip"
    exit
fi
# Check if all dependencies are installed
if ! (pip freeze | grep -Fxq -f requirements.txt)
then
    # Some dependencies are missing, so install them
    echo "Installing missing dependencies..."
    pip install --ignore-installed -r requirements.txt
    echo "Dependencies installed."
else
    # Dependencies are already installed
    echo "All dependencies are already installed."
fi

# Run app
python3 app.py