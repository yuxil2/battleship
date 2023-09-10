from unittest.mock import patch
from src.user_interface import UserInterface
from src.config import MIN_BOARD_SIZE, MAX_BOARD_SIZE, ShipConfig, valid_choices

def test_ask_board_size_valid():
    with patch('builtins.input', side_effect=[str(MIN_BOARD_SIZE), str(MAX_BOARD_SIZE)]):
        m, n = UserInterface.ask_board_size()
        assert m == MIN_BOARD_SIZE
        assert n == MAX_BOARD_SIZE

def test_ask_board_size_invalid_then_valid():
    with patch('builtins.input', side_effect=['invalid', str(MIN_BOARD_SIZE - 1), str(MAX_BOARD_SIZE + 1), str(MIN_BOARD_SIZE), str(MAX_BOARD_SIZE)]):
        m, n = UserInterface.ask_board_size()
        assert m == MIN_BOARD_SIZE
        assert n == MAX_BOARD_SIZE

def test_get_valid_string():
    # Mocking input to simulate valid user choice
    with patch('builtins.input', side_effect=['invalid_choice', 'horizontal']):
        orientation = UserInterface.get_valid_string("Enter orientation (horizontal/vertical): ", valid_choices["orientation"])
        assert orientation == 'horizontal'

def test_get_valid_count_input():
    # Mocking input to simulate a valid ship count choice
    with patch('builtins.input', side_effect=['-1', 'invalid', '3']):
        count = UserInterface.get_valid_count_input(f"How many {ShipConfig.BATTLESHIP} do you want? ")
        assert count == 3
