import enum

class Sex(enum.Enum):
    female = 0
    male = 1

class Type(enum.Enum):
    counting = 'counting'
    count_down = 'count_down'
    