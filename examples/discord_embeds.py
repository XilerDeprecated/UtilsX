from discord.ext import commands
from utilsx.discord import Cog
from utilsx.discord.handlers import MessageHandler

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
        self.message_handler = MessageHandler(prefix="Hey there, ", suffix="!\nI'm {name}")

    @commands.command(name="test")
    async def test(self, ctx: commands.Context):
        await self.send(ctx, ctx.author.mention, format_args={"name": self.bot.user.name})
        await self.embed(ctx, ctx.author.mention, format_args={"name": self.bot.user.name})


if __name__ == "__main__":
    Bot().run()
