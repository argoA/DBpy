import discord
from discord.ext import commands
from discord.ext.commands import BucketType

from cogs.helpers import checks
from cogs import spawning

class Admin(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	# command that adds two ints
	@commands.command(name='add', help='Adds two integers.')
	async def add(ctx, a: int, b: int):
	await ctx.send(a + b)

	# command that purges chat by channel name
	# probably a better way to do this function.
	@commands.command(name='purge', help='* Purges all messages from a channel.')
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

	# command that deletes messages by user
	@comamnds.command(name='delete', help='* Deletes a users messages')
	@commands.has_role('Owner' or 'Admin')
	async def delete_user_message(ctx, name, channel):
		channel_id = get_channel_id(channel)
		channel = bot.get_channel(int(channel_id))
		deleted = 0
		# for every message in channel history
		async for message in channel.history(limit=100):
			author = message.author.name
			# if supplied name input is authors name
			if name == author:
				await message.delete()
				deleted += 1

		await ctx.send(f'Deleted {deleted} of {name}\'s message(s)!') 

	# command that prints total / online / offline members
	@commands.command(name='members', help='* Prints total users')
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