from src.user_interface import UserInterface
from src.config import MAX_BOARD_SIZE, MIN_BOARD_SIZE, valid_choices
from src.ship import Ship
from src.board import Board

"""
Unit tests for the UserInterface class.
It tests the input/output methods of the UserInterface class in isolation.
"""

def test_inform_round_number(mocker):
    # Test the round number is printed
    mocker.patch('builtins.print')
    UserInterface.inform_round_number(5)
    print.assert_called_once_with("\n*** Round 5 ***\n")

def test_ask_dimension_input_invalid_then_valid(mocker):
    # Test for _ask_dimension_input with invalid input followed by valid input
    mocker.patch('builtins.input', side_effect=['invalid', '5', '30', '12'])
    result = UserInterface._ask_dimension_input("height")
    assert result == 12

def test_ask_coordinate_input_valid(mocker):
    # Test for _ask_coordinate_input with invalid input followed by valid input
    mocker.patch('builtins.input', return_value='13')
    result = UserInterface._ask_coordinate_input("X", 15, "placing")
    assert result == 13

def test_ask_ship_placement(mocker):
    # Test the ship placement is asked and the coordinates and orientation are returned
    mocked_ship = mocker.Mock(spec=Ship)
    mocked_ship.config = "Test Ship"
    mocked_board = mocker.Mock(spec=Board)
    mocked_board.m = 10  # Assuming 10x10 board as an example
    mocked_board.n = 10

    # Simulate user input for x, y coordinates and orientation
    mocker.patch('src.user_interface.UserInterface._ask_coordinate_input', side_effect=[15, 16])
    mocker.patch('src.user_interface.UserInterface.get_valid_string', return_value="horizontal")

    # Call the method
    x, y, orientation = UserInterface.ask_ship_placement("player1", mocked_ship, mocked_board)

    # Assert the expected values are returned
    assert x == 15
    assert y == 16
    assert orientation == "horizontal"

    # Also you can assert if your methods were called with the expected arguments if needed
    UserInterface._ask_coordinate_input.assert_any_call("X", 10, "placing")
    UserInterface._ask_coordinate_input.assert_any_call("Y", 10, "placing")
    UserInterface.get_valid_string.assert_called_with("Enter orientation (horizontal/vertical): ", valid_choices["orientation"])

def test_get_valid_string_valid(mocker):
    # Test the valid string is returned
    mocker.patch('builtins.input', return_value='horizontal')
    response = UserInterface.get_valid_string("Enter orientation (horizontal/vertical): ", valid_choices["orientation"])
    assert response == 'horizontal'

def test_inform_invalid_placement(mocker):
    # Test the invalid placement message is printed
    mocker.patch('builtins.print')
    UserInterface.inform_invalid_placement()
    print.assert_called_once_with("Invalid placement. Please try again.")

def test_ask_num_players_valid(mocker):
    # Test the number of players is asked and the valid number is returned
    mocker.patch('builtins.input', return_value='2')
    response = UserInterface._ask_num_players()
    assert response == 2

def test_ask_continue_game_valid(mocker):
    # Test the continue game is asked and the valid response is returned
    mocker.patch('builtins.input', return_value='yes')
    response = UserInterface._ask_continue_game()
    assert response == True

def test_get_player_id_valid(mocker):
    # Test the player id is asked and the valid id is returned
    mocker.patch('builtins.input', return_value='player1')
    response = UserInterface.get_player_id(1, set())
    assert response == 'player1'

def test_show_game_over(mocker):
    # Test the game over message is printed
    mocker.patch('builtins.print')
    UserInterface.show_game_over()
    print.assert_called_once_with("\n*** Game over! Thanks for playing! :) ***\n")