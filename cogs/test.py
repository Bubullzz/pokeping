from typing import Set, List
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
        pkmn_name = pkmn_name.lower()
        pkmn_id = data.get_id(pkmn_name)
        if interaction.guild.id in global_data.servers:
            big_ass_string = ''.join([p.mention + ' ' for p in global_data.servers[interaction.guild.id].players.values() if
                                      p.interested(pkmn_id, interaction)])
            await interaction.response.send_message(f"A wild {pkmn_name} has spawned ! {big_ass_string}")
        else:
            await interaction.response.send_message(f"Server not registred !")

    @app_commands.command(name="stop_ping_here", description="stop getting pings from this channel")
    async def stop_ping_here(selfself, interaction: discord.Interaction) -> None:
        try:
            serv = global_data.servers[interaction.guild.id]
            serv.players[interaction.user.id].guild_to_chans[serv.guild_id].remove(interaction.channel.id)
            await interaction.response.send_message(f"You wont get pinged in this channel anymore !")
            return
        except:
            await interaction.response.send_message(f"Looks like you are already not getting any ping from this channel >:(")

    @app_commands.command(name="ping_me_here", description="start getting pings from this channel")
    async def ping_me_here(selfself, interaction: discord.Interaction) -> None:
        if interaction.guild.id not in global_data.servers:  # Check if server not already exists
            global_data.servers[interaction.guild.id] = server.Server(interaction.guild.id)
        serv = global_data.servers[interaction.guild.id]
        if interaction.user.id not in serv.players:  # Check if player exists in server
            serv.players[interaction.user.id] = player.Player(interaction.user.id, interaction.user.mention, True)
        play = serv.players[interaction.user.id]
        if interaction.guild.id not in play.guild_to_chans.keys():  # Check if player know this server
            play.guild_to_chans[serv.guild_id] = set()
        if interaction.channel.id not in play.guild_to_chans[serv.guild_id]:  # Add current channel if needed
            play.guild_to_chans[serv.guild_id].add(interaction.channel.id)
            await interaction.response.send_message(f"You will now receive pings in this channel !")
        else:
            await interaction.response.send_message(f"Looks like you are already getting pings from this channel >:(")

    async def xable(self, interaction: discord, argument: str, enable: bool) -> None:
        pretty_arg = argument
        argument = argument.lower()
        changed = False
        if interaction.guild.id not in global_data.servers:  # Check if server not already exists
            global_data.servers[interaction.guild.id] = server.Server(interaction.guild.id)
            changed = True

        serv = global_data.servers[interaction.guild.id]

        if interaction.user.id not in serv.players:  # Check if player exists in server
            serv.players[interaction.user.id] = player.Player(interaction.user.id, interaction.user.mention, not enable)
            changed = True

        play = serv.players[interaction.user.id]
        if interaction.guild.id not in play.guild_to_chans.keys():  # Check if player know this server
            play.guild_to_chans[serv.guild_id] = set()
            changed = True

        if interaction.channel.id not in play.guild_to_chans[serv.guild_id]:  # Add current channel if needed
            play.guild_to_chans[serv.guild_id].add(interaction.channel.id)
            changed = True

        if play.set_preference(argument, enable) or changed:
            await interaction.response.send_message(f"Changed your preference for {pretty_arg} !")
        else:
            await interaction.response.send_message(f"Your preference for {pretty_arg} was already set that way !")

    @app_commands.command(name="enable", description="enables pings for a pokemon or category")
    async def enable(self, interaction: discord.Interaction, target: str) -> None:
        await self.xable(interaction, target, True)

    @app_commands.command(name="disable", description="disables pings for a pokemon or category")
    async def disable(self, interaction: discord.Interaction, target: str) -> None:
        await self.xable(interaction, target, False)

    @report.autocomplete("pkmn_name")
    async def report_autocompletion(self, interaction: discord, current: str) -> List[
        app_commands.Choice[str]]:
        print("start")
        ret = []
        i = 0
        for name in data.pkmn_names:
            if current.lower() in name.lower():
                ret.append(app_commands.Choice(name=name, value=name))
                i += 1
                if i == 24:
                    return ret
        print("end")
        return ret

    @enable.autocomplete("target")
    @disable.autocomplete("target")
    async def report_autocompletion(self, interaction: discord, current: str) -> List[
        app_commands.Choice[str]]:
        if current == "":
            return [app_commands.Choice(name=name, value=name) for name in
                               ["all", "6-star", "5-star", "4-star", "Mega-Gardevoir", "Reshiram", "Primo-groudon"]]
        ret = []
        i = 0
        for name in data.xable_list:
            if current.lower() in name.lower():
                ret.append(app_commands.Choice(name=name, value=name))
                i += 1
                if i == 24:
                    return ret
        if (current == "all"):
            return [app_commands.Choice(name="all", value="all")]
        return ret

    @app_commands.command(name="list_preferences", description="see what your preferences are set to")
    async def list_preferences(self, interaction: discord.Interaction) -> None:
        if interaction.guild.id not in global_data.servers:
            await interaction.response.send_message(f"Server not registred !")
            return
        if interaction.user.id not in global_data.servers[interaction.guild.id].players:
            await interaction.response.send_message(f"Player not registred !")
            return
        p = global_data.servers[interaction.guild.id].players[interaction.user.id]
        await interaction.response.send_message(f"Here are your preferences :\n" + p.list_preferences(interaction))

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(test(bot))
