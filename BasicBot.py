import os
import random 
import json
import math
import asyncio
import discord
import dotenv
from dotenv import load_dotenv
from discord.utils import get
from discord.ext import tasks,commands
from requests import get



# load_dotenv(".env")
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') # add token here
GUILD = os.getenv('DISCORD_GUILD')

clientintents = discord.Intents.all()

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

@client.event
async def on_ready():
   print(f'{client.user.name} is connected!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'COOL',('no doubt')
    ]
    star_wars_quotes = read_quotes("starwars.txt")

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)

        await message.channel.send(response)

    if message.content ==  'Star Wars':
        response = random.choice(star_wars_quotes)
        await message.channel.send(response)

    await bot.process_commands(message)

bot.run(TOKEN)


