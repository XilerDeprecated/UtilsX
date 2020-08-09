#   ©Xiler - Arthurdw

from datetime import datetime
from enum import Enum

codes = list(map(lambda i: f"\033[{i}m",
                 [0, 2, 4, 5, 7, 8, 21, 22, 24, 25, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45,
                  46, 47, 49, 90, 91, 92, 93, 94, 95, 96, 97, 100, 101, 102, 103, 104, 105, 106, 107]))


class Formats(Enum):
    default = "\033[0m\033[21m\033[22m\033[24m\033[25m\033[27m\033[28m"
    dim = "\033[2m"
    underline = "\033[4m"
    blink = "\033[5m"
    inverted = "\033[7m"
    hidden = "\033[8m"


class Colors(Enum):
    default = "\033[39m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    light_gray = "\033[37m"
    dark_gray = "\033[90m"
    light_red = "\033[91m"
    light_green = "\033[92m"
    light_yellow = "\033[93m"
    light_blue = "\033[94m"
    light_magenta = "\033[95m"
    light_cyan = "\033[96m"
    white = "\033[97m"


class Backgrounds(Enum):
    default = "\033[49m"
    black = "\033[40m"
    red = "\033[41m"
    green = "\033[42m"
    yellow = "\033[43m"
    blue = "\033[44m"
    magenta = "\033[45m"
    cyan = "\033[46m"
    light_gray = "\033[47m"
    dark_gray = "\033[100m"
    light_red = "\033[101m"
    light_green = "\033[102m"
    light_yellow = "\033[103m"
    light_blue = "\033[104m"
    light_magenta = "\033[105m"
    light_cyan = "\033[106m"
    white = "\033[107m"


class Prettier:
    """Console formatter"""

    def __init__(self, **kwargs):
        self.datetime_format = \
            str(kwargs.get("datetime_format") or
                f"{Formats.default.value + Colors.dark_gray.value + Backgrounds.default.value}["
                f"{Colors.light_green.value}%y-%d-%m %H:%M:%S{Colors.dark_gray.value}]{Colors.default.value} ")

        self.default_text_format = \
            str(kwargs.get("default_color") or Formats.default.value + Colors.default.value + Backgrounds.default.value)

        # 'x if x is not None else `default`' -> Cheat code to check if a x is passed and if its not None (undefined)
        self.colors_enabled = bool(kwargs.get("colors_enabled") if kwargs.get("colors_enabled") is not None else True)
        self.auto_strip_message = \
            bool(kwargs.get("auto_strip_message") if kwargs.get("auto_strip_message") is not None else False)

    @staticmethod
    def clear_colors(msg: str):
        """Removes ALL color codes from a string."""
        for code in codes:
            msg = msg.replace(code, "")
        return msg

    def print(self, message: str, time: datetime = None) -> None:
        """Pretty prints a given message"""
        print(self.format(message, time))

    def format(self, message: str, time: datetime = None) -> str:
        """Formats a given message"""
        data = str((self.format_timestamp(time) if time is not None else '') + self.default_text_format +
                   (message.strip() if self.auto_strip_message else message))
        return data if self.colors_enabled else self.clear_colors(data)

    def format_timestamp(self, time: datetime) -> str:
        """Formats a timestamp"""
        formatted = time.strftime(self.datetime_format)
        return formatted if self.colors_enabled else self.clear_colors(formatted)
