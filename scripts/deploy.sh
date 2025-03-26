#!/bin/bash

### This is the deployment script for deploying the bot in the server

cd
source venv/bin/activate
cd JaneBot/
pip install -r requirements.txt
cd prod
git pull origin main
pkill -f "python3 main.py" || true
nohup python3 main.py > bot.log 2>&1 &
echo "Deployment complete!"