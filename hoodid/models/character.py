from hoodid.models.card import Card
from hoodid.models.location import Location

class Character(Card):
    
    name: str
    location: Location
    homeSquare: Location

    def __init__(self, name: str, location: Location, homeSquare: Location) -> None:
        self.name = name
        self.location = location
        self.homeSquare = homeSquare