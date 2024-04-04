import discord
from DataClases import player
from typing import Dict


class Server:

    def __init__(self, guild_id: int):
        self.guild_id: int = guild_id
        self.players: Dict[int, player.Player] = {}


    def to_dict(self):
        return {
            "guild_id": self.guild_id,
            "players": {str(player_id): player.to_dict() for player_id, player in self.players.items()}
        }

    @classmethod
    def from_dict(cls, data):
        # Fetch guild object from cache or None if not found
        guild = discord.utils.get(discord.client.guilds, id=data['guild_id'])
        if guild is None:
            # If guild not found, create a new Guild object
            guild = discord.Guild(id=data['guild_id'])

        server = cls(guild)
        for player_id, player_data in data['players'].items():
            p = player.Player.from_dict(player_data)
            server.add_player(p)
        return server
