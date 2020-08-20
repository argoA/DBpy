import discord
from discord.ext import commands

from random import choice

class User(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.slap_counter = 0

	@commands.command(help="Randomly slap someone!")
	async def slap(self, ctx):
		author = ctx.message.author
		member = choice(ctx.channel.guild.members)
		# Just incase the choice is the author
		while member is author:
			member = choice(ctx.channel.guild.members)			
		
		await ctx.send(f'{author.mention} slapped {member.mention}!')

		self.slap_counter += 1
		if self.slap_counter == 100:
			self.slap_counter = 0
			await ctx.send(
				f'Congratulations! :partying_face: You have reached :100: slaps!\n`Reseting counter back to 0!`'
			)

def setup(bot):
	bot.add_cog(User(bot))