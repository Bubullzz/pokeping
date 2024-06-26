import discord
from discord.ext import commands
import json
import Runner
import signal
import sys


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='/',
            intents=discord.Intents.default())

    async def setup_hook(self):
        await self.load_extension(f"cogs.test")
        await bot.tree.sync()

    async def on_ready(self):
        print("ready")


bot = MyBot()


def signal_handler(sig, frame):
    print("Received signal:", sig)

    print("Performing cleanup actions...")

    servers_dict = {server_id: server.to_dict() for server_id, server in Runner.global_data.servers.items()}
    with open('server.json', 'w') as file:
        json.dump(servers_dict, file)

    print("Dumped !")

    sys.exit(0)


# Register signal handlers
signal.signal(signal.SIGINT, signal_handler)  # SIGINT is generated by Ctrl+C
signal.signal(signal.SIGTERM, signal_handler)  # SIGTERM is generated by system signals

#ensure that we write the changes in case of Error
try:
    bot.run("TOKEN")
except Exception as e:
    servers_dict = {server_id: server.to_dict() for server_id, server in Runner.global_data.servers.items()}
    with open('server.json', 'w') as file:
        json.dump(servers_dict, file)

    print("Dumped !")

    sys.exit(0)
