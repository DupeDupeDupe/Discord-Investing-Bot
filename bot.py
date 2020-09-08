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
DEFAULT_ARG = "empty"

#current price
@bot.command(
help="This returns the current quote for the requested stock. To use this command type '$current <Stock Ticker>'",
brief="This returns the current quote for the requested stock."
)

async def current(ctx, arg1=DEFAULT_ARG): #TODO: add error handling for quotes. #TODO: Make function reusable

    if arg1 != 'empty':
        url = 'https://finnhub.io/api/v1/quote?symbol={}&token={}'.format(arg1, API)
        request = requests.get(url)
        response = request.text
        decoded_response = json.loads(response)
        try:
            current_price = (decoded_response['c'])
        except KeyError:
            await ctx.send('"{}" Is not a valid stock ticker! Please use a valid ticker.'.format(arg1))
        except ExpectedClosingQuoteError:
            await ctx.send('Close your damn quote.')
        await ctx.send('The current price of {} is: {}'.format(arg1, current_price))
    else:
        await ctx.send('You need to include at least one ticker to your command.')

bot.run(TOKEN)