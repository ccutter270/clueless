class Weapon():

    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self):
        return f"Weapon({self.name})"

