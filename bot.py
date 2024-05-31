# Description: This file contains the code for the discord bot. The bot will connect to the discord server and listen for messages. The bot will respond to messages.

            
import os
import random
import discord
from dotenv import load_dotenv
from discord import Intents
from discord import Client

load_dotenv() # load the environment variables

from api import Pokemon

intents = Intents.default() # create a discord intent
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
    print(f'{client.user.name} has connected to Discord!') # print the bot name

# event to run when a new member joins the server -> the bot will send a welcome message in a private message to the new member
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.') # print the new member
    await member.create_dm() # create a direct message channel with the new member
    await member.dm_channel.send( # send a welcome message to the new member
        f'Hi {member.name}, welcome to my Discord server! Tell me a pokemon, I will tell u his stats for ur game! TYPE !commands to START' 
    )
    
# event to run when a message is sent in the chat
@client.event
async def on_message(message): 
  if message.author == client.user: # if the message is sent by the bot, return
    return
  
  if message.content.lower().startswith('!commands'): # get the commands
    await message.channel.send(commands) # send the commands
    
  if message.content.lower().startswith('!stats'): # get the stats of the pokemon
    pokemon_name = message.content.split(' ')[1] # get the pokemon name
    pokemon = Pokemon(pokemon_name) # create a Pokemon object
    pokemon_stats = pokemon.get_stats() # get the stats of the pokemon
    if pokemon_stats:
      pokemon_statsF=pokemon.format_stats(pokemon_stats) # format the stats
      await message.channel.send(f"Stats for {pokemon_name}: {pokemon_statsF}") # send the stats of the pokemon
    else:
      await message.channel.send(f"Sorry, I couldn't find any stats for {pokemon_name}.") # send a message if no stats are found
      
  if message.content.lower().startswith('!abilities'): # get the abilities of the pokemon
    pokemon_name = message.content.split(' ')[1] # get the pokemon name
    pokemon = Pokemon(pokemon_name) # create a Pokemon object
    pokemon_abilities = pokemon.get_abilities() # get the abilities of the pokemon
    if pokemon_abilities:
      await message.channel.send(f"Abilities for {pokemon_name}: {pokemon_abilities}") # send the abilities of the pokemon
    else:
      await message.channel.send(f"Sorry, I couldn't find any abilities for {pokemon_name}.") # send a message if no abilities are found
      
  if message.content.lower().startswith('!base_experience'): # get the base experience of the pokemon
    pokemon_name = message.content.split(' ')[1] # get the pokemon name
    pokemon = Pokemon(pokemon_name) # create a Pokemon object
    pokemon_base_experience = pokemon.get_base_experience() # get the base experience of the pokemon
    if pokemon_base_experience:
      await message.channel.send(f"Base experience for {pokemon_name}: {pokemon_base_experience}") # send the base experience of the pokemon
    else:
      await message.channel.send(f"Sorry, I couldn't find any base experience for {pokemon_name}.") # send a message if no base experience is found
      
  if message.content.lower().startswith('!moves'): # get the moves of the pokemon
    pokemon_name = message.content.split(' ')[1] # get the pokemon name
    pokemon = Pokemon(pokemon_name) # create a Pokemon object
    pokemon_moves = pokemon.format_moves() # get the moves of the pokemon
    if pokemon_moves:
        await send_large_message(message.channel, f"Moves for {pokemon_name}: {pokemon_moves}")
    else:
      await message.channel.send(f"Sorry, I couldn't find any moves for {pokemon_name}.")  # send a message if no moves are found
  
  if message.content.lower().startswith('!pokemon'): # get the pokemon sprite image
        pokemon_name = message.content.split(' ')[1] # get the pokemon name
        pokemon = Pokemon(pokemon_name) # create a Pokemon object
        sprite_url = pokemon.get_random_sprite() # get the sprite url

        if sprite_url is not None:
            await message.channel.send(sprite_url) # send the sprite url
        else:
            await message.channel.send(f"No sprite found for {pokemon_name}.") # send a message if no sprite is found
    
  if message.content.lower().startswith('!types'): # get the types of the pokemon
    pokemon_name = message.content.split(' ')[1] # get the pokemon name
    pokemon = Pokemon(pokemon_name) # create a Pokemon object
    pokemon_types = pokemon.get_types() # get the types of the pokemon
    if pokemon_types:
      await message.channel.send(f"{pokemon_types}") # send the types of the pokemon
    else:
      await message.channel.send(f"Sorry, I couldn't find any types for {pokemon_name}.") # send a message if no types are found
      
  await message.channel.send(f"Type !commands to see all my commands") # send a message to type !commands to see all the commands

async def send_large_message(channel, message):
    if len(message) <= 2000:
        await channel.send(message)
    else:
        parts = [message[i:i+2000] for i in range(0, len(message), 2000)]
        for part in parts:
            await channel.send(part)
            
client.run(DISCORD_TOKEN)


