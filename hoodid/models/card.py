from models.weapon import Weapon
from models.character import Character
from models.location import Location
from typing import List
import random
import json


class Card:
    def __init__(self, name: str):
        self.name = name  # The name of the card (could be weapon, character, or room)

    def __repr__(self):
        return f"Card({self.name})"


class CardDeck:

    """ Deck of Game Cards"""

    suspects: List[Character]
    weapons: List[Weapon]
    rooms: List[Location]

    def __init__(self, suspects: List[Character], weapons: List[Weapon], rooms: List[Location]) -> None:
        self.suspects = suspects
        self.weapons = weapons
        self.rooms = rooms
        self.deck = suspects + weapons + rooms


    def deal_cards(self, num_players: int):
        """Shuffle the deck and deal cards to the specified number of players"""
        
        # Shuffle the deck
        random.shuffle(self.deck)
        
        # Create an empty list to store each player's hand
        hands = [[] for _ in range(num_players)]
        
        # Distribute the cards to players
        for i, card in enumerate(self.deck):
            player_index = i % num_players
            # Create Card object
            card_object = card.name
            hands[player_index].append(card_object)
        
        return hands

