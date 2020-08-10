from datetime import datetime
from random import randint
from typing import List, Union

from discord import Embed, File, AllowedMentions, Color
from discord.abc import Messageable
from discord.ext import commands
from discord.message import Message

from . import objects as obj
from .handlers import MessageHandler, FooterHandler, AuthorHandler


class Cog(commands.Cog):
    def __init__(self, *, message_handler: MessageHandler = None):
        self.message_handler = message_handler
        self.embed_object = obj.Embed()
        self.footer_handler = FooterHandler(obj.Footer())
        self.author_handler = AuthorHandler(obj.Author("Unfilled Parameter"))

    def handle_message(self, message: str, format_args: dict, handler_enabled: bool) -> str:
        """Checks and handles a message."""
        if format_args is None:
            format_args = {}
        return self.message_handler.process(message, **format_args) \
            if self.message_handler and handler_enabled else message

    async def send(self, channel: Messageable, message: str, *, tts: bool = False, embed: Embed = None,
                   file: File = None, files: List[File] = None, nonce: int = None, delete_after: float = None,
                   allowed_mentions: AllowedMentions = None, handler_enabled: bool = True, format_args: dict = None
                   ) -> Message:
        """Process a message and send it using the default discord.py send method."""
        message = self.handle_message(message, format_args, handler_enabled)
        return await channel.send(message, tts=tts, embed=embed, file=file, files=files, nonce=nonce,
                                  delete_after=delete_after, allowed_mentions=allowed_mentions)

    async def embed(self, channel: Messageable, message: str, *, title: str = None, raw: str = "",
                    handler_enabled: bool = True, color: Union[Color, int] = None, format_args: dict = None,
                    image: str = None, thumbnail: str = None, footer: obj.Footer = None, author: obj.Author = None,
                    fields: List[obj.Field] = None) -> Message:
        """Processes and sends a message"""
        message = self.handle_message(message, format_args, handler_enabled)
        color = color or self.embed_object.color or Color(int(hex(randint(0, 16581375)), 0))
        embed = Embed(title=title or "", color=color, description=message)
        if image:
            embed.set_image(url=image)
        if thumbnail:
            embed.set_thumbnail(url=thumbnail)
        footer = self.footer_handler.process(footer)
        if footer:
            embed.set_footer(text=footer.text, icon_url=footer.icon_url)
            if footer.timestamp:
                embed.timestamp = datetime.now()
        author = self.author_handler.process(author)
        if author:
            embed.set_author(name=author.name, url=author.url, icon_url=author.icon_url)
        if fields:
            for field in fields:
                embed.add_field(name=field.name, value=field.value, inline=field.inline)
        return await channel.send(raw, embed=embed)
