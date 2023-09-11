import pytest
from src.ship import Ship
from src.board import Board
from src.config import ShipConfig
from src.player import Player
from src.user_interface import UserInterface

"""
Unit tests for the Player class.
It tests the methods of the Player class in isolation.
"""

def test_player_initialization():
    # Test the player is initialized with empty ships and no board
    player = Player(1)
    assert player.player_id == 1
    assert player.ships == {}
    assert player.board is None

def test_assign_board():
    # Test assigning a board to the player
    player = Player(1)
    board = Board(10, 10)
    player.assign_board(board)
    assert player.board == board

def test_add_ships():
    # Test adding a ship to the player
    player = Player(1)
    player.add_ships({ShipConfig.BATTLESHIP: 1})
    assert len(player.ships) == 1

    # Test the ship is initialized correctly
    for ship_id, ship in player.ships.items():
        assert ship_id == f"{player.player_id}_{ShipConfig.BATTLESHIP.name}_0"
        assert isinstance(ship, Ship)

def test_remove_ship():
    # Test removing a ship from the player
    player = Player(1)
    player.add_ships({ShipConfig.BATTLESHIP: 1})
    ship_id = list(player.ships.keys())[0]
    player.remove_ship(ship_id)
    assert len(player.ships) == 0

@pytest.mark.parametrize("initial_ships, has_ships_left", [(0, False), (1, True)])
def test_has_ships_left(initial_ships, has_ships_left):
    # Test the player has ships left
    player = Player(1)
    player.add_ships({ShipConfig.BATTLESHIP: initial_ships})
    assert player.has_ships_left() == has_ships_left

def test_place_ships(monkeypatch):
    # Assign a board to the player and ask the user for ship placement
    player = Player(1)
    player.assign_board(Board(10, 10))
    player.add_ships({ShipConfig.BATTLESHIP: 1})
    monkeypatch.setattr(UserInterface, "ask_ship_placement", lambda _, __, ___: (1, 1, 'horizontal'))
    
    # Place the ship
    player.place_ships(UserInterface)

    # Ensure ship is placed on the board
    assert player.board.grid[1][1].ship_id in player.ships