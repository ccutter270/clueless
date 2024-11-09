from typing import List
from hoodid.models.card import Card
from hoodid.models.character import Character
from hoodid.models.location import Location
from hoodid.models.weapon import Weapon

class Player:

    character: Character
    location: Location # Room or Location or Hallway?
    cardsList: List[Card]
    # Do we need a Hand attrib? or a list of cards
    # To show what the player has in "Hand"

    def __init__(self, character: Character, location: Location, cardsList: List[Card]) -> None:
        self.character = character
        self.location = location
        self.cardsList = cardsList