#!/bin/bash

### This is the deployment script for deploying the bot in the server

cd
# Activating Virtual Environment
source venv/bin/activate

# Change to main directory
cd JaneBot && git pull origin main && pip install -r requirements.txt
cd ~/JaneBot/code/prod/JaneBot && pkill -f "python3 main.py" || true && nohup python3 main.py > bot.log 2>&1
echo "Deployment complete!"