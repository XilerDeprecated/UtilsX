from discord.ext import commands

from utilsx.discord import Cog

DISCORD_BOT_TOKEN = "XXXYOURTOKENHEREXXX"


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!",
                         description="UtilsX discord embed example bot!",
                         case_insensitive=True,
                         help_attrs=dict(hidden=True))
        self.add_cog(UtilsX(self))

    def run(self):
        super().run(DISCORD_BOT_TOKEN, reconnect=True)


class UtilsX(Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name="test")
    async def test(self, ctx: commands.Context):
        await self.embed(ctx, "Hello World!", color=0xff131a)


if __name__ == "__main__":
    Bot().run()
