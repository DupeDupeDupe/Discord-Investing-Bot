# bot.py
import os
import requests
import discord
import json
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
API = os.getenv('API_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.command(
help="This returns the current quote for the requested stock. To use this command type '$current <Stock Ticker>'",
brief="This returns the current quote for the requested stock."
)
async def current(ctx, arg1): #TODO: add error handling

    url = 'https://finnhub.io/api/v1/quote?symbol={}&token={}'.format(arg1, API)
    request = requests.get(url)
    response = request.text
    decoded_response = json.loads(response)
    current_price = (decoded_response['c'])
    await ctx.send('The current price of {} is: {}'.format(arg1, current_price))

bot.run(TOKEN)

#hot desk swap wright pat
