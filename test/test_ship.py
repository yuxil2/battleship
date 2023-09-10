from src.ship import Ship
from src.config import ShipConfig

def test_ship_initialization():
    ship = Ship("ship1", 1, ShipConfig.BATTLESHIP)
    assert ship.ship_id == "ship1"
    assert ship.player_id == 1
    assert ship.remaining_hits == ShipConfig.BATTLESHIP.length * ShipConfig.BATTLESHIP.width

def test_hit_and_is_alive():
    ship = Ship("ship1", 1, ShipConfig.BATTLESHIP)
    for _ in range(ShipConfig.BATTLESHIP.length * ShipConfig.BATTLESHIP.width - 1):
        ship.hit()
        assert ship.is_alive()
    ship.hit()
    assert not ship.is_alive()
