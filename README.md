# Discord Voice Channel Notification Bot

This Discord bot is designed to notify a specific role in the server about users joining voice channels. The role and text channel is specified in the .env file using the ROLE_NAME and TEXT_CHANNEL variable.

### Prerequisites

Before you start, make sure you have the Discord bot token:

- Discord bot token (you can obtain one by creating a new bot on the [Discord Developer Portal](https://discord.com/developers/applications))

### Setup

Clone the repository:

```
git clone git@github.com:Anstane/active_user_checker_discord.git
```

Install the poetry:

```
pip install poetry
```

Start the virtual env:

```
poetry shell
```


Install the required dependencies:

```
poetry install
```

Add your .env file to the core of project:
```
DISCORD_TOKEN=your_discord_bot_token
TEXT_CHANNEL=your_text_channel_id
ROLE_NAME=name_of_your_role
```

### Running the Bot

Run the bot using the following commands:

```
cd active_user_checker_discord
```

```
poetry run python main.py
```

### Bot commands:

- `/info`: Get information about the bot and its functionality.


### Notes

- Make sure the bot has the necessary permissions to read messages in the specified text channel and access voice state updates.
- Adjust the role name in the code to match the actual role name in your Discord server.
- Uncomment the relevant code if you want the bot to send messages to the Telegram.


### Author

- [@Anstane](https://github.com/Anstane)