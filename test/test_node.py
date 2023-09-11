from src.config import NodeStatus
from src.node import Node

"""
Unit test for the Node class.
"""

def test_node_initialization():
    # Test the node is initialized with empty status and no ship
    node = Node()
    assert node.status == NodeStatus.EMPTY
    assert node.ship_id is None