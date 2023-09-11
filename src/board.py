from src.config import NodeStatus
from src.node import Node
from src.ship import Ship

class Board:
    """
    A fleet board for a player.
    Each player has their own board to place ships and track hits.
    """
    def __init__(self, m, n):
        """
        Initialize a board with m * n nodes.
        
        Args:
        m (int): number of rows.
        n (int): number of columns.
        """
        self.grid = [[Node() for _ in range(n)] for _ in range(m)] # 2D array of nodes
        self.m = m
        self.n = n

    def is_valid_position(self, x, y):
        """
        Check if a position is valid on the board.

        Args:
        x (int): x-coordinate of the node.
        y (int): y-coordinate of the node.

        Returns:
        bool: True if the position is valid, False otherwise.
        """
        return 0 <= x < self.m and 0 <= y < self.n

    def is_node_empty(self, x, y):
        """
        Check if a node at the given position is empty.
        
        Args:
        x (int): x-coordinate of the node.
        y (int): y-coordinate of the node.
        
        Returns:
        bool: True if the node is empty, False otherwise.
        """
        if not self.is_valid_position(x, y):
            return False
        return self.grid[x][y].status == NodeStatus.EMPTY

    def is_valid_hit(self, x, y):
        """
        Check if a hit is valid on the board.

        Args:
        x (int): x-coordinate of the node.
        y (int): y-coordinate of the node.

        Returns:
        bool: True if the hit is valid, False otherwise.
        """
        if not self.is_valid_position(x, y):
            return False
        return self.grid[x][y].status in [NodeStatus.EMPTY, NodeStatus.OCCUPIED]
    
    def place_ship(self, start_x: int, start_y: int, ship: Ship, orientation: str) -> bool:
        """
        Place a ship on the board.
        
        Args:
        start_x (int): x-coordinate of the starting node.
        start_y (int): y-coordinate of the starting node.
        ship (Ship): ship to be placed.
        orientation (str): orientation of the ship (horizontal/vertical).
        
        Returns:
        bool: True if the ship is placed successfully, False otherwise."""
        end_x, end_y = start_x, start_y

        # Calculate the ending position of the ship
        if orientation == "horizontal": # all ships has width 1
            end_y += ship.config.length - 1
        elif orientation == "vertical":
            end_x += ship.config.length - 1

        # Check if the ship can be placed on the board
        if not (self.is_valid_position(start_x, start_y) and self.is_valid_position(end_x, end_y)):
            return False

        nodes_to_place = []

        # Check if the nodes can place the ship
        if orientation == "horizontal":
            for i in range(ship.config.length):
                if not self.is_node_empty(start_x, start_y + i):
                    return False
                nodes_to_place.append((start_x, start_y + i))
        else:
            for i in range(ship.config.length):
                if not self.is_node_empty(start_x + i, start_y):
                    return False
                nodes_to_place.append((start_x + i, start_y))

        # All checks passed, place the ship
        for x, y in nodes_to_place:
            self.grid[x][y].status = NodeStatus.OCCUPIED
            self.grid[x][y].ship_id = ship.ship_id

        return True