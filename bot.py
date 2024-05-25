# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')

from discord import Intents
from discord import Client

intents = Intents.default()
intents.members = True

client = Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server! Tell me a pokemon, I will tell u his stats for ur game! TYPE !hello to START'

    )
    

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('!hello'):
    await message.channel.send('My commands: !pokemon pokemon_name')

client.run(TOKEN)