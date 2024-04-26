import rich


class Sailor:
    def __init__(self, name, level) -> None:
        self.name = name
        self.level = level
        self.boat = None

    def __str__(self) -> str:
        return "Sailor" + self.name

    def __repr__(self):
        return f"Sailor: {self.name} {self.level}"

    def serialize(self):
        data = {"name": self.name,
                "level": self.level
                }
        return data

    @classmethod
    def deserialize(cls, data):
        sailor = cls(data["name"], data["level"])
        return sailor


class Boat:
    def __init__(self, name: str, speed: int) -> None:
        self.name = name
        self.speed = speed
        self.crew = []

    def __str__(self) -> str:
        return f"{self.name} {self.speed} {self.crew}"

    def add_sailor(self, sailor: Sailor):
        self.crew.append(sailor)
        # sailor.boat = self

    def serialize(self):
        data = {
            "name": self.name,
            "speed": self.speed,
            "crew": []
        }

        data["crew"] = [sailor.serialize() for sailor in self.crew]
        return data

    @classmethod
    def deserialize(cls, data):
        boat = Boat(data["name"], data["speed"])
        for sailor_data in data["crew"]:
            sailor = Sailor.deserialize(sailor_data)
            boat.add_sailor(sailor)
        return boat


bato = Boat('Bato', 5)
gromhak = Sailor('Gromhak', 42)
william = Sailor('William', 57)

bato.add_sailor(william)
bato.add_sailor(gromhak)

# rich.print(gromhak.boat)

data = bato.serialize()
rich.print(data)

bato_bis = Boat.deserialize(data)
rich.print(bato_bis)

data_bis = bato_bis.serialize()
rich.print(data_bis)
