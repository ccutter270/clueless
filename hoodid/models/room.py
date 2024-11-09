from hoodid.models.card import Card
from hoodid.models.location import Location

class Room(Location, Card):
    
    def __init__(self) -> None:
        super().__init__()