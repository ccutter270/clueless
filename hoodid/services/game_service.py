from models.player import Player
from models.game import Game
from config import Config
from typing import List

class GameService:

    """

    Game Serivce

    """

    game = Game()
    players = List[Player]

    def __init__(self):
        self.players: List[Player] = []


    
    def add_player(self, character):
        """ Add a player to the game """
        if len(self.players) >= 6:
            return {"message": "Maximum number of players reached."}

        # Ensure the character is unique
        if any(player.character == character for player in self.players):
            return {"message": f"Character {character} is already taken."}

        # Assign a unique player ID
        player_id = len(self.players) + 1
        player = Player(player_id, character)
        self.players.append(player)
        print({"message": f"Player {player_id} added as {character}!", "player": player.get_player_info()})
        print(self.players)
        return {"message": f"Player {player_id} added as {character}!", "player": player.get_player_info()}




    def start_game(self):

        if len(self.players) < 3:
            return {"message": "Need at least 3 players to start the game!"}


        # When starting game, deal cards to players
        hands = self.game.cards.deal_cards(num_players=len(self.players))
        for i, player in enumerate(self.players):
            player.cardsList = hands[i]
        
        # Then add players to the Game class
        self.game.players = self.players

        # Start game
        return self.game.start_game()

    def get_game_state(self):

        return {
    "character": [
        {
            "name": "Professor Plum",
            "location": {
                "name": "Kitchen",
                "locationType": "Room",
                "connectedLocations": [],
                "occupied": True,
                "weapon": {
                    "name": "Wrench"
                }
            },
            "homeSquare": {
                "name": "Kitchen",
                "locationType": "Room",
                "connectedLocations": [],
                "occupied": True,
                "weapon": {
                    "name": "Wrench"
                }
            }
        }
    ],
    "currentTurn": "Professor Plum",
    "lastActionTaken": {
        "type": "Action",
        "message": "Someone moved somewhere."
    }
}
