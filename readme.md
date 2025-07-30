# Telegram Channel Member & Admin Logger Bot


This bot automatically logs the following information from a Telegram channel:
- Names and usernames of users who post messages

- List of channel administrators (name, username, and user ID)

##  Features

Saves users (who post in the channel) to channel_users.txt

Saves admin list to channel_admins.txt

Prevents duplicate entries

Ignores non-channel messages

Fully asynchronous and lightweight

---
## installation
`bash`
- venv by using:
    - python -m venv .venv
    - .venv\scripts\activate
- telegram bot by using:
    - pip install python-telegram-bot 
---
 ## How to Run

1. Replace your bot token in the script:

    - TOKEN = "YOUR_BOT_TOKEN"


2. Run the Python script:

    - python bot.py


3. Add your bot as an admin in your Telegram channel.


4. As soon as someone posts in the channel, their info is logged. The admin list is also updated each time.

 ---
 ## Output Files

File Name Description

channel_users.txt Contains users who posted in the channel
channel_admins.txt Contains all current channel admins