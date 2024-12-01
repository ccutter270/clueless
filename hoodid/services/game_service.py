from models.player import Player
from models.character import Character
from models.game import Game
from typing import List
import json

class GameService:

    """

    Game Serivce

    """

    game = Game()
    players = List[Player]

    def __init__(self):
        self.players: List[Player] = []


    
    def add_player(self, player: Player):
        """ Add a player to the game """
        if len(self.players) >= 6:
            return {"message": "Maximum number of players reached."}

        self.players.append(player)



    def start_game(self):

        if len(self.players) < 3:
            return {"message": "Need at least 3 players to start the game!"}

        # When starting game, deal cards to players
        hands = self.game.cards.deal_cards(num_players=len(self.players))
        for i, player in enumerate(self.players):
            player.cardsList = hands[i]
        
        # Then add players to the Game class
        self.game.players = self.players
        self.game.assign_player()

        # Start game
        return self.game.start_game()