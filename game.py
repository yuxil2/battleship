from src.config import ShipConfig
from src.user_interface import UserInterface
from src.round import Round
from src.player import Player

class Game:
    def __init__(self):
        self.players = []
        self.rounds = []
        self.ship_configs = {}
    
    def reset_for_new_round(self):
        self.players = []
        self.ship_configs = {}

    def start(self):
        while True:
            UserInterface.inform_round_number(len(self.rounds) + 1)

            num_players = UserInterface._ask_num_players()

            player_ids = set()
            for i in range(1, num_players + 1):
                player_id = UserInterface.get_player_id(i, player_ids)
                if player_id not in player_ids:
                    player_ids.add(player_id)
                    self.players.append(Player(player_id))

            self.ship_configs = UserInterface._ask_ship_configs()
            
            round_obj = Round(self.players, self.ship_configs)
            self.rounds.append(round_obj)
            round_obj.play()

            if not UserInterface._ask_continue_game():
                break

            self.reset_for_new_round()
        
        UserInterface.show_game_over()

if __name__ == '__main__':
    game = Game()
    game.start()
