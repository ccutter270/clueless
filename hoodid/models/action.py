class Action:

    type: str
    message: str

    def __init__(self, type: str, message: str) -> None:
        self.type = type
        self.message = message
