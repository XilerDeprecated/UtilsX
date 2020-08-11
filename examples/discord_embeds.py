from discord.ext import commands

from utilsx.discord import Cog, BotX

DISCORD_BOT_TOKEN = "XXXYOURTOKENHEREXXX"


class Bot(BotX):
    def __init__(self):
        super().__init__()
        self.add_cog(UtilsX(self))


class UtilsX(Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name="test")
    async def test(self, ctx: commands.Context):
        await self.embed(ctx, "Hello World!", color=0xff131a)


if __name__ == "__main__":
    Bot().run(DISCORD_BOT_TOKEN)
