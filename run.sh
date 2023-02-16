#!/bin/bash

echo "Installing libraries"

pip install pillow
pip install python-dotenv

echo "Running main file"
python ./src/main.py