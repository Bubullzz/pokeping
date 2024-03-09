import typing

import discord

from Runner.global_data import *

from discord import app_commands


class TestCommands(commands.Cog):
    people = {}


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
    async def atoi_autocomplete(interaction: discord, current: str) -> typing.List[app_commands.Choice[str]]:
        data = []
        for n in ["one", "two", "three", "four"]:
            if current.lower() in n:
                data.append(app_commands.Choice(name=n))
        return data

    @bot.tree.command()
    @app_commands.autocomplete(number=atoi_autocomplete)
    async def atoi(interaction: discord.Interaction, number: str):
        await interaction.response.send_message(f"your number + {number}")



