import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
def config(bot):

	load_dotenv()
	bot.token = os.getenv('DISCORD_TOKEN')

	bot.admins = [740637118115872919,]