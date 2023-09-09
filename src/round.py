from src import user_interface
from src.player import Player
from src.board import Board
from src.user_interface import UserInterface
from src.config import NodeStatus, ShipConfig
from typing import List, Dict

class Round:
    def __init__(self, players: List[Player], ship_counts: Dict[ShipConfig, int]):
        self.ui = UserInterface()
        self.players = players
        self.ship_counts = ship_counts
        self.board_size = None
        self.initialize()

    def initialize(self):
        self.board_size = self.ui.ask_board_size()
        # create board for players
        for player in self.players:
            board = Board(self.board_size)
            player.assign_board(board)

        # Add ships to players
        for player in self.players:
            player.add_ships(self.ship_counts)

        # Player ship placement phase
        for player in self.players:
            player.place_ships(self.ui)

    def play(self):
        # Main game loop
        while True:
            for player in self.players:
                if not player.has_ships_left:
                    continue

                print(f"{player}'s turn to hit!")

                target_players = [
                    p for p in self.players
                    if p != player and p.has_ships_left
                ]
                
                # TODO: implement ui - ask_target_for_hit, use get_valid_string to check must select from target_players
                # TODO: implement ui - ask_coordinates_for_hit
                is_finshed_hit = False
                while not is_finshed_hit:
                    target_for_hit = self.ui.ask_target_for_hit(self.player_id, target_players)
                    x, y = self.ui.ask_coordinates_for_hit()
                    if target_for_hit.board.is_valid_hit(x, y):
                        is_finshed_hit = True
                        target_node = target_for_hit.board.grid[x][y]
                        target_ship_id = target_node.ship_id
                        if not target_ship_id:
                            target_node.status = NodeStatus.HITTED_EMPTY
                            # TODO: implement ui - show_empty_hit
                        else:
                            target_node.status = NodeStatus.HITTED_OCCUPIED
                            target_ship = target_for_hit.ships[target_ship_id]
                            target_ship.hit()
                            # TODO: implement ui - show_hit_ship
                            if not target_ship.is_alive():
                                player.remove_ship(target_ship.ship_id)
                                # TODO: implement ui - show_ship_destroyed
                    else:
                        self.ui.inform_invalid_placement()

                # If all ships of a target player are sunk, the other player wins
                if not any(target_player.has_ships_left() for target_player in target_players):
                    # TODO: implement ui - show_winner
                    # TODO: return this winner player_id to Game
                    return

    def reset(self):
        """Reset the game for another round."""
        # Logic to reset the game state, boards, ships, etc.
        pass
