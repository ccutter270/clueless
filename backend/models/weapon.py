class Weapon():

    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self):
        return f"Weapon({self.name})"

    def jsonify(self):
        """
        Convert the Weapon object to a dictionary.
        """
        return {
            'name': self.name,
        }
