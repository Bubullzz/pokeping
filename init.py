import discord
from global_data import *

@bot.tree.command()
async def init_guild(interaction: discord.Interaction):
    await init_g(interaction.guild)

async def init_g(guild):
    print(f'Bot joined server: {guild.name} (id: {guild.id})')
    servers[guild.id] = 