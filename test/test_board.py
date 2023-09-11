from src.board import Board
from src.config import MAX_BOARD_SIZE, MIN_BOARD_SIZE, NodeStatus
from src.ship import Ship
from src.config import ShipConfig

"""
Unit tests for the Board class.
It tests the methods of the Board class in isolation.
"""

def test_is_valid_position():
    board = Board(MIN_BOARD_SIZE, MAX_BOARD_SIZE)
    
    # Test valid position
    assert board.is_valid_position(0, 0) 

    # Test invalid position
    assert not board.is_valid_position(-1, 0) 
    assert not board.is_valid_position(0, MAX_BOARD_SIZE) 
    assert board.is_valid_position(MIN_BOARD_SIZE - 1, MAX_BOARD_SIZE - 1) 

def test_is_node_empty():
    # Test empty node
    board = Board(MIN_BOARD_SIZE, MAX_BOARD_SIZE)
    assert board.is_node_empty(0, 0)

    # Test occupied node
    board.grid[0][0].status = NodeStatus.OCCUPIED
    assert not board.is_node_empty(0, 0)

    # Test hitted node
    board.grid[0][0].status = NodeStatus.HITTED_EMPTY
    assert not board.is_node_empty(0, 0)

    # Test hitted occupied node
    board.grid[0][0].status = NodeStatus.HITTED_OCCUPIED
    assert not board.is_node_empty(0, 0)

def test_is_valid_hit():
    # Test valid hit
    board = Board(MIN_BOARD_SIZE, MAX_BOARD_SIZE)
    assert board.is_valid_hit(0, 0)

    # Test invalid hit
    board.grid[0][0].status = NodeStatus.OCCUPIED
    assert board.is_valid_hit(0, 0)

    # Test invalid hit
    board.grid[0][0].status = NodeStatus.HITTED_EMPTY
    assert not board.is_valid_hit(0, 0)

def test_place_ship():
    board = Board(MIN_BOARD_SIZE, MAX_BOARD_SIZE)
    ship = Ship("ship1", "player1", ShipConfig.BATTLESHIP)

    # Test placing the ship horizontally
    assert board.place_ship(0, 0, ship, "horizontal")
    assert board.grid[0][0].status == NodeStatus.OCCUPIED
    assert board.grid[0][1].status == NodeStatus.OCCUPIED

    # Test placing the ship vertically
    assert board.place_ship(2, 0, ship, "vertical")
    assert board.grid[2][0].status == NodeStatus.OCCUPIED
    assert board.grid[3][0].status == NodeStatus.OCCUPIED

    # Test invalid placement
    assert not board.place_ship(MIN_BOARD_SIZE - 1, MAX_BOARD_SIZE - 1, ship, "horizontal")
    assert not board.place_ship(MIN_BOARD_SIZE - 1, MAX_BOARD_SIZE - 1, ship, "vertical")
