import os
import logging
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import track

import discord
from discord.ext import commands

# rich.console
console = Console()

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
	console.print(
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

# BUG: checks for user input 'hello'; stops
#      the code from checking for user commands (!)
"""
@bot.event
async def on_message(message):
	print(f'{message.channel}: {message.author}: {message.author.name}: {message.content}')
	if 'hello' in message.content.lower():
		await message.channel.send(f'Hi, {message.author.name}!')
"""

bot.run(TOKEN)