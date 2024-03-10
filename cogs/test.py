import typing
from discord import app_commands
from discord.ext import commands
import discord





class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @app_commands.command(name="bonssse", description = "soirsoir")
    async def bonsoir15(self, interaction: discord.Interaction, name: str) -> None:
        await interaction.response.send_message(f"Bonsoir {name}")

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






