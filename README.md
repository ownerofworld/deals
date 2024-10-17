# Deals [TGBOT]

## Description
**Deals [TGBOT]** is a Telegram bot designed to automate the process of forwarding deal messages from one source channel to multiple target channels. The bot listens for new messages in a specified source channel (where deals or discounts are posted) and forwards them to other Telegram channels you manage.

This bot can help manage deal sharing across multiple groups or channels, saving time and effort, and ensuring that all target channels are updated with the latest deals in real-time.

## Features
- **Automated Forwarding**: Automatically forwards messages from a source channel to one or more target channels.
- **Customizable Target Channels**: You can configure multiple target channels where deals will be forwarded.
- **Easy Setup**: The bot can be easily set up by providing the channel IDs and bot API token.
- **Real-Time Forwarding**: Ensures that deals are forwarded immediately as they are posted in the source channel.

## Setup Instructions

### Prerequisites
- **Telegram API Token**: You need to create a Telegram bot using [BotFather](https://core.telegram.org/bots#botfather) and get the bot API token.
- **Channel IDs**: You need the channel IDs of the source and target channels where messages will be forwarded.

### Steps to Set Up

1. Clone the repository:
```bash
git clone https://github.com/ownerofworld/deals
cd deals
```
2: Install dependencies:

```bash
pip install -r requirements.txt
```
3: Replace `TOKEN` in bot.py
4: Run with
```bash
python3 bot.py
```
5: Add the bot to your source and target channels with the appropriate permissions (like sending messages to target channels).

## Usage

Once the bot is set up and running, it will automatically forward any new messages from the source channel to all specified target channels.
