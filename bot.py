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
	await member.create_dm()
	await member.dm_channel.send(
		f'Hi there {member.name}, welcome to the server!'
	)

@bot.event
async def on_member_remove(member):
	print(f'{member} has left a server.')

# COGS
@bot.command()
async def load(ctx, extension):
	bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')

for cog in os.listdir('./cogs'):
	if cog.endswith('.py'):
		bot.load_extension(f'cogs.{cog[:-3]}')

bot.run(TOKEN)