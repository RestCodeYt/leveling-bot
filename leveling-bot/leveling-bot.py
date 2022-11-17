import discord
from discord.ext.commands import Bot

intents = discord.Intents.default()
intents.message_content = True

bot = Bot(command_prefix='R', intents=intents)

bot.run('TOKEN')
