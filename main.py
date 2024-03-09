import discord
import player
import server
import global_data
from global_data import *
from init import *

from discord.ext import commands

people = {}
@bot.tree.command()
async def bonjour(interaction: discord.Interaction, user: discord.User):
    """
    Cette commande dit bonjour.

    user: discord.User
        L'utilisateur à saluer
    """
    await interaction.response.send_message(f"Bonjour {user.mention}")

@bot.tree.command()
async def count(interaction: discord.Interaction, val: int):
    """
    Cette commande compte.

    val: int
        la val à add
    """
    x = people.get(interaction.user.id)
    s = ""
    if x == None:
        x = 0
        s = f"Added you with count {val}\n"
        people[interaction.user.id] = 0
    people[interaction.user.id] = x + val
    await interaction.response.send_message(f"{s}Curr tot = {x + val}")

@bot.event
async def on_guild_join(guild):
    init_guild(guild)

@bot.event
async def on_ready():
    print("Connecté !")
    await bot.tree.sync()
    print("Commandes syncro")



bot.run("MTIxMDU5OTc3OTU1NDU1ODA2NA.GkEKVc.aXb5DXawvw-X9EXJa_Mo3HCHjIs3SeI5icLLhE")