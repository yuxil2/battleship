from src.node import Node
from src.config import NodeStatus

class Board:
    def __init__(self, m, n):
        self.grid = [[Node() for _ in range(n)] for _ in range(m)]
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
        return self.grid[y][x].status == NodeStatus.EMPTY

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
        return self.grid[y][x].status in [NodeStatus.EMPTY, NodeStatus.OCCUPIED]
