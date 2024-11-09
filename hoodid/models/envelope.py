from hoodid.models.weapon import Weapon
from hoodid.models.location import Location
from hoodid.models.player import Player

class Envelope:

    location: Location
    weapon: Weapon
    player: Player

    def __init__(self, location: Location, weapon: Weapon, player: Player) -> None:
        self.location = location
        self.weapon = weapon
        self.player = player