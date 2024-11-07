from typing import List
from hoodid.models.character import Character
from hoodid.models.location import Location
from hoodid.models.weapon import Weapon

class Player:

    character: Character
    location: Location # Room or Location or Hallway?
    # How do we keep track of suggestions, accusations, etc.
    # Maybe a suggestions history per player?
    locationsKnown: List[Location]
    weaponsKnown: List[Weapon]
    charactersKnown: List[Character]
    # Do we need a Hand attrib? or a list of cards
    # To show what the player has in "Hand"

    def __init__(self, character: Character, location: Location, locationsKnown: List[Location], weaponsKnown: List[Weapon], charactersKnown: List[Character]) -> None:
        self.character = character
        self.location = location
        self.locationsKnown = locationsKnown
        self.weaponsKnown = weaponsKnown
        self.charactersKnown = charactersKnown