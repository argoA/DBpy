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

# variables are stored in a .env file for obscurity
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')
STAFF_ROLES = ( ### ADD NEW STAFF ROLES HERE ###
	'Owner',
	'Admin'
)
CHANNELS = { ### ADD NEW CHANNELS HERE ###
	'general': 740639148041306155,
	'test': 740667812615290972
}

bot = commands.Bot(command_prefix='!')

# returns channel id # from channel name REQUIRES updating CHANNELS dict
# ex. bot.get_channel() which requires the channel id
def get_channel_id(arg):
	for channel in CHANNELS:
		if channel == arg:
			channel_id = CHANNELS[channel]
	return channel_id

# checks if the arg is in channels dict. if so it returns the channel
def channel_name_check(channels, arg):
	for channel in channels:
		if channel == arg:
			return channel

# when the bot boots
@bot.event
async def on_ready():
	print(
		f'{bot.user.name} has connected!',
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

# command that purges chat by channel name
# probably a better way to do this function.
@bot.command(name='purge', help='* Purges all messages from a channel.')
@commands.has_role('Owner')
async def channel_purge(ctx, *args):
	channel_check = False
	verbose_check = False
	# added command line args for this command
	for arg in args:
		if arg == channel_name_check(CHANNELS, arg):
			channel_check = True
		# makes the command verbose
		if arg == '-v':
			verbose_check = True

	while channel_check:
		channel_id = get_channel_id(arg)
		channel = bot.get_channel(int(channel_id))
		if verbose_check:
			purged = await channel.purge(limit=200)
			await ctx.send(f'Purged {len(purged)} message(s) from {channel}')
			verbose_check = False
		else:
			await channel.purge(limit=100)
		channel_check = False

# TODO command that deletes messages by user
@bot.command(name='delete', help='* Deletes a users messages')
@commands.has_role('Owner' or 'Admin')
async def delete_user_message(ctx, name, channel):
	channel_id = get_channel_id(channel)
	channel = bot.get_channel(int(channel_id))
	#messages = discord.Message
	deleted = 0
	# for every message in channel history
	async for message in channel.history(limit=100):
		# author of message = message.author.name
		author = message.author.name
		# if supplied name input is authors name
		if name == author:
			await message.delete()
			# TODO make this actually delete the users message.
			deleted += 1
			#channel.delete_messages(message.author.name)

	await ctx.send(f'Deleted {deleted} of {name}\'s message(s)!') 

# command that prints total / online / offline members
@bot.command(name='members', help='* Prints total users')
@commands.has_role('Owner' or 'Admin')
async def members_count(ctx):
	guild = bot.get_guild(int(GUILD_ID))
	online = 0
	offline = 0
	# loops through guild members (m) and checks their status
	for m in guild.members:
		if str(m.status) == 'online':
			online += 1
		if str(m.status) == 'offline':
			offline += 1
	
	await ctx.send(
		f'```Total: {guild.member_count}\nOnline: {online}\nOffline: {offline}```'
	)

# ERROR handling
@bot.event
async def on_command_error(ctx, error):
	await ctx.send(f'ERROR: ({error})')

bot.run(TOKEN)