import os
import logging
from logging.handlers import RotatingFileHandler

import discord
from discord.ext import commands
from dotenv import load_dotenv

# from telegram import send_message_telegram


load_dotenv()


logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)

log_handler = RotatingFileHandler(
    filename="discord.log",
    encoding="utf-8",
    maxBytes=32 * 1024 * 1024,
    backupCount=1,
)

dt_fmt = '%Y-%m-%d %H:%M:%S'
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s', dt_fmt)

log_handler.setFormatter(log_formatter)
logger.addHandler(log_handler)


intents = discord.Intents.default() # Default set of intents
intents.message_content = True # Enable bot chat
intents.voice_states = True # Enable bot voice chats

bot = commands.Bot(command_prefix="/", intents=intents) # Create a bot with an intent parameter


@bot.event
async def on_ready():
    """The function throws print when the bot starts."""

    logger.info(f"The bot is running.")
    print(f"The bot is activated as: {bot.user}")


@bot.command(name="info")
async def info_command(ctx):
    """The bot responds to the /info command and describes its functions."""

    help_text = """
    Hello! I'm here to monitor who is joining the voice channels on the server and report it to all users.
    """

    username = ctx.author.name if ctx.author else 'Unknown User'
    logger.info(f"{username} requested /info.")

    await ctx.send(help_text)


@bot.event
async def on_voice_state_update(member, before, after):
    """A function that tracks who enters voice chats and notifies everyone about it."""

    text_channel_id = os.getenv("TEXT_CHANNEL")
    text_channel = bot.get_channel(int(text_channel_id))

    if before.channel is None and after.channel is not None: # Checking that someone has joined.

        username = member.display_name if member else "Unknown User"
        logger.info(f"{username} - joined the chat: {after.channel.name}.")

        role_to_mention = discord.utils.get(member.guild.roles, name=os.getenv("ROLE_NAME"))

        if role_to_mention:
            await text_channel.send(
                f"{role_to_mention.mention} {username} - joined the chat: {after.channel.name}"
            )
        else:
            logger.error(f"Role {role_to_mention} not found.")

        # await send_message_telegram(
        #     f"{username} - joined the chat: {after.channel.name}"
        # ) # Uncomment this line if we want the bot to send a message to the Telegram.


bot.run(os.getenv("DISCORD_TOKEN"))
