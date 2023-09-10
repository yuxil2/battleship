from enum import Enum, unique

# Board configurations
MIN_BOARD_SIZE = 10
MAX_BOARD_SIZE = 25

# Choices for user inputs, to validate against in UserInterface.get_valid_string()
valid_choices = {
    'orientation': ['horizontal', 'vertical'],
    'yes_no': ['yes', 'no'],
}

@unique
class NodeStatus(Enum):
    EMPTY = 1
    OCCUPIED = 2
    HITTED_EMPTY = 3
    HITTED_OCCUPIED = 4

@unique
class ShipConfig(Enum):
    # BATTLESHIP = (4, 1, "Battleship")
    # CRUISER = (3, 1, "Cruiser")
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
