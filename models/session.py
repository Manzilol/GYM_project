class Session:

    def __init__(self, name, room, duration, capacity, difficulty, id = None):
        self.name = name
        self.room = room
        self.duration = duration
        self.capacity = capacity
        self.difficulty = difficulty
        self.id = id