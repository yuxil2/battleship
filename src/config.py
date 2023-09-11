from enum import Enum, unique

# Board configurations
MIN_BOARD_SIZE = 10
MAX_BOARD_SIZE = 25

# Choices for user inputs, to validate against in UserInterface.get_valid_string()
valid_choices = {
    'orientation': ['horizontal', 'vertical'],
    'yes_no': ['yes', 'no'],
}

"""
Status of a node on the board.

EMPTY: the node is empty.
OCCUPIED: the node is occupied by a ship.
HITTED_EMPTY: the node is empty and has been hit.
HITTED_OCCUPIED: the node is occupied by a ship and has been hit.
"""
@unique
class NodeStatus(Enum):
    EMPTY = 1
    OCCUPIED = 2
    HITTED_EMPTY = 3
    HITTED_OCCUPIED = 4

"""
Type of a ship.

BATTLESHIP: length 4, width 1.
CRUISER: length 3, width 1.
DESTROYER: length 2, width 1.
SUBMARINE: length 1, width 1.
"""
@unique
class ShipConfig(Enum):
    BATTLESHIP = (4, 1, "Battleship")
    CRUISER = (3, 1, "Cruiser")
    DESTROYER = (2, 1, "Destroyer")
    SUBMARINE = (1, 1, "Submarine")

    @property
    def length(self):
        return self.value[0]

    @property
    def width(self):
        return self.value[1]

    def __str__(self):
        return f"{self.value[2]} with shape {self.value[0]} * {self.value[1]}"