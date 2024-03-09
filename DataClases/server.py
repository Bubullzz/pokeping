import discord
from DataClases import player
from Runner import global_data
from typing import Dict


class Server:
    guild: discord.Guild
    players: Dict[int, player.Player] = {}

    def __init__(self, guild: discord.Guild):
        self.guild = guild
        for p in guild.members:
            if global_data.players.get(p.id) is not None:
                self.players[p.id] = global_data.players.get(p.id)