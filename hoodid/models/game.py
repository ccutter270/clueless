import json
import random
import time
from typing import List, Any

from flask_socketio import SocketIO, emit
from models.card import CardDeck
from models.character import Character
from models.envelope import Envelope
from models.location import Location
from models.player import Player
from models.weapon import Weapon


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
    action: str
    move_to: Location
    move_options: List[Location]
    # i.e, suggestion = {"character": Professor Plum,"location": Study}
    suggestion: object
    disprove_finished: bool
    disproves: List[str]            # i.e, ["Candlestick", "Ballroom"]

    def __init__(self):
        self.started = False
        self.locations, self.rooms, self.characters = self._create_game()
        self.weapons = self._create_weapons()
        self.cards = CardDeck(self.characters, self.weapons, self.rooms)
        self.envelope = Envelope(random.choice(self.weapons), random.choice(
            self.characters), random.choice(self.rooms))
        self.players: List[Player] = []
        self.set_weapon_locations()
        self.currentTurn = 0
        self.flow = "Starting"
        self.current_player = None
        self.last_action_taken = "Initializing game"

        # Play game variables that control the game flow
        self.action = None              # move, accuse, suggest
        self.move_to = None             # location to move to
        self.move_options = []          # Location options to move to
        self.suggestion = None          # Current suggestion
        self.disprove_finished = False  # Waiting for disproof
        self.disproves = []             # Disproved cards from players

        # Remove envelope cards from card deck
        self.cards.remove_card(self.envelope.suspect)
        self.cards.remove_card(self.envelope.weapon)
        self.cards.remove_card(self.envelope.room)

    def _create_game(self):

        # region Starting
        scarlet_start = Location("Scarlet Start", "start")
        plum_start = Location("Plum Start", "start")
        mustard_start = Location("Mustard Start", "start")
        peacock_start = Location("Peacock Start", "start")
        green_start = Location("Green Start", "start")
        white_start = Location("White Start", "start")

        # endregion Starting

        # region Hallways
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
        # endregion Hallways

        # region Rooms
        ballroom = Location("Ballroom", "room")
        billiard_room = Location("Billiard Room", "room")
        conservatory = Location("Conservatory", "room")
        dining_room = Location("Dining Room", "room")
        hall = Location("Hall", "room")
        kitchen = Location("Kitchen", "room")
        library = Location("Library", "room")
        lounge = Location("Lounge", "room")
        study = Location("Study", "room")
        # endregion Rooms

        # Add connections to locations:

        # region Starting Connected Locations
        scarlet_start.connectedLocations = [hall_lounge]
        plum_start.connectedLocations = [study_library]
        mustard_start.connectedLocations = [lounge_dining]
        peacock_start.connectedLocations = [library_conservatory]
        green_start.connectedLocations = [conservatory_ballroom]
        white_start.connectedLocations = [ballroom_kitchen]
        # endregionStarting

        # region Hallways Connected Locations
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
        # endregion Hallways Connected Locations

        # region Rooms Connected Locations
        ballroom.connectedLocations = [
            ballroom_kitchen, billiard_ballroom, conservatory_ballroom]
        billiard_room.connectedLocations = [
            billiard_dining, billiard_ballroom, hall_billiard, library_billiard]
        conservatory.connectedLocations = [
            conservatory_ballroom, library_conservatory, lounge]
        dining_room.connectedLocations = [
            dining_kitchen, billiard_dining, lounge_dining]
        hall.connectedLocations = [study_hall, hall_billiard, hall_lounge]
        kitchen.connectedLocations = [ballroom_kitchen, dining_kitchen, study]
        library.connectedLocations = [
            library_billiard, study_library, library_conservatory]
        lounge.connectedLocations = [hall_lounge, lounge_dining, conservatory]
        study.connectedLocations = [study_hall, study_library, kitchen]
        # endregion Rooms Connected Locations

        # Create List of all Locations:
        locations = [scarlet_start, plum_start, mustard_start, peacock_start, green_start, white_start,
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

        # region Characters
        scarlet = Character("Miss Scarlet", scarlet_start, scarlet_start)
        scarlet_start.setOccupied(True)
        mustard = Character("Colonel Mustard", mustard_start, mustard_start)
        mustard_start.setOccupied(True)
        white = Character("Mrs. White", white_start, white_start)
        white_start.setOccupied(True)
        green = Character("Mr. Green", green_start,
                          green_start)
        green_start.setOccupied(True)
        peacock = Character(
            "Mrs. Peacock", peacock_start, peacock_start)
        peacock_start.setOccupied(True)
        plum = Character("Professor Plum", plum_start, plum_start)
        plum_start.setOccupied(True)
        # endregion Characters

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

    def assign_player(self):
        """Add a player to the game."""

        for player in self.players:
            player.character = next(
                (obj for obj in self.characters if obj.name == player.character), None)

    def remove_player(self, character: str):
        """Remove a player from the game."""
        self.players = [
            p for p in self.players if p.character.name != character]

    def set_weapon_locations(self):
        """Place each weapon in a random room that does not already have a weapon"""

        for weapon in self.weapons:

            # Shuffle rooms to ensure randomness
            random.shuffle(self.rooms)

            # Find a room without a weapon
            for room in self.rooms:
                if not room.hasWeapon():
                    room.setWeapon(weapon)  # Place the weapon in this room
                    break

    def next_turn(self):
        """Get the index of the next turn"""
        self.currentTurn = (self.currentTurn + 1) % len(self.players)

    def get_room_options(self, player: Player):
        """Get the options of rooms to move to"""
        room_options = []
        for location in player.character.location.connectedLocations:
            if location.locationType == "room":
                room_options.append(location.name)
            else:
                if not location.isOccupied():
                    room_options.append(location.name)

        return room_options

    def move_player(self, character: Character, new_location: Location):

        # If in hallway currently, make sure to "unoccupy it"
        if character.location.locationType == "hallway":
            character.location.setOccupied(False)

        character.location = new_location           # Move character to new location
        new_location.setOccupied(True)              # Set Room to Occupied

    def accuse(self, suspect: str, accused_weapon: str, accused_location: str):

        # Check if the accusation matches the solution
        if (suspect == self.envelope.suspect.name and
            accused_weapon == self.envelope.weapon.name and
                accused_location == self.envelope.room.name):

            return True
        else:
            return False

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

            # Fill out current characters
            for character in self.characters:
                game_state["characters"][character.name] = character.jsonify()

        # Game state for game not started
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

        game_over = False
        while not game_over:

            # Set Current Player - get next player whose still in game

            player_set = False
            for player in self.players:
                self.current_player = self.players[self.currentTurn]
                if self.current_player.lost:
                    self.next_turn()
                else:
                    player_set = True
                    break

            # TODO: all players lost the game... emit game lost message
            if not player_set:
                self.last_action_taken = "Game Over - nobody won! The solution was " + self.envelope.suspect.name + " did it with the " + self.envelope.weapon.name + \
                    " in the " + self.envelope.room.name
                emit('game_over', {
                     'message': self.last_action_taken}, broadcast=True)
                game_over = True
                self.started = False
                self.send_game_state()
                break
                # TODO: game_lost should message popup that all players lost, ask to start new game (refresh to beginning or keep current players?)

            # Broadcast that its that Players Turn
            self.flow = "get_action"
            self.last_action_taken = self.current_player.character.name + \
                "'s turn, choose your action"
            self.send_game_state()

            # Wait for player to choose action
            while self.action is None:
                time.sleep(.5)

            if self.action == "move":

                self.action = None
                self.flow = "move"
                self.last_action_taken = self.current_player.character.name + " chose to move"
                self.send_game_state()

                # Get options that the player can move to
                if self.current_player.character.location.locationType == "hallway":
                    for location in self.current_player.character.location.connectedLocations:
                        self.move_options.append(location.name)

                else:
                    self.move_options = self.get_room_options(
                        self.current_player)

                # Broadcast move options for player
                emit('move_options', self.move_options, broadcast=True)

                # Wait for player to choose where to move to
                while self.move_to is None:
                    time.sleep(.5)

                # Get location instance
                location = next(
                    (location for location in self.locations if location.name == self.move_to), None)

                self.move_player(self.current_player.character, location)

                # Reset move options
                self.last_action_taken = self.current_player.character.name + \
                    " moved to " + self.current_player.character.location.name
                self.move_to = None
                self.move_options = []

                # If move to room, make a suggestion
                if self.current_player.character.location.locationType == "room":
                    self.action = "suggest"
                    self.flow = "suggest"
                else:
                    # Ask if player want to accuse or move on to next turn
                    self.flow = "ask_accuse"
                    self.last_action_taken = "Move finished, asking for accusation or end turn"
                    self.send_game_state()

                    # Wait for response
                    while self.action == None:
                        time.sleep(.5)

                self.send_game_state()

                # TODO: Make function that logs something without the game state being changed. Look where the logging happens

            if self.action == "suggest":

                self.action = None
                self.flow = "suggest"
                self.last_action_taken = self.current_player.character.name + " chose to suggest"
                self.send_game_state()

                # Wait for Suggestion
                while self.suggestion is None:
                    time.sleep(.5)

                # Move the character of the suggestion to the room & display
                character = next(
                    (character for character in self.characters if character.name == self.suggestion["character"]), None)
                self.move_player(
                    character, self.current_player.character.location)
                self.last_action_taken = self.current_player.character.name + " suggested it was " + \
                    self.suggestion["character"] + " with the " + self.suggestion["weapon"] + \
                    " in the " + self.current_player.character.location.name
                self.send_game_state()

                # Emit suggestion so that players can disprove
                self.disprove_finished = False
                suggestion_data = {
                    "character": self.suggestion["character"],
                    "location": self.current_player.character.location.name,
                    "weapon": self.suggestion["weapon"]
                }
                emit('suggestion_made', {
                     'data': suggestion_data}, broadcast=True)

                # Wait for other players to disprove
                while self.disprove_finished == False:
                    time.sleep(.5)

                # Emit Disproves to display ONLY to user whose turn it is
                emit('show_disproves', {
                     'data': self.disproves}, broadcast=True)

                # Reset Suggestion variables
                self.disproves = []
                self.disprove_finished == False
                self.suggestion = None

                # Ask if player want to accuse or move on to next turn
                self.flow = "ask_accuse"
                self.last_action_taken = "Suggestion finished, asking for accusation or end turn"
                self.send_game_state()

                # Wait for response
                while self.action == None:
                    time.sleep(.5)

            if self.action == "accuse":

                self.action = None
                self.flow = "accuse"
                self.last_action_taken = self.current_player.character.name + " chose to accuse"
                self.send_game_state()

                # Suggestion & accusation form is the same
                while self.suggestion is None:
                    time.sleep(.5)

                # Check the accusation
                accusation_correct = self.accuse(
                    self.suggestion["character"], self.suggestion["weapon"], self.suggestion["location"])

                self.suggestion = None

                # TODO: Now that we have if the accusation is correct, do something
                if accusation_correct:
                    # TODO: create this logic
                    self.last_action_taken = "Game Over - " + self.current_player.character.name + " won! The solution was " + self.envelope.suspect.name + " did it with the " + self.envelope.weapon.name + \
                        " in the " + self.envelope.room.name

                    emit('game_over', {
                         'message': self.last_action_taken}, broadcast=True)
                    game_over = True
                    self.started = False
                    self.send_game_state()

                else:
                    # Player is out
                    self.current_player.lost = True

                    # If player is currently in hallway, move to one of connecting rooms:
                    if self.current_player.character.location.locationType == "hallway":
                        move_location = self.current_player.character.location.connectedLocations[
                            0]
                        self.move_player(
                            self.current_player.character, move_location)

                    # Popup message telling player they are out of the game
                    message = "Oh No! That is incorrect. You are out of the game. You may still disprove suggestions but you will no longer be able to win. The solution was: " + self.envelope.suspect.name + " did it with the " + self.envelope.weapon.name + \
                        " in the " + self.envelope.room.name
                    self.last_action_taken = self.current_player.character.name + \
                        " made a wrong accusation. They are out of the game!"
                    emit("player_lost", {'message': message}, broadcast=True)
                    self.send_game_state()

            # Done with loop, move to next players turn
            self.action = None
            self.last_action_taken = self.current_player.character.name + \
                " chose to end their turn"
            self.flow = "get_action"
            self.send_game_state()
            self.next_turn()

    def __repr__(self):
        return f"Game(Players: {self.players}, Crime Envelope: {self.envelope})"
