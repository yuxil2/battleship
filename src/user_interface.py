from src.board import Board
from src.config import MAX_BOARD_SIZE, MIN_BOARD_SIZE, ShipConfig, valid_choices
from src.ship import Ship

class UserInterface: 
    @staticmethod
    def inform_round_number(round_num: int):
        """Inform the user about the round number."""
        print(f"\n*** Round {round_num} ***\n")

    @staticmethod
    def _ask_dimension_input(dimension_name: str) -> int:
        while True:
            try:
                value = int(input(f"Enter board {dimension_name} ({MIN_BOARD_SIZE}-{MAX_BOARD_SIZE}): "))
                if MIN_BOARD_SIZE <= value <= MAX_BOARD_SIZE:
                    return value
                else:
                    print("Invalid input. Please enter a number within the specified range.")
            except ValueError:
                print("Invalid input. Please enter a number within the specified range.")
                
    @staticmethod
    def ask_board_size():
        m = UserInterface._ask_dimension_input("height")
        n = UserInterface._ask_dimension_input("width")
        return m, n

    @staticmethod
    def _ask_coordinate_input(coordinate_name: str, max_value: int, action: str) -> int:
        """Ask the user for a coordinate input and ensure it's valid."""
        while True:
            try:
                prompt_msg = f"Enter {coordinate_name} coordinate for {action} (0-{max_value - 1}): "
                coord = int(input(prompt_msg))
                if 0 <= coord < max_value:
                    return coord
                else:
                    print(f"Invalid {coordinate_name} coordinate. Please enter a number between 0 and {max_value - 1}.")
            except ValueError:
                print(f"Invalid input. Please enter a valid integer for {coordinate_name} coordinate.")

    @staticmethod
    def ask_ship_placement(player_id: str, ship: Ship, board: Board):
        print(f"\nPlayer {player_id} - Placing {ship.config}. Please specify starting coordinate and orientation.")  
        x = UserInterface._ask_coordinate_input("X", board.m, "placing")
        y = UserInterface._ask_coordinate_input("Y", board.n, "placing")   
        orientation = UserInterface.get_valid_string("Enter orientation (horizontal/vertical): ", valid_choices["orientation"])
        return x, y, orientation

    @staticmethod
    def ask_ship_counts():
        ship_counts = {}
        for ship_config in ShipConfig:
            count = ShipConfig.get_valid_count_input(f"How many {ship_config} do you want? ")
            ship_counts[ship_config] = count
        return ship_counts
    
    @staticmethod
    def get_valid_count_input(prompt):
        while True:
            try:
                count = int(input(prompt))
                if count > 0:
                    return count
                else:
                    print("Invalid input. Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

    @staticmethod
    def get_valid_string(prompt: str, valid_choices: list) -> str:
        while True:
            response = input(prompt).lower().strip()
            if response in valid_choices:
                return response
            print(f"Invalid choice. Please choose from: {', '.join(valid_choices)}")

    @staticmethod
    def inform_invalid_placement():
        print("Invalid placement. Please try again.")

    @staticmethod
    def ask_target_for_hit(player_id: str, target_players: list()):
        player_ids = [p.player_id for p in target_players]
        print(f"Player {player_id}, choose your target!")
        print("Available targets: ", ', '.join(player_ids))
        target_id = UserInterface.get_valid_string("\nSelect target player_id: ", player_ids)
        return next(p for p in target_players if p.player_id == target_id)
    
    @staticmethod
    def ask_coordinates_for_hit(board: Board):
        x = UserInterface._ask_coordinate_input("X", board.m, action="hitting")
        y = UserInterface._ask_coordinate_input("Y", board.n, action="hitting")
        return x, y

    @staticmethod
    def show_empty_hit():
        print("\nMissed!\n")

    @staticmethod
    def show_hit_ship():
        print("\nHit!\n")

    @staticmethod
    def show_ship_destroyed(ship: Ship):
        print(f"\nHit! {ship.config} is destroyed!\n")

    @staticmethod
    def show_winner(player):
        print(f"\nCongratulations {player}! You've won this round!\n")

    @staticmethod
    def _ask_num_players() -> int:
        while True:
            try:
                num = int(input("Enter the number of players (at least 2): "))
                if num > 1:
                    return num
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input. Please enter a positive integer (at least 2): ")

    @staticmethod
    def _ask_ship_configs() -> dict:
        """Ask the players for their preferred ship configuration for the game."""
        ship_configs = {}
        print("Setting up ship configurations for the game...\n")
        for ship_config in ShipConfig:
            count = UserInterface.get_valid_count_input(f"How many {ship_config} do you want? ")
            ship_configs[ship_config] = count
        return ship_configs
    
    @staticmethod
    def _ask_continue_game() -> bool:
        """Ask the players if they want to continue the game."""
        while True:
            continue_game = input("Do you want to play another round? (yes/no) ")
            if continue_game.lower() in ['yes', 'no']:
                return continue_game.lower() == 'yes'
            print("Invalid input. Please answer with 'yes' or 'no'.")

    @staticmethod
    def get_player_id(i, existing_ids):
        while True:
            player_id = input(f"Enter ID for player {i}: ")
            if player_id not in existing_ids:
                return player_id
            else:
                print("This ID is already taken. Please choose another ID.")

    @staticmethod
    def show_game_over():
        print("\n*** Game over! Thanks for playing! :) ***\n")