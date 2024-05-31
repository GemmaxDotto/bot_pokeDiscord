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

# create a discord client
client = Client(intents=intents)
# get the discord token from the environment

# SPACE FOR THE DISCORD TOKEN I CANNOT SHOW

# define the commands
commands="My commands:\n* !pokemon pokemon_name -> to get a image of the pokemon \n* !stats pokemon_name -> to get the base stats of the pokemon \n* !abilities pokemon_name -> to get the abilities of the pokemon \n* !base_experience pokemon_name -> to get the base experience of the pokemon \n* !moves pokemon_name -> to get the possible moves of the pokemon \n* !types pokemon_name -> to get the types of the pokemon  and his strenghs and weaknesses"

# event to run when the bot is ready
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

# event to run when a new member joins the server -> the bot will send a welcome message in a private message to the new member
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server! Tell me a pokemon, I will tell u his stats for ur game! TYPE !commands to START'
    )
    
# event to run when a message is sent in the chat
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('!commands'):
    await message.channel.send(commands)
    
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
        sprite_url = pokemon.get_random_sprite()

        if sprite_url is not None:
            await message.channel.send(sprite_url)
        else:
            await message.channel.send(f"No sprite found for {pokemon_name}.")
    
  if message.content.startswith('!types'):
    pokemon_name = message.content.split(' ')[1]
    pokemon = Pokemon(pokemon_name)
    pokemon_types = pokemon.get_types()
    if pokemon_types:
      await message.channel.send(f"{pokemon_types}")
    else:
      await message.channel.send(f"Sorry, I couldn't find any types for {pokemon_name}.")
      
  await message.channel.send(f"Type !commands to see all my commands")
client.run(DISCORD_TOKEN)