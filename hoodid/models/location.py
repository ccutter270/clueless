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

    