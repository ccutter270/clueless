import json
from typing import List

from models.card import Card
from models.character import Character
from models.location import Location
from models.weapon import Weapon


class Player:

    playerID: int
    character: Character
    cardsList: List[Card]
    lost: bool

    def __init__(self, playerID: int, character: Character) -> None:
        self.playerID: int = playerID        # Unique PlayerID
        # The character the player is controlling
        self.character: Character = character
        # The lisst of cards the player has
        self.cardsList: List[Card] = []
        # If lost, set true
        self.lost = False

    def __repr__(self):
        return f"Player({self.character}, {self.cardsList})"

    def get_player_info(self):
        return {
            "playerID": self.playerID,
            "character": self.character
        }

    def jsonify_cards_list(self):
        # Convert cardsList to a JSON string
        return json.dumps([card for card in self.cardsList])
