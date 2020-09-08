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

#current price
@bot.command(
help="This returns the current quote for the requested stock. To use this command type '$current <Stock Ticker>'",
brief="This returns the current quote for the requested stock."
)
async def current(ctx, arg1): #TODO: add error handling.

    url = 'https://finnhub.io/api/v1/quote?symbol={}&token={}'.format(arg1, API)
    request = requests.get(url)
    response = request.text
    decoded_response = json.loads(response)
    current_price = (decoded_response['c'])
    await ctx.send('The current price of {} is: {}'.format(arg1, current_price))

#daily low
@bot.command(
help="This returns the daily low for the requested stock. To use this command type '$dl <Stock Ticker>'",
brief="This returns the daily low for the requested stock."
)
async def dl(ctx, arg1): #TODO: add error handling.

    url = 'https://finnhub.io/api/v1/quote?symbol={}&token={}'.format(arg1, API)
    request = requests.get(url)
    response = request.text
    decoded_response = json.loads(response)
    daily_low = (decoded_response['l'])
    await ctx.send('The daily low of {} is: {}'.format(arg1, daily_low))

#daily high
@bot.command(
help="This returns the daily high for the requested stock. To use this command type '$dh <Stock Ticker>'",
brief="This returns the daily high for the requested stock."
)
async def dh(ctx, arg1): #TODO: add error handling.

    url = 'https://finnhub.io/api/v1/quote?symbol={}&token={}'.format(arg1, API)
    request = requests.get(url)
    response = request.text
    decoded_response = json.loads(response)
    daily_high = (decoded_response['h'])
    await ctx.send('The daily high of {} is: {}'.format(arg1, daily_high))

#open
@bot.command(
help="This returns the opening price for the requested stock. To use this command type '$open <Stock Ticker>'",
brief="This returns the opening price for the requested stock."
)
async def open(ctx, arg1): #TODO: add error handling.

    url = 'https://finnhub.io/api/v1/quote?symbol={}&token={}'.format(arg1, API)
    request = requests.get(url)
    response = request.text
    decoded_response = json.loads(response)
    opened = (decoded_response['o'])
    await ctx.send('{} opened at: {}'.format(arg1, opened))

bot.run(TOKEN)