from typing import List

from discord import Embed, File, AllowedMentions
from discord.ext import commands
from discord.message import Message

from .handlers import MessageHandler


class Cog(commands.Cog):
    def __init__(self, *, message_handler: MessageHandler = None):
        self.message_handler = message_handler

    async def send(self, ctx: commands.Context, message: str, *, tts: bool = False, embed: Embed = None,
                   file: File = None, files: List[File] = None, nonce: int = None, delete_after: float = None,
                   allowed_mentions: AllowedMentions = None, handler_enabled: bool = True, format_args: dict = None
                   ) -> Message:
        """Process a message and send it using the default discord.py send method."""
        if format_args is None:
            format_args = {}
        message = self.message_handler.process(message, **format_args) \
            if self.message_handler and handler_enabled else message

        return await ctx.send(message, tts=tts, embed=embed, file=file, files=files, nonce=nonce,
                              delete_after=delete_after, allowed_mentions=allowed_mentions)

    async def embed(self, ctx: commands.Context, message: str, *, title: str = None, raw: str = "",
                    handler_enabled: bool = True, format_args: dict = None) -> Message:
        """Processes and sends a message"""
        message = self.message_handler.process(message, **format_args) \
            if self.message_handler and handler_enabled else message
        return await ctx.send(raw, embed=Embed(title=title or "", color=0xff00ff, description=message))
