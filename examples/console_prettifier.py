import utilsx
from utilsx.console import Prettier, Colors
from datetime import datetime


if __name__ == "__main__":
    p = Prettier(default_text_format=Colors.yellow.value)

    p.print(f"Running on UtilsX {utilsx.__version__}")

    p.print("Hello World!", datetime.now())

