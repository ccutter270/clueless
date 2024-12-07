from typing import List

from models.weapon import Weapon


class Location:

    name: str
    locationType: str
    connectedLocations: List['Location']
    occupied: bool
    weapon: Weapon

    def __init__(self, name: str, locationType: str) -> None:
        # The name of the location (e.g., "Kitchen", "Living Room")
        self.name = name
        # Type being "room" or "hallway"
        self.locationType = locationType
        # List of connected locations (rooms)
        self.connectedLocations: List['Location'] = []
        self.occupied = False
        self.weapon = None

    def __repr__(self):
        return f"Location({self.name})"

    def setOccupied(self, occupied: bool):
        """ Set occupied to true or false """
        self.occupied = occupied

    def isOccupied(self):
        return self.occupied

    def hasWeapon(self):
        return self.weapon is not None

    def setWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def jsonify(self):
        """
        Convert the Location object to a dictionary that can be serialized to JSON.
        """
        return {
            'name': self.name,
            'locationType': self.locationType,
            # Serialize each connected Location
            'connectedLocations': [location.name for location in self.connectedLocations],
            'occupied': self.occupied,
            # Serialize weapon if it exists
            'weapon': self.weapon.jsonify() if self.weapon else None,
        }
