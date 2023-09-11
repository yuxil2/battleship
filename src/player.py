from src.board import Board
from src.config import ShipConfig
from src.ship import Ship
from src.user_interface import UserInterface

class Player:
    """
    Represents a player in the game with functionalities for placing ships and tracking hits.
    """
    def __init__(self, player_id):
        """
        Initialize a player with a player ID.

        Args:
        player_id (str): ID of the player.
        """
        self.player_id = player_id
        self.ships = {}  # {ship_id: Ship object}
        self.board = None

    def __str__(self):
        """
        Return a string representation of the player.
        """
        return f"Player {self.player_id} (with {len(self.ships)} ships)"

    def assign_board(self, board: Board):
        """
        Assign a board to the player.

        Args:
        board (Board): board to be assigned.
        """
        self.board = board

    def add_ships(self, ship_counts):
        """
        Add ships to the player's fleet based on the passed config.
        
        Args:
        ship_counts (dict): {ShipConfig: count}
        """
        for ship_config, count in ship_counts.items():
            if not isinstance(ship_config, ShipConfig):  # Check if ship_config is an instance of ShipConfig
                raise ValueError(f"Invalid ship configuration provided: {ship_config}")
            for _ in range(count):
                ship_id = f"{self.player_id}_{ship_config.name}_{_}"  # Generating a unique ship ID
                self.ships[ship_id] = Ship(ship_id, self.player_id, ship_config)

    def remove_ship(self, ship_id):
        """
        Remove a destroyed ship from the player's fleet.

        Args:
        ship_id (str): ID of the ship to be removed.
        """
        if ship_id in self.ships:
            del self.ships[ship_id]

    def place_ships(self, user_interface: UserInterface):
        """
        Place the player's ships on the board.
        
        Args:
        user_interface (UserInterface): user interface to interact with the player.
        """
        for _, ship in self.ships.items(): # Place each ship in the fleet
            is_placed = False
            while not is_placed: # Keep asking for placement until a valid placement is made
                start_x, start_y, orientation = user_interface.ask_ship_placement(self.player_id, ship, self.board)
                if self.board.place_ship(start_x, start_y, ship, orientation):
                    is_placed = True
                else:
                    user_interface.inform_invalid_placement()

    def has_ships_left(self):
            """
            Check if the player still has undamaged ships.

            Returns:
            bool: True if the player still has undamaged ships, False otherwise.
            """
            return bool(self.ships)  