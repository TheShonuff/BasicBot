import discord
import os
from dotenv import load_dotenv
from discord.ext import commands, tasks
from discord.utils import get

load_dotenv(".env")
TOKEN = os.getenv('DISCORD_TOKEN') # add token here
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print("I am running on " + bot.user.name)
    
    print('Bot is ready to be used')
   # after it is ready do it

    takenGuild = bot.get_guild('DISCORD_GUILD')
    print(takenGuild.id)

    for guild in bot.guilds:
        print(guild)
        print(guild.id)
    
    
bot.run(TOKEN)
