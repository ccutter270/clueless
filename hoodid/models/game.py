import random
from typing import List
from models.character import Character
from models.weapon import Weapon
from models.player import Player
from models.envelope import Envelope
from models.location import Location
from models.card import CardDeck

class Game:

    """
    Game instance, starts game & initializes all variables

    """

    locations: List[Location]
    rooms: List[Location]
    weapons: List[Weapon]
    characters: List[Character]
    cards = CardDeck
    envelope: Envelope
    players = List[Player]
    currentTurn: Player
    
    def __init__(self):
        self.locations, self.rooms, self.characters = self._create_game()
        self.weapons = self._create_weapons()
        self.cards = CardDeck(self.characters, self.weapons, self.rooms)
        self.envelope = Envelope(random.choice(self.weapons), random.choice(self.characters), random.choice(self.rooms))
        self.players: List[Player] = []
        self.set_weapon_locations()


        
    def _create_game(self):
        
        #region Hallways
        ballroom_kitchen = Location("Ballroom to Kitchen", "hallway")
        billiard_ballroom = Location("Billiard Room to Ballroom", "hallway")
        billiard_dining = Location("Billiard Room to Dining Room", "hallway")
        conservatory_ballroom = Location("Conservatory to Ballroom", "hallway")
        dining_kitchen = Location("Dining Room to Kitchen", "hallway")
        hall_billiard = Location("Hall to Billiard Room", "hallway")
        hall_lounge = Location("Hall to Lounge", "hallway")
        library_billiard = Location("Library to Billiard Room", "hallway")
        library_conservatory = Location("Library to Conservatory", "hallway")
        lounge_dining = Location("Lounge to Dining Room", "hallway")
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

        candle_stick = Weapon("Candle Stick")
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


    # TODO: Update with actual players
    def add_player(self, player: Player):
        """Add a player to the game."""
        if len(self.players) < 6:
            self.players.append(player)
        else:
            raise ValueError("Maximum number of players reached.")

    
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

        
    def get_game_state(self):
        # TODO: Fill in game state JSON
        return 0


    def start_game(self):
        """Start the game loop (this can be expanded with turns and gameplay mechanics)."""

        # TODO: Exampnd this to have game play mechanics
        print("Welcome to the Clue game!")
        print(f"The solution to the crime is: {self.envelope}")

    def __repr__(self):
        return f"Game(Players: {self.players}, Crime Envelope: {self.envelope})"