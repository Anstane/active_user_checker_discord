import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


load_dotenv()


telegram_bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')

dp = Dispatcher(bot=telegram_bot)


async def send_message_telegram(message):
    """Send a message to Telegram."""

    try:
        await telegram_bot.send_message(telegram_chat_id, message)
    except Exception as e:
        print("An error occurred {e}.")
