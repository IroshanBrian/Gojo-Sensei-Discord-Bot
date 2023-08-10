import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN') 
intents = discord.Intents.default()
bot = commands.Bot (command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.username}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    user_message = message.content.lower()
    user_message = user_message.split(' ', 1) [1]
    response = ""
    
    if user_message == 'hello':
        response = f'Hello {message.author.mention}'
    elif user_message.startswith('!ask'):
        response = f"{message.author.mention} that's a good question"
    elif user_message.startswith('!help'):
        response = f"Hello {message.author.mention} GET SOME FUCKING HELP URSELF"
    elif user_message.startswith('!gay'):
        response = f"Hello {message.author.mention} Call Hephyrian rn"
    else:
        response = "I'm not sure how to answer that shit"    
        
    await message.channel.send(response)
    await bot.process_commands (message)

bot.run(TOKEN)