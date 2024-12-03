import random
from typing import List
from models.character import Character
from models.weapon import Weapon
from models.player import Player
from models.envelope import Envelope
from models.location import Location
from models.card import CardDeck
import json
from flask_socketio import SocketIO, emit
import time

class Game:

    """
    Game instance, starts game & initializes all variables

    """
    started: bool
    locations: List[Location]
    rooms: List[Location]
    weapons: List[Weapon]
    characters: List[Character]
    cards = CardDeck
    envelope: Envelope
    players = List[Player]
    currentTurn: int
    current_player: Player
    flow: str
    last_action_taken: str


    def __init__(self):
        self.started = False
        self.locations, self.rooms, self.characters = self._create_game()
        self.weapons = self._create_weapons()
        self.cards = CardDeck(self.characters, self.weapons, self.rooms)
        self.envelope = Envelope(random.choice(self.weapons), random.choice(self.characters), random.choice(self.rooms))
        self.players: List[Player] = []
        self.set_weapon_locations()
        self.currentTurn = 0
        self.flow = "Starting"
        self.current_player = None
        self.last_action_taken = "Initializing game"
        self.socketio = SocketIO  # Inject SocketIO instance
        
        # Play game variables that control the game flow
        self.action = None          # move, accuse, suggest
        self.move_to = None         # location to move to
        self.move_options = []      # Location options to move to
        self.suggestion = None      # Current suggestion


        
    def _create_game(self):
        
        #region Hallways
        ballroom_kitchen = Location("Ballroom to Kitchen", "hallway")
        billiard_ballroom = Location("Billiard to Ballroom", "hallway")
        billiard_dining = Location("Billiard to Dining", "hallway")
        conservatory_ballroom = Location("Conservatory to Ballroom", "hallway")
        dining_kitchen = Location("Dining to Kitchen", "hallway")
        hall_billiard = Location("Hall to Billiard", "hallway")
        hall_lounge = Location("Hall to Lounge", "hallway")
        library_billiard = Location("Library to Billiard", "hallway")
        library_conservatory = Location("Library to Conservatory", "hallway")
        lounge_dining = Location("Lounge to Dining", "hallway")
        study_hall = Location("Study to Hall", "hallway")
        study_library = Location("Study to Library", "hallway")
        #endregion Hallways

        #region Rooms
        ballroom = Location("Ballroom", "room")
        billiard_room = Location("Billiard Room", "room")
        conservatory = Location("Conservatory", "room")
        dining_room = Location("Dining Room", "room")
        hall = Location("Hall", "room")
        kitchen = Location("Kitchen", "room")
        library = Location("Library", "room")
        lounge = Location("Lounge", "room")
        study = Location("Study", "room")
        #endregion Rooms

        # Add connections to locations:
        
        #region Hallways Connected Locations
        ballroom_kitchen.connectedLocations = [ballroom, kitchen]
        billiard_ballroom.connectedLocations = [billiard_room, ballroom]
        billiard_dining.connectedLocations = [billiard_room, dining_room]
        library_billiard.connectedLocations = [library, billiard_room]
        library_conservatory.connectedLocations = [library, conservatory]
        lounge_dining.connectedLocations = [lounge, dining_room]
        study_hall.connectedLocations = [study, hall]
        study_library.connectedLocations = [study, library]
        conservatory_ballroom.connectedLocations = [conservatory, ballroom]
        dining_kitchen.connectedLocations = [dining_room, kitchen]
        hall_billiard.connectedLocations = [hall, billiard_room]
        hall_lounge.connectedLocations = [hall, lounge]
        #endregion Hallways Connected Locations

        #region Rooms Connected Locations
        ballroom.connectedLocations = [ballroom_kitchen, billiard_ballroom, conservatory_ballroom]
        billiard_room.connectedLocations = [billiard_dining, billiard_ballroom, hall_billiard, library_billiard]
        conservatory.connectedLocations = [conservatory_ballroom, library_conservatory, lounge]
        dining_room.connectedLocations = [dining_kitchen, billiard_dining, lounge_dining]
        hall.connectedLocations = [study_hall, hall_billiard, hall_lounge]
        kitchen.connectedLocations = [ballroom_kitchen, dining_kitchen, study]
        library.connectedLocations = [library_billiard, study_library, library_conservatory]
        lounge.connectedLocations = [hall_lounge, lounge_dining, conservatory]
        study.connectedLocations = [study_hall, study_library, kitchen]
        #endregion Rooms Connected Locations
        
        # Create List of all Locations: 
        locations = [
            ballroom_kitchen, billiard_ballroom, billiard_dining,
            conservatory_ballroom, dining_kitchen, hall_billiard,
            hall_lounge, library_billiard, library_conservatory,
            lounge_dining, study_hall, study_library,
            ballroom, billiard_room, conservatory, dining_room,
            hall, kitchen, library, lounge, study]

        # Create List of just rooms:
        rooms = [
            ballroom, 
            billiard_room, 
            conservatory, 
            dining_room, 
            hall, 
            kitchen, 
            library, 
            lounge, 
            study]

        #region Characters
        scarlet = Character("Miss Scarlet", hall_lounge, hall_lounge)
        hall_lounge.setOccupied(True)
        mustard = Character("Colonel Mustard", lounge_dining, lounge_dining)
        lounge_dining.setOccupied(True)
        white = Character("Mrs. White", ballroom_kitchen, ballroom_kitchen)
        ballroom_kitchen.setOccupied(True)
        green = Character("Mr. Green", conservatory_ballroom, conservatory_ballroom)
        conservatory_ballroom.setOccupied(True)
        peacock = Character("Mrs. Peacock", library_conservatory, library_conservatory)
        library_conservatory.setOccupied(True)
        plum = Character("Professor Plum", study_library, study_library)
        study_library.setOccupied(True)
        #endregion Characters

        # Create List of all characters:
        characters = [
            scarlet,
            mustard,
            white,
            green,
            peacock,
            plum
        ]

        return locations, rooms, characters

    def _create_weapons(self):
        """Create weapons used in the game"""

        candle_stick = Weapon("Candlestick")
        dagger = Weapon("Dagger")
        lead_pipe = Weapon("Lead Pipe")
        revolver = Weapon("Revolver")
        rope = Weapon("Rope")
        wrench = Weapon("Wrench")
        
        # Create List of all weapons:
        weapons = [
            candle_stick,
            dagger,
            lead_pipe,
            revolver,
            rope,
            wrench
        ]

        return weapons

    def _create_characters(self):
        return self.characters


    # Updates the players to point to character
    def assign_player(self):
        """Add a player to the game."""
        for player in self.players:
            player.character = next((obj for obj in self.characters if obj.name == player.character), None)

    
    def set_weapon_locations(self):
        """Place each weapon in a random room that does not already have a weapon"""
        
        for weapon in self.weapons:

            # Shuffle rooms to ensure randomness
            random.shuffle(self.rooms)

            # Find a room without a weapon
            for room in self.rooms:
                if not room.hasWeapon():
                    room.setWeapon(weapon) # Place the weapon in this room
                    print(f"{weapon.name} placed in {room.name}.")
                    break


    def next_turn(self):
        # Move to the next player's turn
        self.currentTurn = (self.currentTurn + 1) % len(self.players)

    
    def get_room_options(self, player: Player):

        room_options = []
        for location in player.character.location.connectedLocations:
            if location.locationType == "room":
                room_options.append(location.name)
            else:
                if not loction.isOccupied():
                    room_options.append(location.location.name)

        return room_options


    # TODO: if we move character, player moves as well? check this. Pointer to the object
    def move_player(self, character: Character, new_location: Location):

        # If in hallway currently, make sure to "unoccupy it"
        if character.location.locationType == "hallway":
            character.location.setOccupied(False)
        
        character.location = new_location           # Move character to new location
        new_location.setOccupied(True)              # Set Room to Occupied

        



    def accuse(self, player: Player, suspect: str, accused_weapon: str, accused_location: str):
        
        # Check if the accusation matches the solution
        if (suspect == self.envelope.suspect.name and
            accused_weapon == self.envelope.weapon.name and
            accused_location == self.solution.location):
                result = f"Player {player.character.name} wins! The solution was correct."
                return {"result": result, "correct": True}
                return True
        else:
            result = f"Player {player.character.name} lost! The solution was incorrect."
            return {"result": result, "correct": False}



    def get_game_state(self):

        if self.started:
            game_state = {
                "started": True,
                "flow": self.flow,
                "characters": {},
                "current_player": self.current_player.character.jsonify(),
                "lastActionTaken": {
                    "message": self.last_action_taken
                }
            }

            # Fill out current game state
            for character in self.characters:
                game_state["characters"][character.name] = character.jsonify()


        # Not started game state
        else:
            game_state = {
                "started": False,
                "flow": "Not Started",
                "current_player": "",
                "lastActionTaken": {
                    "message": self.last_action_taken
                }
            }


        # TODO: delete for debug
        # print(f"Game State: {json.dumps(game_state, indent=4)}")

        return game_state
  

    def send_game_state(self):
        emit('game_state', {'data': self.get_game_state()}, broadcast=True)

    def start_game(self):
        """Start the game loop (this can be expanded with turns and gameplay mechanics)."""

        self.started = True

        # TODO: delete, for testing
        print("Welcome to the Clue game!")
        print(f"The solution to the crime is: {self.envelope}")
        print(f"Players {self.players}")


        # TODO: make a boolean for players turn and move to next player when one of the players is done
        game_won = False
        # while not game_won:
        if True:

            # Set Current Player
            self.current_player = self.players[self.currentTurn]

            # Broadcast that its that Players Turn
            self.last_action_taken = self.current_player.character.name + "'s turn, choose your action"
            emit('game_state', {'data': self.get_game_state()}, broadcast=True)

            print("Made it here")

            # Wait for player to choose action
            while self.action is None:
                time.sleep(.5)


            if self.action == "move":

                self.action = None
                self.flow = "move"
                self.last_action_taken = self.current_player.character.name + " chose to move"
                emit('game_state', {'data': self.get_game_state()}, broadcast=True)

                
                # Get options that the player can move to
                if self.current_player.character.location.locationType == "hallway":
                    for location in self.current_player.character.location.connectedLocations:
                        self.move_options.append(location.name)
                    print(f"Hallway Options: {self.move_options}")

                elif self.current_player.character.location.locationType == "room":
                    self.move_options = self.get_room_options(self.current_player)
                    print(f"Room Options: {self.move_options}")

                
                else:
                    print("Error: This should be a room or a hallway but it is neither")

                
                # Broadcast move options for player
                emit('move_options', self.move_options, broadcast=True)
                
                # Wait for player to choose where to move to
                while self.move_to is None:
                    time.sleep(.5)

                # Get location instance
                location = next((location for location in self.locations if location.name == self.move_to), None)

                self.move_player(self.current_player.character, location)

                # Reset move options
                self.last_action_taken = self.current_player.character.name + " moved to " + self.current_player.character.location.name
                self.move_to = None
                self.move_options = []
               

                # If move to room, make a suggestion
                if self.current_player.character.location.locationType == "room":
                    self.action = "suggest"
                    self.flow = "suggest"
                
                self.send_game_state()

                # TODO: Make function that logs something without the game state being changed. Look where the logging happens

                
            if self.action == "suggest":

                self.action = None
                self.flow = "suggest"
                self.last_action_taken = self.current_player.character.name + " chose to suggest"
                self.send_game_state()
                
              

                # Wait for Suggestion - TODO start here with the form button
                while self.suggestion is None:
                    time.sleep(.5)

                # Move the character of the suggestion to the room & display
                character = next((character for character in self.characters if character.name == self.suggestion["character"]), None)
                print(self.current_player.character.location)
                print(character)
                self.move_player(character, self.current_player.character.location)
                self.last_action_taken = self.current_player.character.name + " suggested it was " + self.suggestion["character"] + " with the " + self.suggestion["weapon"] + " in the " + self.current_player.character.location.name
                self.send_game_state()

                # Check Sug
                print(f"Suggested.....")

                self.suggestion = None
                while self.suggestion is None:
                    time.sleep(.5)

            if self.action == "accuse":
                
                self.action = None

                accusation = self.prompt_player_accuse()
                accuse(accusation)  # TODO: make this take the JSON in? 
                
                print("accuse")
            
            


            # Handle Suggestions


            # Display 

            # # Simulate or get input for player's guess (for now, we randomly choose)
            # guess = self.make_player_guess(self.self.current_player)

            # # Display the guess (character, weapon, and location)
            # print(f"{self.self.current_player.character_name} guesses: {guess['character']} with the {guess['weapon']} in the {guess['location']}.")

            # # Check if the guess is correct
            # if self.make_guess(self.self.current_player, guess['character'], guess['weapon'], guess['location']):
            #     print(f"Correct! {self.self.current_player.character_name} wins!")
            #     return  # Game over, someone won.


            # print(f"Incorrect guess. Moving to the next player.")

            # Move to the next player's turn
            self.next_turn()


    def __repr__(self):
        return f"Game(Players: {self.players}, Crime Envelope: {self.envelope})"