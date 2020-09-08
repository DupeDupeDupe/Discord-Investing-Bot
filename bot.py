# bot.py
import os
import random
import requests
import discord
from dotenv import load_dotenv
from discord.ext import commands
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
API = os.getenv('API_TOKEN')
bot = commands.Bot(command_prefix='$')

@bot.command()
async def end(ctx, arg1):
    url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&outputsize=compact&apikey={}'.format(arg1, API)
    request = requests.get(url)
    response = request.text
    decoded_response = json.JSONDecoder().decode(response)
    await ctx.send(decoded_response)

bot.run(TOKEN)
