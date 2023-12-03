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


intents = discord.Intents.default() # Дефолтный набор намерений
intents.message_content = True # Включаем боту чат
intents.voice_states = True # Включаем боту голосовые чаты

bot = commands.Bot(command_prefix="/", intents=intents) # Создаём бота с параметром намерений


@bot.event
async def on_ready():
    """Функция кидает print при запусе бота."""

    logger.info(f"Бот запущен.")
    print(f"Бот активирован как: {bot.user}")


@bot.command(name="info")
async def info_command(ctx):
    """Бот отвечает на команду /info и описывает свой ход работы."""

    help_text = """
    Привет! Я здесь, чтобы следить за теми, кто присоединяется к голосовым каналам на сервере, и сообщать об этом всем пользователям.
    """

    username = ctx.author.name if ctx.author else 'Unknown User'
    logger.info(f"{username} запросил /info.")

    await ctx.send(help_text)


@bot.event
async def on_voice_state_update(member, before, after):
    """Функция, которая отслеживает кто заходит в голосовые чаты и сообщает всем об этом."""

    text_channel_id = os.getenv("TEXT_CHANNEL")
    text_channel = bot.get_channel(int(text_channel_id))

    if before.channel is None and after.channel is not None: # Проверяем, что кто-то присоединился.

        username = member.display_name if member else "Unknown User"
        logger.info(f"{username} - присоединился к чату: {after.channel.name}.")

        role_to_mention = discord.utils.get(member.guild.roles, name=os.getenv("ROLE_NAME"))

        if role_to_mention:
            await text_channel.send(
                f"{role_to_mention.mention} {username} - присоединился к чату: {after.channel.name}"
            )
        else:
            logger.error(f"Роль {role_to_mention} не найдена.")

        # await send_message_telegram(
        #     f"{username} - присоединился к чату: {after.channel.name}"
        # ) # Раскоментить эту строчку, если хотим, чтобы бот отправлял сообщение в ТГ.


bot.run(os.getenv("DISCORD_TOKEN"))
