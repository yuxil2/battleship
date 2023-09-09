from enum import Enum, unique

@unique
class NodeStatus(Enum):
    EMPTY = 1
    OCCUPIED = 2
    HITTED_EMPTY = 3
    HITTED_OCCUPIED = 4

@unique
class ShipConfig(Enum):
    SMALL = (1, 2)
    MEDIUM = (1, 3)
    LARGE = (2, 3)
    XLARGE = (2, 4)

    @property
    def length(self):
        return self.value[0]

    @property
    def width(self):
        return self.value[1]
