import json
import random
from typing import List

from models.character import Character
from models.location import Location
from models.weapon import Weapon


class Card:
    def __init__(self, name: str):
        # The name of the card (could be weapon, character, or room)
        self.name = name

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

    def remove_card(self, card):
        # Remove the given card from the deck
        self.deck = [c for c in self.deck if c != card]
