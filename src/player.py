from src.board import Board
from src.ship import Ship
from src.config import ShipConfig
from uuid import uuid4
from typing import Dict

from src.user_interface import UserInterface

class Player:
    """
    Represents a player in the game.
    """
    def __init__(self, player_id: int):
        self.player_id = player_id
        self.ships = {}  # {ship_id: Ship object}
        self.board = None

    def __str__(self):
        return f"Player {self.player_id} with {len(self.ships)} ships"

    def assign_board(self, board: Board):
        """Assign a board to the player."""
        self.board = board

    def add_ships(self, ship_counts: Dict[ShipConfig, int]):
        """
        Add ships to the player's fleet based on the passed config.
        :param ship_counts: A dict containing ShipConfig as key and count as value. Example: {ShipConfig.SMALL: 2}
        """
        for ship_config, count in ship_counts.items():
            if not isinstance(ship_config, ShipConfig):
                raise ValueError(f"Invalid ship configuration provided: {ship_config}")
            for _ in range(count):
                ship_id = f"{self.player_id}_{ship_config.name}_{_}"  # Generating a unique ship ID
                self.ships[ship_id] = Ship(ship_id, self.player_id, ship_config)

    def remove_ship(self, ship_id):
        """Remove a destroyed ship from the player's fleet."""
        if ship_id in self.ships:
            del self.ships[ship_id]

    def place_ships(self, user_interface: UserInterface):
        for _, ship in self.ships.items():
            is_placed = False
            while not is_placed:
                start_x, start_y, orientation = user_interface.ask_ship_placement(self.player_id, ship)
                if self.board.place_ship(start_x, start_y, ship, orientation):
                    is_placed = True
                else:
                    user_interface.inform_invalid_placement()

    def has_ships_left(self):
        """Check if the player still has undamaged ships."""
        return bool(self.ships)
