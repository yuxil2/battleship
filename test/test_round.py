from src.round import Round
from src.player import Player
from src.config import ShipConfig


def mock_ask_board_size(_):
    return 10, 10

def mock_input_for_coordinates(prompt):
    if "X" in prompt:
        return "0"
    elif "Y" in prompt:
        return "1"
    elif "orientation" in prompt:
        return "horizontal"
    else:
        raise ValueError("Unexpected prompt")

def mock_ask_ship_placement(_, player_id, ship, board):
    return 0, 1, "horizontal"


def mock_ask_ship_counts():
    return {ShipConfig.BATTLESHIP: 1}


def test_round_initialization(monkeypatch):
    # Mock user interactions
    monkeypatch.setattr("src.user_interface.UserInterface.ask_board_size", mock_ask_board_size)
    monkeypatch.setattr("builtins.input", mock_input_for_coordinates)
    monkeypatch.setattr("src.user_interface.UserInterface.ask_ship_placement", mock_ask_ship_placement)
    monkeypatch.setattr("src.user_interface.UserInterface.ask_ship_counts", mock_ask_ship_counts)
    
    round_instance = Round([Player(1), Player(2)], {ShipConfig.BATTLESHIP: 1})

    # Basic checks to ensure the round has been initialized properly
    assert round_instance.players[0].player_id == 1
    assert round_instance.players[1].player_id == 2
    assert len(round_instance.players[0].ships) == 1
    assert len(round_instance.players[1].ships) == 1
