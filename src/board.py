from src.config import NodeStatus
from src.node import Node
from src.ship import Ship


class Board:
    def __init__(self, m, n):
        self.grid = [[Node() for _ in range(n)] for _ in range(m)] # m * n
        self.m = m
        self.n = n

    def is_valid_position(self, x, y):
        """
        Check if the given (x, y) coordinates are valid for this board.

        Args:
        x (int): x-coordinate of the node.
        y (int): y-coordinate of the node.

        Returns:
        bool: True if the position is valid, False otherwise.
        """
        return 0 <= x < self.m and 0 <= y < self.n

    def is_node_empty(self, x, y):
        """
        Check if a node at the given (x, y) coordinates is of status EMPTY.

        Args:
        x (int): x-coordinate of the node.
        y (int): y-coordinate of the node.

        Returns:
        bool: True if the node's status is EMPTY, False otherwise.
        """
        if not self.is_valid_position(x, y):
            return False
        return self.grid[x][y].status == NodeStatus.EMPTY

    def is_valid_hit(self, x, y):
        """
        Check if a node at the given position has not been hit.

        Args:
        x (int): x-coordinate of the node.
        y (int): y-coordinate of the node.

        Returns:
        bool: True if the node has not been hit, False otherwise.
        """
        if not self.is_valid_position(x, y):
            return False
        return self.grid[x][y].status in [NodeStatus.EMPTY, NodeStatus.OCCUPIED]
    
    def place_ship(self, start_x: int, start_y: int, ship: Ship, orientation: str) -> bool:
        """
        Try to place a ship on the specific coordinates with orientation.

        Args:
        x (int): starts from x-coordinate of the board.
        y (int): starts y-coordinate of the board.
        orientation (str): places the ship either vertically or horizontally

        Returns:
        bool: True if the ship has not been placed successfully, False otherwise.
        """
        end_x, end_y = start_x, start_y

        if orientation == "horizontal": # all ships has width 1
            end_y += ship.config.length - 1
        elif orientation == "vertical":
            end_x += ship.config.length - 1

        if not (self.is_valid_position(start_x, start_y) and self.is_valid_position(end_x, end_y)):
            return False

        nodes_to_place = []

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

        # If all checks passed, place the ship
        for x, y in nodes_to_place:
            self.grid[x][y].status = NodeStatus.OCCUPIED
            self.grid[x][y].ship_id = ship.ship_id

        return True
