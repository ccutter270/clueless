from models.location import Location

class Character:
    
    name: str
    location: Location
    homeSquare: Location

    def __init__(self, name: str, location: 'Location', homeSquare: 'Location') -> None:
        self.name = name
        self.location = location        # Current location of the character
        self.homeSquare = homeSquare    # Starting location of the character

    def __repr__(self):
        return f"Character({self.name})"

    def set_location(self, location):
        """Sets the character's current location."""
        self.location = location