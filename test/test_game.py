import pytest
from game import Game
from src.user_interface import UserInterface
from src.round import Round
from src.player import Player

@pytest.fixture
def game():
    return Game()

def test_game_initialization(game):
    assert isinstance(game.players, list)
    assert isinstance(game.rounds, list)
    assert isinstance(game.ship_configs, dict)

def test_reset_for_new_round(game):
    game.players = [Player("test_player")]
    game.ship_configs = {"test_config": 2}
    
    game.reset_for_new_round()
    
    assert not game.players
    assert not game.ship_configs

def test_start(mocker, game):
    mocker.patch.object(UserInterface, 'inform_round_number')
    mocker.patch.object(UserInterface, '_ask_num_players', return_value=2)
    mocker.patch.object(UserInterface, 'get_player_id', side_effect=["Player1", "Player2"])
    mocker.patch.object(UserInterface, '_ask_ship_configs', return_value={})
    mocker.patch.object(UserInterface, '_ask_continue_game', return_value=False)
    mocker.patch.object(UserInterface, 'show_game_over')
    mocker.patch.object(Round, 'play')
    mocker.patch('builtins.input', return_value='10')  # Mocking the input here
    game.start()

    assert len(game.players) == 2
    assert len(game.rounds) == 1