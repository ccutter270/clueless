import json
from typing import List

from flask_socketio import SocketIO, emit
from models.character import Character
from models.game import Game
from models.player import Player


class GameService:

    """

    Game Serivce

    """

    game = Game()
    players = List[Player]

    def __init__(self):
        self.players: List[Player] = []
        self.game = Game()

    def add_player(self, player: Player):
        """ Add a player to the game """
        if len(self.players) >= 6:
            return {"message": "Maximum number of players reached."}

        self.players.append(player)

    def get_player_cards(self):

        # List containing player & their cards
        # i.e [["Professor Plum", [Card, Card, Card]], ["Colonel Mustard", [Card, Card, Card]]]
        player_cards = []

        # Fill out players cards
        for player in self.players:
            cards = []
            for card in player.cardsList:
                cards.append(card)

            player_cards.append([player.character.name, cards])

        return player_cards

    def start_game(self):

        if len(self.players) < 3:
            return {"message": "Need at least 3 players to start the game!"}

        # Get Solution
        # solution = self.game.envelope
        # print(f"Solution {solution}")
        # print(f"Deck cards size {self.game.cards.size}")

        # print(f"Deck cards size {self.game.cards.size}")

        # Take out solution cards from deck

        # When starting game, deal cards to players
        hands = self.game.cards.deal_cards(num_players=len(self.players))
        for i, player in enumerate(self.players):
            player.cardsList = hands[i]

        # Then add players to the Game class
        self.game.players = self.players
        self.game.assign_player()

        # Emit message to display player's cards on UI
        emit('display_cards', {
             'data': self.get_player_cards()}, broadcast=True)

        # Set Game State
        self.game.last_action_taken = "The game is starting!"
        self.game.current_player = self.players[0]
        emit('game_state', {
             'data': self.game.get_game_state()}, broadcast=True)

        # Start game
        return self.game.start_game()
