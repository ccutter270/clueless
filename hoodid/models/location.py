from typing import List
from hoodid.models.character import Character

class Location:

    label: str
    connectedLocations: List['Location']
    characters: List[Character]

    def __init__(self, label: str, connectedLocations: List['Location']) -> None:
        self.label = label
        self.connectedLocations = connectedLocations
        self.characters = None

    def isEmpty(self):
        return not self.characters or self.characters == []