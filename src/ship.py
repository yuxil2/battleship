from src.config import ShipConfig

class Ship:
    """
    Represents a ship in the game with functionalities for tracking hits and checks if it's destroyed.
    """
    def __init__(self, ship_id, player_id, config: ShipConfig):
        """
        Initialize a ship with a ship ID, player ID, config, and remaining hits.
        """
        self.ship_id = ship_id
        self.player_id = player_id
        self.config = config
        self.remaining_hits = self.config.length * self.config.width

    def hit(self):
        """
        Register a hit on the ship and reduce the remaining hits by 1.
        """
        if self.remaining_hits > 0:
            self.remaining_hits -= 1

    def is_alive(self):
        """
        Check if the ship is still alive based on remaining hits.

        Returns:
        bool: True if the ship is still alive (has remaining hits), False otherwise.
        """
        return self.remaining_hits > 0