import typing
from Runner import global_data
from DataClases import player, server
from finders import data
from discord import app_commands
from discord.ext import commands
import discord


class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="bonssse", description="soirsoir")
    async def bonsoir15(self, interaction: discord.Interaction, name: str) -> None:
        await interaction.response.send_message(f"Bonsoir {name}")

    @app_commands.command(name="report", description="reports a raid")
    async def report(self, interaction: discord.Interaction, pkmn_name: str) -> None:
        pkmn_id = data.get_id(pkmn_name)
        if interaction.guild.id in global_data.servers:
            big_ass_string = ''.join([p.user.mention for p in global_data.servers[interaction.guild.id].players.values() if
                                      p.interested(pkmn_id)])
            await interaction.response.send_message(f"A wild {pkmn_name} has spawned ! {big_ass_string}")
        else:
            await interaction.response.send_message(f"Server not registred !")


    async def xable(self, interaction: discord, argument: str, enable: bool) -> None:
        if interaction.guild.id not in global_data.servers:
            global_data.servers[interaction.guild.id] = server.Server(interaction.guild)
        if interaction.user.id not in global_data.servers[interaction.guild.id].players:
            global_data.servers[interaction.guild.id].players[interaction.user.id] = player.Player(interaction.user,
                                                                                                   not enable)

        if global_data.servers[interaction.guild.id].players[interaction.user.id].set_preference(argument, enable):
            await interaction.response.send_message(f"Changed your preference for {argument} !")
        else:
            await interaction.response.send_message(f"Your preference for {argument} was already set that way !")

    @app_commands.command(name="enable", description="enables pings for a pokemon or category")
    async def enable(self, interaction: discord.Interaction, pkmn_name: str) -> None:
        await self.xable(interaction, pkmn_name, True)

    @app_commands.command(name="disable", description="disables pings for a pokemon or category")
    async def disable(self, interaction: discord.Interaction, pkmn_name: str) -> None:
        await self.xable(interaction, pkmn_name, False)

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

    @report.autocomplete("pkmn_name")
    async def report_autocompletion(self, interaction: discord, current: str) -> typing.List[
        app_commands.Choice[str]]:
        ret = []
        i = 0
        for name in data.pkmn_names:
            if current.lower() in name.lower():
                ret.append(app_commands.Choice(name=name, value=name))
                i += 1
                if i == 24:
                    return ret
        return ret


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(test(bot))
