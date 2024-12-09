import json

from models.location import Location


class Character:

    name: str
    location: Location
    homeSquare: Location
    moved_to: bool

    def __init__(self, name: str, location: Location, homeSquare: Location) -> None:
        self.name = name
        self.location = location        # Current location of the character
        self.homeSquare = homeSquare    # Starting location of the character
        # If you were moved to a room by another player (do not have to move)
        self.moved_to = False

    def __repr__(self):
        return f"Character({self.name})"

    def jsonify(self):
        """
        Convert the Character object to a dictionary that can be serialized into JSON.
        """
        return {
            'name': self.name,
            'location': self.location.jsonify(),
            'homeSquare': self.homeSquare.jsonify(),
            'moved_to': self.moved_to,
        }
