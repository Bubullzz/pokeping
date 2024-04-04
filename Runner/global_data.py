from typing import Dict
from DataClases import player, server
import json

players: Dict[int, player.Player] = {}
servers: Dict[int, server.Server] = {}

with open('server.json', 'r') as file:
    servers_data = json.load(file)

for server_id, server_data in servers_data.items():
    s = server.Server(server_data['guild_id'])
    for player_id, player_data in server_data['players'].items():
        player_obj = player.Player.from_dict(player_data)
        s.players[int(player_id)] = player_obj

    servers[int(server_id)] = s

print(servers[1184858846397734952].to_dict())