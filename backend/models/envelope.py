from models.character import Character
from models.location import Location
from models.weapon import Weapon


class Envelope:

    def __init__(self, weapon: Weapon, suspect: Character, room: Location) -> None:
        self.weapon = weapon    # The weapon used in the crime
        self.suspect = suspect  # The character who committed the crime
        self.room = room        # The location where the crime took place

        self.solution = [weapon, suspect, room]

    def __repr__(self):
        return f"Envelope({self.weapon}, {self.suspect}, {self.room})"
