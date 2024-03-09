import discord
import player
import global_data
from typing import Dict


class Server:
    guild: discord.Guild
    players: Dict[int, player.Player] = {}

    def __init__(self, guild: discord.Guild):
        self.guild = guild
        for player in guild.members:
            if global_data.players.get(player.id) != None:
                self.players[player.id] = global_data.players.get(player.id)