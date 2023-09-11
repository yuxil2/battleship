from src.board import Board
from src.config import NodeStatus
from src.user_interface import UserInterface

class Round:
    """
    Represents a round of the game with functionalities for initializing the game and playing a round.
    A round is won when a player sinks all ships of all other players.
    """
    def __init__(self, players, ship_counts):
        """
        Initialize a round with players and ship counts.
        
        Args:
        players (list): list of Player objects.
        ship_counts (dict): {ShipConfig: count}
        """
        self.ui = UserInterface()
        self.players = players
        self.ship_counts = ship_counts
        self.board_size = None
        self.initialize()

    def initialize(self):
        """
        Initialize the ships and boards for players.
        """
        self.board_size = self.ui.ask_board_size()

        # create board for players
        for player in self.players:
            board = Board(*self.board_size)
            player.assign_board(board)

        # Add ships to players
        for player in self.players:
            player.add_ships(self.ship_counts)

        # Player ship placement
        for player in self.players:
            player.place_ships(self.ui)

    def play(self):
        """
        Play a round of the game.

        Returns:
        Player: the winning player.
        """
        # Loop until a player wins
        while True: 
            # Loop through players
            for player in self.players:
                # Skip the player if all ships are sunk
                if not player.has_ships_left():
                    continue

                # Get available target players
                target_players = [
                    p for p in self.players
                    if p != player and p.has_ships_left()
                ]
                
                # Loop until the player makes a valid hit
                is_finshed_hit = False
                while not is_finshed_hit: 
                    # Ask for target player and coordinates
                    target_for_hit = self.ui.ask_target_for_hit(player.player_id, target_players)
                    x, y = self.ui.ask_coordinates_for_hit(target_for_hit.board)

                    # Check if the hit isn't in a hitted place
                    if target_for_hit.board.is_valid_hit(x, y):
                        # Update the status of the node and the ship
                        is_finshed_hit = True
                        target_node = target_for_hit.board.grid[x][y]
                        target_ship_id = target_node.ship_id

                        # Check if the hit is in an empty place or an occupied place
                        if not target_ship_id: # If the node is empty, show empty hit
                            target_node.status = NodeStatus.HITTED_EMPTY
                            self.ui.show_empty_hit()
                        else: # If the node is occupied, show hit ship
                            target_node.status = NodeStatus.HITTED_OCCUPIED
                            target_ship = target_for_hit.ships[target_ship_id]
                            target_ship.hit()

                            # Check if the ship is sunk. If so, remove the ship from the player's fleet
                            if target_ship.is_alive():
                                self.ui.show_hit_ship()
                            else:
                                target_for_hit.remove_ship(target_ship.ship_id)
                                self.ui.show_ship_destroyed(target_ship)
                    else:
                        # If the hit is in a hitted place, show invalid hit
                        self.ui.inform_invalid_placement()

                # Check if the player wins
                # If all target players have no ships left, the player wins
                if not any(target_player.has_ships_left() for target_player in target_players):
                    self.ui.show_winner(player)
                    return player

    def reset(self):
        """
        Reset the game for another round.
        """
        # For extendability
        # Logic to reset the game state, boards, ships, etc.
        pass