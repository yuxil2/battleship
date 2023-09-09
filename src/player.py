from src.ship import Ship
from src.config import ShipConfig
from uuid import uuid4

class Player:
    """
    Represents a player in the game.
    """
    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name
        self.ships = {}  # {ship_id: Ship object}
        self.board = None

    def assign_board(self, board):
        """Assign a board to the player."""
        self.board = board

    def add_ships(self, ship_configs):
        """
        Add ships to the player's fleet based on the passed config.
        :param ship_configs: A dict containing ShipConfig as key and count as value. Example: {ShipConfig.SMALL: 2}
        """
        for ship_config, count in ship_configs.items():
            if not isinstance(ship_config, ShipConfig):
                raise ValueError(f"Invalid ship configuration provided: {ship_config}")
            for _ in range(count):
                ship_id = uuid4()  # Generating a unique ship ID
                new_ship = Ship(ship_id=ship_id, player_id=self.player_id, config=ship_config)
                self.ships[ship_id] = new_ship

    def remove_ship(self, ship_id):
        """Remove a destroyed ship from the player's fleet."""
        if ship_id in self.ships:
            del self.ships[ship_id]

    def has_ships_left(self):
        """Check if the player still has undamaged ships."""
        return bool(self.ships)
