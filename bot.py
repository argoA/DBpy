import discord
from discord.ext import commands

import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected')

@bot.event
async def on_member_join(member):
	print(f'{member} has joined a server.')

@bot.event
async def on_member_remove(member):
	print(f'{member} has left a server.')

# COGS
@bot.command(help='Loads a specific cog')
async def load(ctx, extension):
	bot.load_extension(f'cogs.{extension}')

@bot.command(help='Unloads a specific cog')
async def unload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')

# Loads all local cogs
for cog in os.listdir('./cogs'):
	if cog.endswith('.py'):
		bot.load_extension(f'cogs.{cog[:-3]}')

# Made it this far. Time to start the bot
try:
	bot.loop.run_until_complete(bot.start(TOKEN))
except KeyboardInterrupt:
	pass
finally:
	bot.loop.run_until_complete(bot.logout())

	bot.loop.close()