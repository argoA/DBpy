import discord
from discord import Status
from discord.ext import commands
from cogs.helpers import checks

import os

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

# Load the config
from cogs.helpers.config import config

config(bot)

@bot.command(aliases=['tm'], help='Checks total members.')
@checks.is_super_admin()
async def total_members(ctx):
	online, offline, total = 0, 0, 0
	total = len([m for m in ctx.guild.members if not m.bot])
	online = len([m for m in ctx.guild.members if m.status == Status.online])
	offline = len([m for m in ctx.guild.members if m.status == Status.offline])


	await ctx.send(f'Total: {total}\nOnline: {online}\nOffline: {offline}')

# COGS
@bot.command(help='Loads a specific cog')
@checks.is_super_admin()
async def load(ctx, extension):
	bot.load_extension(f'cogs.{extension}') 

@bot.command(help='Unloads a specific cog')
@checks.is_super_admin()
async def unload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')

# Loads all local cogs
for cog in os.listdir('./cogs'):
	if cog.endswith('.py'):
		bot.load_extension(f'cogs.{cog[:-3]}')

# Made it this far. Time to start the bot
try:
	bot.loop.run_until_complete(bot.start(bot.token))
except KeyboardInterrupt:
	pass
finally:
	bot.loop.run_until_complete(bot.logout())

	bot.loop.close()