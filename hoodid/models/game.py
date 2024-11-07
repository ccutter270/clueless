from typing import List
from hoodid.models.character import Character
from hoodid.models.weapon import Weapon
from hoodid.models.player import Player
from hoodid.models.envelope import Envelope
from hoodid.models.room import Room

class Game:

    envelope: Envelope #Do we need an envelope instance in Game? or do we fetch the envelope from somewhere else for comparison?
    players: List[Player]
    rooms: List[Room]
    weapons: List[Weapon]
    characters: List[Character]
    currentTurn: Player

    def __init__(self, envelope: Envelope, players: List[Player], rooms: List[Room], weapons: List[Weapon], characters: List[Character], currentTurn: Player) -> None:
        self.envelope = envelope
        self.players = players
        self.rooms = rooms
        self.weapons = weapons
        self.characters = characters
        self.currentTurn = currentTurn