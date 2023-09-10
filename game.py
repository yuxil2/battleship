from src.config import ShipConfig
from src.user_interface import UserInterface
from src.round import Round
from src.player import Player

class Game:
    def __init__(self):
        self.players = []
        self.rounds = []
        self.ship_configs = {}

    def _ask_num_players(self) -> int:
        while True:
            try:
                num = int(input("Enter the number of players (at least 2): "))
                if num > 1:
                    return num
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input. Please enter a positive integer (at least 2): ")

    def _ask_ship_configs(self) -> dict:
        """Ask the players for their preferred ship configuration for the game."""
        ship_configs = {}
        print("Setting up ship configurations for the game...\n")
        for ship_config in ShipConfig:
            count = UserInterface.get_valid_count_input(f"How many {ship_config} do you want? ")
            ship_configs[ship_config] = count
        return ship_configs
    
    def _ask_continue_game(self) -> bool:
        """Ask the players if they want to continue the game."""
        while True:
            continue_game = input("Do you want to play another round? (yes/no) ")
            if continue_game.lower() in ['yes', 'no']:
                return continue_game.lower() == 'yes'
            print("Invalid input. Please answer with 'yes' or 'no'.")

    def start(self):
        num_players = self._ask_num_players()

        player_ids = set()
        for i in range(1, num_players + 1):
            while True:
                player_id = input(f"Enter ID for player {i}: ")
                if player_id not in player_ids:
                    player_ids.add(player_id)
                    self.players.append(Player(player_id))
                    break
                else:
                    print("This ID is already taken. Please choose another ID.")

        self.ship_configs = self._ask_ship_configs()

        while True:
            round_obj = Round(self.players, self.ship_configs)
            self.rounds.append(round_obj)
            round_obj.play()

            # Ask and validate if players want to continue
            if not self._ask_continue_game():
                break

            # Reset ship configurations for the next round
            self.ship_configs = {}
            self._ask_ship_configs()
        
        print("Game over! Thanks for playing! :)")

if __name__ == '__main__':
    game = Game()
    game.start()
