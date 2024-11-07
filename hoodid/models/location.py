from typing import List

class Location:

    label: str
    connectedLocations: List['Location']

    def __init__(self, label: str, connectedLocations: List['Location']) -> None:
        self.label = label
        self.connectedLocations = connectedLocations