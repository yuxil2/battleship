from src.ship import Ship
from src.config import ShipConfig

"""
Unit tests for the Ship class.
It tests the methods of the Ship class in isolation.
"""

def test_ship_initialization():
    # Test the ship is initialized with the correct attributes
    ship = Ship("ship1", 1, ShipConfig.BATTLESHIP)
    assert ship.ship_id == "ship1"
    assert ship.player_id == 1
    assert ship.remaining_hits == ShipConfig.BATTLESHIP.length * ShipConfig.BATTLESHIP.width

def test_hit_and_is_alive():
    # Test hitting the ship and checking if it is alive
    ship = Ship("ship1", 1, ShipConfig.BATTLESHIP)
    for _ in range(ShipConfig.BATTLESHIP.length * ShipConfig.BATTLESHIP.width - 1):
        ship.hit()
        assert ship.is_alive()
    
    # Test hitting the ship and checking if it is dead
    ship.hit()
    assert not ship.is_alive()