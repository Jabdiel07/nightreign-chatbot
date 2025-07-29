# nightreign-chatbot
Retrieval based Discord chatbot to get information about Elden Ring Nightreign

# Features

- Slash command /category to choose between characters or bosses and what field you want information about

- Simple !hello command to make sure the bot is alive and running

- Robust logging via Pythons's logging module with both console and file handles

# Prerequisites

- Python 3.8+ installed on your system

- A Discord application and bot token (you can create this at the Discord Developer Portal: https://discord.com/developers/applications)

- Git for cloning the repository

# Setup & Installation

1. Clone the repository and move into the directory

git clone https://github.com/<your-username>/nightreign-chatbot.git
cd discord-generative-chatbot

2. Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate # macOS/Linux
venv\Scripts\Activate # Windows PowerShell

3. Install dependencies

pip install -r requirements.txt

4. Create a .env file in the project root and set the following

DISCORD_TOKEN = your_bot_token_here (this is provided to you when you create your bot in the Dev Portal, if you don't remember it, you have the option to reset it and a new one will be generated)

# Configuration

- Discord intents: In Discord's Dev Portal, under your bot's settings,enable the Message Content Intent so the bot can read message text

- Environment Variables:
    - DISCORD_TOKEN: your bot's token
    - LOG_LEVEL (optional): Sets the logging level (DEBUG, INFO, etc) at launch. By default, this is already set to INFO

# Logging

- All logs are output to:
    - Console
    - File: logs/bot.log with auto-rotation (max of 5MB and up to 3 backups at a time)

- If you want detailed DEBUG loggings, set the LOG_LEVEL environment variable and run the following in the terminal:
    - export LOG_LEVEL=DEBUG
    - python main.py

# Usage

1. Start the bot

pyhton main.py

2. Run the commands in Discord

/category "character or boss" "name" "field": This will allow the user to enter the category of choice (between character or boss), choose the name of the character or boss they want information about, and the field they want to gather information from (this could be like lore, description, passive abilities, weaknesses, and more).

!hello: The bot will reply in chat with "Hello! I'm alive."

# Troubleshooting

- Bot not responding: Check that DISCORD_TOKEN is correct and the bot is invited to your server
- Missing intents errors: Enable the Message Content Intent in the Discord Developer Portal
- Logging not showing DEBUG: Make sure LOG_LEVEL is set to DEBUG  before starting the bot in the same terminal session
