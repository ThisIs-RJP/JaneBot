# Table of contents

RobinBot Python 

> Our dev log should be out soon! Stay tuned!

1. Basic Setup
- 1.1 [Prerequisites](#11-prerequisites)
- 1.2 [Installation Instructions](#12-installation-instructions)

### 1.1 Prerequisites

This bot was created with Python version [3.12](https://www.python.org/downloads/release/python-3120/). 
I am unsure how well this code will do with older versions.

It is also recommended to create a Python [virtual environment](https://docs.python.org/3/library/venv.html) (and mandatory for the latest Ubuntu Versions, e.g version 23).

See this [Reddit thread](https://www.reddit.com/r/learnpython/comments/1338la7/you_cant_use_pip_on_ubuntu_2304_anymore/?rdt=38421) for more information.

```
╭─prinz at eugen in ~/Janebot-Project/Janebot-app/dev on main✔
╰─± lsb_release -a

| No LSB modules are available.
| Distributor ID:	Ubuntu
| Description:	Ubuntu 24.04.2 LTS
| Release:	24.04
| Codename:	noble
```

We can create a virtual environment with the following

```
# optional: cd into preferred directory

python -m venv venv
source venv/bin/activate
```

### 1.2 Installation Instructions

You are also required to retrieve the [bot token](https://www.writebots.com/discord-bot-token/).

This token is a **SECRET** and should **NOT** be shared anywhere.

```
echo <bot_token> >> token.env 

git clone https://github.com/ThisIs-RJP/JaneBot.git

cd JaneBot/prod ## prod usually contains our latest changes, if you are in the main branch

pip install -r requirements.txt # Install dependencies

python3 main.py
```