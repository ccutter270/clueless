from hoodid.models.location import Location

class Character:
    
    name: str
    location: Location

    def __init__(self, name: str, location: Location) -> None:
        self.name = name
        self.location = location