from typing import List
from models.weapon import Weapon

class Location:

    name: str
    locationType: str
    connectedLocations: List['Location']
    occupied: bool
    weapon: Weapon

    def __init__(self, name: str, locationType: str) -> None:
        self.name = name                                    # The name of the location (e.g., "Kitchen", "Living Room")
        self.locationType = locationType                    # Type being "room" or "hallway"
        self.connectedLocations: List['Location'] = []      # List of connected locations (rooms)
        self.occupied = False
        self.weapon = None

    def __repr__(self):
        return f"Location({self.name})"

    def setOccupied(self, occupied: bool):
        """ Set occupied to true or false """
        self.occupied = occupied
    
    def isOccupied(self):
        return occupied

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
            'connectedLocations': [location.name for location in self.connectedLocations],  # Serialize each connected Location
            'occupied': self.occupied,
            'weapon': self.weapon.jsonify() if self.weapon else None,  # Serialize weapon if it exists
        }

    