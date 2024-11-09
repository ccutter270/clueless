from typing import List
from models.card import Card
from models.character import Character
from models.location import Location
from models.weapon import Weapon

class Player:

    playerID: int
    character: Character
    cardsList: List[Card]
    # Do we need a Hand attrib? or a list of cards
    # To show what the player has in "Hand"

    def __init__(self, playerID: int, character: Character, ) -> None:
        self.playerID = playerID        # Unique PlayerID
        self.character = character      # The character the player is controlling
        self.cardsList = []             # The list of cards the player has

    def __repr__(self):
        return f"Player({self.character}, {self.cardsList})"


    def move_to(self, new_location: Location):
        """ Move the player to a new location """
        if new_location in self.location.connected_locations:
            self.location = new_location
            print(f"{self.character.name} moved to {new_location.label}")
        else:
            print(f"{new_location.label} is not connected to {self.location.label}. Cannot move.")



    def get_player_info(self):
        return {
            "playerID": self.playerID,
            "character": self.character
        }