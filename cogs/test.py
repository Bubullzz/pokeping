import typing
from Runner import global_data
from finders import data
from discord import app_commands
from discord.ext import commands
import discord

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @app_commands.command(name="bonssse", description = "soirsoir")
    async def bonsoir15(self, interaction: discord.Interaction, name: str) -> None:
        await interaction.response.send_message(f"Bonsoir {name}")

    @app_commands.command(name="report", description = "reports a raid")
    async def report(self, interaction: discord.Interaction, pkmn_name: str) -> None:
        pkmn_id = data.get_id(pkmn_name)
        big_ass_string = ''.join([player.user.mention for player in global_data.servers[interaction.guild.id].players if player.interested(pkmn_id)])
        await interaction.response.send_message(f"A wild {pkmn_name} has spawned ! {big_ass_string}")

    @app_commands.command(name="enable", description = "enables pings for a pokemon or category")
    async def enable(self, interaction: discord, argument: str) -> None:
        if argument in data.category_names or argument == 'all':
            interaction.user


    @app_commands.command()
    async def atoi(self, interaction: discord.Interaction, item: str):
        await interaction.response.send_message(f"your number + {item}")

    @atoi.autocomplete("item")
    async def atoi_autocompletion(self, interaction: discord.Interaction, current: str) -> typing.List[
        app_commands.Choice[str]]:
        data = []
        for n in ["M_GENGAR",
                "M_GARDEVOIR",
                "M_CHARIZARD_X"]:
            if current.lower() in n:
                data.append(app_commands.Choice(name=n, value=n))
        return data

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(test(bot))






