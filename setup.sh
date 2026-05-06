#!/bin/bash

# setup.sh - Automated Deployment Script for your Project

echo "--- 1. Updating System Packages ---"
sudo apt update && sudo apt upgrade -y

echo "--- 2. Installing Python Environment Tools ---"
sudo apt install python3-venv -y

echo "--- 3. Creating Virtual Environment ---"
python3 -m venv venv

echo "--- 4. Activating Environment and Installing Dependencies ---"
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "--- SETUP COMPLETE! ---"
echo "Your environment is ready."
echo "To run your app, simply type: source venv/bin/activate && streamlit run app.py --server.port 80"