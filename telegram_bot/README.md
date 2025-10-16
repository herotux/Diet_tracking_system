# Telegram Bot

This is the Telegram bot for the Diet & Fitness Tracking System.

## Setup

1.  Create a `.env` file from the `.env.example` and fill in your Telegram bot token.
2.  Install the dependencies: `pip install -r requirements.txt`.
3.  Run the bot: `python bot.py`.

## Commands

-   `/start` - Start the bot
-   `/setlang <fa|en|ku>` - Set the language
-   `/link <username> <password>` - Link your account
-   `/today` - Get today's plan
-   `/complete <item_id> <status> [note]` - Mark an item as complete
    -   `status` can be `COMPLETED`, `PARTIALLY_COMPLETED`, or `NOT_COMPLETED`.