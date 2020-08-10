class MessageHandler:
    def __init__(self, *, prefix: str = "", suffix: str = ""):
        self.prefix = prefix
        self.suffix = suffix

    def process(self, message: str, **kwargs) -> str:
        """Processes the message."""
        return (self.prefix + message + self.suffix).format(**kwargs)
