from src.config import NodeStatus
from src.node import Node

def test_node_initialization():
    node = Node()
    assert node.status == NodeStatus.EMPTY
    assert node.ship_id is None