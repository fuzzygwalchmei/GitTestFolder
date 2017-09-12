import tdl
import ConsoleConstants

class myObjects(object):
    #Create characters, monsters, items, etc
    def __init__(self):
        self.Class = "Hero"
        self.level = 1
        self.hitPoints = 15


class myRooms(object):
    #create rooms
    def __init__(self):
        self.rooms = 1

class myStats(object):
    #Stats for characters and monsters. Hp, Class, Level, Defence, Attack, etc
    def __init__(self):
        self.stats = 1
