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
bot.run("MTIxMDU5OTc3OTU1NDU1ODA2NA.G69h6c.wf-qMC3kcugCuX2bRHm_pnZ86wRFVv2I7Dgbgo")