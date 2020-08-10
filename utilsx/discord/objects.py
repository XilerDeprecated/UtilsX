from typing import Union

from discord import Color


class Embed:
    def __init__(self, *, color: Union[Color, int] = None):
        self.color = color


class Footer:
    def __init__(self, text: str = "", icon_url: str = "", timestamp: bool = False):
        self.text = text
        self.icon_url = icon_url
        self.timestamp = timestamp


class Author:
    def __init__(self, name: str, url: str = "", icon_url: str = ""):
        self.name = name
        self.url = url
        self.icon_url = icon_url


class Field:
    def __init__(self, name: str, value: str, inline: bool = False):
        self.name = name
        self.value = value
        self.inline = inline
