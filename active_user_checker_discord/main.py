import discord
from discord.ext import commands


intents = discord.Intents.default() # Устанавливаем дефолтный набор намерений
intents.message_content = True # Делаем так, чтобы бот начал видеть сообщения
intents.voice_states = True # Проверяем голосовые чаты

client = discord.Client(intents=intents) # Создаём бота и передаём ему намерения


@client.event
async def on_ready(): # Когда бот готов - бросает это сообщение
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send('Hello!')


@client.event
async def on_voice_state_update(member, before, after):
    text_channel_id = 1026170389908430863
    text_channel = client.get_channel(text_channel_id)

    if before.channel is None and after.channel is not None:
        # Пользователь присоединился к голосовому каналу
        await text_channel.send(f"@everyone {member.display_name} присоединился к голосовому каналу {after.channel.name}")


client.run('MTE3OTE1MDQwMTY0ODQ3MjExNQ.Gjw6a3.-PFi5Drle1GjNJjza0JAqi7aNwP0ydYxX62bXw')
