import discord
from discord.ext import commands

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
bot.run("MTIxMDU5OTc3OTU1NDU1ODA2NA.GxVQb4.NHyAo_58h09yV1OXkC9z49KaQDY0UBQc3Qi3dk")