import json
import copy
from typing import List

from flask_socketio import SocketIO, emit
from models.character import Character
from models.game import Game
from models.player import Player


class GameService:

    """

    Game Serivce

    """

    game: Game
    players: List[Player]
    started: bool

    def __init__(self):
        self.players = []
        self.game = Game()
        self.started = False

    def add_player(self, player: Player):
        """ Add a player to the game """
        if len(self.players) >= 6:
            return {"message": "Maximum number of players reached."}

        self.players.append(player)

    def remove_player(self, character: str):
        """ Remove a player from the game """
        if (len(self.players) > 0):

            # Remove player from game_service if game has not started
            if (self.started == False):
                self.players = [
                    p for p in self.players if p.character != character]

            # Remove players from game & game service if game has started
            else:
                self.players = [
                    p for p in self.players if p.character.name != character]
                self.game.remove_player(character)

                print("Player disconnectd")
                # If not players left, end game
                if len(self.game.players) == 0:
                    print("Should be ending game now")
                    emit('game_over', {
                        'message': "Disconnected"}, broadcast=True)

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
        self.started = True
        return self.game.start_game()

    def new_game(self):
        print("Should be starting new game")
        self.game = Game()
        self.started = False
        self.players = [Player(player.playerID, player.character.name)
                        for player in self.players]
