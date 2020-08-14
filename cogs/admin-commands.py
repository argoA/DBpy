import discord
from discord.ext import commands
from cogs.helpers import checks

class Admin(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(help='checks server ping')
	@checks.is_server_admin()
	async def ping(self, ctx):
		await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

	@commands.command()
	@checks.is_server_admin()
	async def clear(self, ctx, amount=5):
		await ctx.channel.purge(limit=amount)

	@commands.command()
	@checks.is_server_admin()
	async def kick(self, ctx, member : discord.Member, *, reason=None):
		await member.kick(reason=reason)

	@commands.command()
	@checks.is_server_admin()
	async def ban(self, ctx, member : discord.Member, *, reason=None):
		await member.ban(reason=reason)

	@commands.command()
	@checks.is_server_admin()
	async def unban(self, ctx, member):
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split('#')

		for ban_entry in banned_users:
			user = ban_entry.user
			if (user.name, user.discriminator) == (member_name, member_discriminator):
				await ctx.guild.unban(user)
				print(f'{user.name} was unbanned.')
				return

def setup(bot):
	bot.add_cog(Admin(bot))