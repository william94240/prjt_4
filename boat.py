
# Option 1 : Tout dans un même fichier (db.json)
# {
#   "players": [{}, {}],
#   "tournaments": []
# }

# Option 2 : Un fichier par élémente (players.json tournaments.json)
# [
#   {},
#   {}
# ]


# pip install rich
# https://github.com/Textualize/rich/blob/master/README.fr.md
import rich


class Boat:

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.crew = []

    def add_sailor(self, sailor):
        self.crew.append(sailor)
        sailor.boat = self

    def __str__(self):
        return f'{self.name} {self.speed} {self.crew}'

    def serialize(self):
        data = {
            'name': self.name,
            'speed': self.speed,
            'crew': [],

        }

        data['crew'] = [sailor.serialize() for sailor in self.crew]
        # for sailor in self.crew:
        #     data['crew'].append(sailor.serialize())

        return data

    @classmethod
    def deserialize(cls, data):
        boat = cls(data['name'], data['speed'])
        for sailor_data in data['crew']:
            sailor = Sailor.deserialize(sailor_data)
            boat.add_sailor(sailor)
        return boat


class Sailor:

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.boat = None

    def __str__(self):
        return "Sailor: " + self.name

    def __repr__(self):
        return f"Sailor: {self.name} {self.level}"

    def serialize(self):
        data = {
            'name': self.name,
            'level': self.level,
        }
        return data

    @classmethod
    def deserialize(cls, data):
        return cls(data['name'], data['level'])


bato = Boat('Bato', 5)
gromhak = Sailor('Gromhak', 42)
william = Sailor('William', 57)

bato.add_sailor(william)
bato.add_sailor(gromhak)


rich.print(gromhak.boat)


data = bato.serialize()
rich.print(data)


bato_bis = Boat.deserialize(data)
rich.print(bato_bis)

data_bis = bato_bis.serialize()
rich.print(data_bis)
