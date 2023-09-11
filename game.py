from src.config import ShipConfig
from src.user_interface import UserInterface
from src.round import Round
from src.player import Player

class Game:
    """
    Handles the game logic.
    A game has multiple rounds.
    Each round has a winner.
    """
    def __init__(self):
        """
        Initialize the game with empty players and rounds.
        """
        self.players = []
        self.rounds = []
        self.ship_configs = {}
    
    def reset_for_new_round(self):
        """
        Reset the game for a new round by clearing the players and ship configs.
        """
        self.players = []
        self.ship_configs = {}

    def start(self):
        """
        Start the game.
        """
        # Implement a new round until the user decides to stop
        while True:
            # inform users about the round number
            UserInterface.inform_round_number(len(self.rounds) + 1)


            num_players = UserInterface._ask_num_players() 

            # Ask the user for the player IDs and create the players
            player_ids = set()
            for i in range(1, num_players + 1):
                player_id = UserInterface.get_player_id(i, player_ids)
                if player_id not in player_ids:
                    player_ids.add(player_id)
                    self.players.append(Player(player_id))

            # Ask the user for the ship configurations
            self.ship_configs = UserInterface._ask_ship_configs()
            
            # Starts a new round
            round_obj = Round(self.players, self.ship_configs)
            self.rounds.append(round_obj)
            round_obj.play()

            # Ask the user if they want to continue playing. 
            if not UserInterface._ask_continue_game(): # If not, break the loop
                break
            self.reset_for_new_round() # Otherwise, reset the game for a new round
        
        # Game over
        UserInterface.show_game_over()

if __name__ == '__main__':
    game = Game()
    game.start()
