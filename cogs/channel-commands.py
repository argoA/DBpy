import discord
from discord.ext import tasks, commands

class Channels(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=['tc'], help="Create a temporary voice channel.")
	async def temp_channel(self, ctx, channel):
		member = ctx.message.author
		guild = ctx.message.guild
		# CREATES the channel
		channel = await guild.create_voice_channel(channel)

		# Moves the user to channel.
		reason = (f"Moved to their temporary channel, {channel}!")
		await member.move_to(channel, reason=reason)

		# TODO make the channel delete if empty

	@commands.command(aliases=['dc'], help="Delete channel.")
	async def delete_channel(self, ctx, channel : discord.VoiceChannel):
		await channel.delete(reason='')

	@commands.command(aliases=['cm'])
	async def channel_members(self, ctx, channel : discord.VoiceChannel):
		await ctx.send(f'Members: {len(channel.members)}')
		if len(channel.members) == 0:
			await ctx.send('YES IT IS EMPTY!')

def setup(bot):
	bot.add_cog(Channels(bot))