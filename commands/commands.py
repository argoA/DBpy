import discord
from discord.ext import commands

@commands.command()
@commands.has_role('Owner')
async def channel_purge(ctx, amount=5):
	await ctx.channel.purge(limit=amount)

@commands.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@commands.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)

@commands.command
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)

@commands.command
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	# splits the user into name and their # discriminator
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user
		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			print(f'{user.name} was unbanned.')
			return
