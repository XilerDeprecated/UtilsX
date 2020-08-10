from typing import Union

from .exceptions import MissingFormatArguments
from .objects import Footer, Author


class MessageHandler:
    def __init__(self, *, prefix: str = "", suffix: str = ""):
        self.prefix = prefix
        self.suffix = suffix

    def process(self, message: str, **kwargs) -> str:
        """Processes the message."""
        try:
            return (self.prefix + message + self.suffix).format(**kwargs)
        except KeyError as e:
            args = ', '.join([f"'{arg}'" for arg in e.args])
            raise MissingFormatArguments(f"Missing format arguments {args}. "
                                         f"(fix eg, `format_args={{'{e.args[0]}': 'Cool String'}}`)")


class FooterHandler:
    def __init__(self, footer: Footer):
        self.footer = footer

    def process(self, obj: Union[Footer, None]) -> Union[Footer, None]:
        """Processes the footer and returns an appropriate Footer object!"""
        if obj:
            return Footer(text=(obj.text or self.footer.text),
                          icon_url=(obj.icon_url or self.footer.icon_url),
                          timestamp=(obj.timestamp if obj.timestamp else self.footer.timestamp))
        elif self.footer:
            return self.footer
        return None


class AuthorHandler:
    def __init__(self, author: Author):
        self.author = author

    def process(self, obj: Union[Author, None]) -> Union[Author, None]:
        """Processes the footer and returns an appropriate Author object!"""
        if obj:
            return Author(name=obj.name,
                          url=(obj.url or self.author.url),
                          icon_url=(obj.icon_url or self.author.icon_url))
        elif self.author:
            return self.author
        return None
