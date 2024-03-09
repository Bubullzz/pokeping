from init import *
from API import TestCommands
@bot.event
async def on_guild_join(guild):
    await init_guild(guild)

@bot.event
async def on_ready():
    print("Connecté !")
    await bot.load_extension('API.TestCommands')
    print("loaded !")
    await bot.tree.sync()
    print("Commandes syncro")


@bot.tree.command()
async def bonjour(interaction: discord.Interaction, user: discord.User):
    """
    Cette commande dit bonjour.

    user: discord.User
        L'utilisateur à saluer
    """
    await interaction.response.send_message(f"Bonjour {user.mention}")



bot.run("MTIxMDU5OTc3OTU1NDU1ODA2NA.GEairx.sCo4ASNdSM36255HGvu0b7AQzQDLsCW60UFV1g")