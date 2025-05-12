#!/bin/bash

set -e

cd ~
source venv/bin/activate

cd JaneBot
git pull origin main
pip install -r requirements.txt

cd ~/JaneBot/code/prod/JaneBot
pkill -f "python3 main.py" || true
nohup python3 main.py > bot.log 2>&1 &

echo "Deployment complete!"

exit 0