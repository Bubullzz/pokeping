import discord
from DataClases import player
from Runner import global_data
from typing import Dict


class Server:

    def __init__(self, guild: discord.Guild):
        self.guild = guild
        self.players: Dict[int, player.Player] = {}
        for p in guild.members:
            if global_data.players.get(p.id) is not None:
                self.players[p.id] = global_data.players.get(p.id)

    def to_dict(self):
        # Convert instance attributes to a dictionary
        return {
            "guild_id": self.guild.id,
            "players": {str(player_id): player_data.to_dict() for player_id, player_data in self.players.items()}
        }

    @classmethod
    def from_dict(cls, guild, data):
        # Create a new Server instance from a dictionary
        server = cls(guild)
        server.players = {int(player_id): player.Player.from_dict(player_data) for player_id, player_data in data.get("players", {}).items()}
        return server
