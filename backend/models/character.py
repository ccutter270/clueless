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

    def set_location(self, location):
        """Sets the character's current location."""
        self.location = location

    def move_to(self, new_location: Location):
        """ Move the player to a new location """
        if new_location in self.location.connectedLocations:
            self.set_location(new_location)
            print(f"{self.name} moved to {new_location.name}")
        else:
            print(
                f"{new_location.name} is not connected to {self.location.name}. Cannot move.")

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
