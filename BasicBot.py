import os
import random 
<<<<<<< HEAD
import json
import math
import asyncio
import discord
import math_functions
from dotenv import load_dotenv
from discord.utils import get
from discord.ext import tasks,commands
from requests import get
=======

import discord
from dotenv import load_dotenv
from discord.utils import get
from discord.ext import tasks,commands
>>>>>>> e4b1171 (Basic structure and connection implemented)


load_dotenv(".env")
TOKEN =  os.getenv('DISCORD_TOKEN') # add token here
GUILD = os.getenv('DISCORD_GUILD')

clientintents = discord.Intents.all()

<<<<<<< HEAD
bot = commands.Bot(command_prefix='!')

client = discord.Client()

def read_quotes(file):
    infile = open(file, "r")
    content = infile.readlines()
     # mainlist = content.split(",")

    # for line in infile:
    #     mainlist.append(line.strip().split(','))
    return content


# @client.event
# async def on_ready():
#  print(f'{client.user.name} is connected!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected as super bot')

@bot.command(name='meme')
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content)
    meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
    await ctx.send(embed=meme)

@bot.command(name='convertPolar')
async def convertPolar(ctx):
        
        await ctx.send('Input resistor value: ')
        message_response = await bot.wait_for('message')
        a = (message_response.content)
        
        await ctx.send('Input capacitive reactance value: ')
        message_response = await bot.wait_for('message')
        b = (message_response.content)

        # a = input("Input resistor value: ")
        # b = input("input capacitive reactance value: ")

        magnitude = math.sqrt((int(a)**2) + (int(b)**2))
        print(magnitude)

        phase_angle = math.degrees(math.atan(int(b)/int(a)) )
        print(phase_angle)

        # result = print(f'Z = {magnitude} \u2221 {phase_angle}')
        
        await ctx.send(f'z = {magnitude} \u2221 {phase_angle}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
=======
bot = commands.Bot(command_prefix='b?', intents=clientintents)

client = discord.Client()

@client.event
async def on_ready():
   print(f'{client.user.name} is connected!')


@client.event
async def on_message(message):
    if message.author == client.user:
>>>>>>> e4b1171 (Basic structure and connection implemented)
        return

    brooklyn_99_quotes = [
        'COOL',('no doubt')
    ]
<<<<<<< HEAD
    star_wars_quotes = read_quotes("starwars.txt")

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)

        await message.channel.send(response)

    if message.content ==  'Star Wars':
        response = random.choice(star_wars_quotes)
        await message.channel.send(response)

    await bot.process_commands(message)

bot.run(TOKEN)
=======

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

client.run(TOKEN)
>>>>>>> e4b1171 (Basic structure and connection implemented)
