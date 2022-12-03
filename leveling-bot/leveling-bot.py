import discord
from discord.ext.commands import Bot
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = Bot(command_prefix='R', intents=intents)

bot.run(os.getenv('TOKEN'))
