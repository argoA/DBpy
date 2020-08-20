from discord.ext import commands

class NotSuperAdmin(commands.CheckFailure):
	pass

def is_super_admin():
	async def predicate(ctx):
		cond = ctx.message.author.id in ctx.bot.admins

		if cond:
			return True
		else:
			raise NotSuperAdmin

	return commands.check(predicate)

class NotServerAdmin(commands.CheckFailure):
	pass

def is_server_admin():
	async def predicate(ctx):
		cond = ctx.message.channel.permissions_for(ctx.message.author).administrator

		if cond:
			return True
		else:
			raise NotServerAdmin

	return commands.check(predicate)