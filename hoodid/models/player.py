from typing import List
from models.card import Card
from models.character import Character
from models.location import Location
from models.weapon import Weapon

class Player:

    playerID: int
    character: Character
    cardsList: List[Card]

    def __init__(self, playerID: int, character: Character) -> None:
        self.playerID: int = playerID        # Unique PlayerID
        self.character: Character = character      # The character the player is controlling
        self.cardsList: List[Card] = []             # The list of cards the player has

    def __repr__(self):
        return f"Player({self.character}, {self.cardsList})"


    def move_to(self, new_location: Location):
        """ Move the player to a new location """
        if new_location in self.location.connectedLocations:
            self.location = new_location
            print(f"{self.character.name} moved to {new_location.name}")
        else:
            print(f"{new_location.name} is not connected to {self.location.name}. Cannot move.")



    def get_player_info(self):
        return {
            "playerID": self.playerID,
            "character": self.character
        }