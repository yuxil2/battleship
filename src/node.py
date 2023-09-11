from src.config import NodeStatus

class Node:
    """
    Represents a node on the board.
    The node can be empty or occupied by a ship.
    """
    def __init__(self):
        """
        Initialize a node with status EMPTY and no ship.
        """
        self.status = NodeStatus.EMPTY
        self.ship_id = None