import discord
from discord.ext import commands
from typing import Dict


players: Dict = {}
servers: Dict = {}
bot = commands.Bot(command_prefix="/", intents=discord.Intents.default())
