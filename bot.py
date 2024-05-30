# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from discord import Intents
from discord import Client

load_dotenv()

from api import Pokemon

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
  
  if message.content.startswith('!commands'):
    await message.channel.send('My commands:\n* !pokemon pokemon_name\n* !stats pokemon_name\n* !abilities pokemon_name\n* !base_experience pokemon_name\n* !moves pokemon_name')
  if message.content.startswith('!stats'):
    pokemon_name = message.content.split(' ')[1]
    pokemon = Pokemon(pokemon_name)
    pokemon_stats = pokemon.get_stats()  
    if pokemon_stats:
      pokemon_statsF=pokemon.format_stats(pokemon_stats)
      await message.channel.send(f"Stats for {pokemon_name}: {pokemon_statsF}")
    else:
      await message.channel.send(f"Sorry, I couldn't find any stats for {pokemon_name}.")
  if message.content.startswith('!abilities'):
    pokemon_name = message.content.split(' ')[1]
    pokemon = Pokemon(pokemon_name)
    pokemon_abilities = pokemon.get_abilities()
    if pokemon_abilities:
      await message.channel.send(f"Abilities for {pokemon_name}: {pokemon_abilities}")
    else:
      await message.channel.send(f"Sorry, I couldn't find any abilities for {pokemon_name}.")
  if message.content.startswith('!base_experience'):
    pokemon_name = message.content.split(' ')[1]
    pokemon = Pokemon(pokemon_name)
    pokemon_base_experience = pokemon.get_base_experience()
    if pokemon_base_experience:
      await message.channel.send(f"Base experience for {pokemon_name}: {pokemon_base_experience}")
    else:
      await message.channel.send(f"Sorry, I couldn't find any base experience for {pokemon_name}.")
  if message.content.startswith('!moves'):
    pokemon_name = message.content.split(' ')[1]
    pokemon = Pokemon(pokemon_name)
    pokemon_moves = pokemon.format_moves()
    if pokemon_moves:
      await message.channel.send(f"Moves for {pokemon_name}: {pokemon_moves}")
    else:
      await message.channel.send(f"Sorry, I couldn't find any moves for {pokemon_name}.")
  if message.content.startswith('!pokemon'):
    pokemon_name = message.content.split(' ')[1]
    pokemon = Pokemon(pokemon_name)
    pokemon_image = pokemon.get_image()
    if pokemon_image:
      await message.channel.send(f"Image for {pokemon_name}: {pokemon_image}")
    else:
      await message.channel.send(f"Sorry, I couldn't find any image for {pokemon_name}.")
    

client.run(DISCORD_TOKEN)