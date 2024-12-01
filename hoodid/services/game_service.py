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

    def get_game_state(self):

        
        if self.game.started:

            game_state = {
                "started": True,
                "characters": {},
                "current_player": self.game.current_player.character.name,
                "lastActionTaken": {    # TODO: Update with real action
                    "type": "Action",
                    "message": "Someone moved somewhere. This is a Test Message."
                }
            }

            # Fill out current game state
            for character in self.game.characters:
                game_state["characters"][character.name] = character.jsonify()


        # TODO: make a game not started state
        else:
            game_state = {
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
                "current_player": "Mrs. White",
                "lastActionTaken": {
                    "type": "Action",
                    "message": "Someone moved somewhere. This is a Test Message."
                }
            }


        # TODO: delete for debug
        print(f"Game State: {json.dumps(game_state, indent=4)}")

        return game_state
