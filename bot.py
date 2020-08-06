import os
import logging
from dotenv import load_dotenv

import discord
from discord.ext import commands

# LOGGING
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='err.log', encoding='utf-8')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
STAFF_ROLES = ('Owner', 'Admin')

bot = commands.Bot(command_prefix='!')

# when the bot boots
@bot.event
async def on_ready():
	print(
		f'{bot.user.name} has connected!', style="bold white", justify="center"
	)

# welcome new members
@bot.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
		f'Hi {member.name}, welcome to the server!'
	)

# command that adds two ints
@bot.command(name='add', help='Adds two integers.')
async def add(ctx, a: int, b: int):
	await ctx.send(a + b)

# TODO make a command that clears chat
@bot.command(name='clear', help='* Clears messages.')
@commands.has_role('Owner')
async def clear(ctx, name):
	print('clear')
	
# ERROR handling
@bot.event
async def on_command_error(ctx, error):
	await ctx.send(f'ERROR: Try !help ({error})')

bot.run(TOKEN)