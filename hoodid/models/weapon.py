from hoodid.models.card import Card


class Weapon(Card):

    name: str

    def __init__(self, name: str) -> None:
        self.name = name