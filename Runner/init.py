import discord
from global_data import *
from DataClases import server

"""
@bot.tree.command()
async def init_guild(interaction: discord.Interaction):
    await init_g(interaction.guild)
"""
async def init_guild(guild):
    print(f'Bot joined server: {guild.name} (id: {guild.id})')
    servers[guild.id] = server.Server(guild)