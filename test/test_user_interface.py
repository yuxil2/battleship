from src.user_interface import UserInterface
from src.config import MAX_BOARD_SIZE, MIN_BOARD_SIZE, valid_choices
from src.ship import Ship
from src.board import Board

# 1. Test for inform_round_number
def test_inform_round_number(mocker):
    mocker.patch('builtins.print')
    UserInterface.inform_round_number(5)
    print.assert_called_once_with("\n*** Round 5 ***\n")

# 2. Test for _ask_dimension_input with invalid input followed by valid input
def test_ask_dimension_input_invalid_then_valid(mocker):
    mocker.patch('builtins.input', side_effect=['invalid', '5', '30', '12'])
    result = UserInterface._ask_dimension_input("height")
    assert result == 12

# 3. Test for _ask_coordinate_input with valid input
def test_ask_coordinate_input_valid(mocker):
    mocker.patch('builtins.input', return_value='3')
    result = UserInterface._ask_coordinate_input("X", 5, "placing")
    assert result == 3

# 4. Test for ask_ship_placement
# def test_ask_ship_placement(mocker):
    # ship = Ship("P1_small_1", "P1", "small")
    # board = Board(5, 5)
    # mocker.patch('builtins.input', side_effect=['2', '3', 'horizontal'])
    # x, y, orientation = UserInterface.ask_ship_placement("P1", ship, board)
    # assert x == 2
    # assert y == 3
    # assert orientation == 'horizontal'

# 5. Test for get_valid_string with valid input
def test_get_valid_string_valid(mocker):
    mocker.patch('builtins.input', return_value='horizontal')
    response = UserInterface.get_valid_string("Enter orientation (horizontal/vertical): ", valid_choices["orientation"])
    assert response == 'horizontal'

# 6. Test for inform_invalid_placement
def test_inform_invalid_placement(mocker):
    mocker.patch('builtins.print')
    UserInterface.inform_invalid_placement()
    print.assert_called_once_with("Invalid placement. Please try again.")

# 7. Test for _ask_num_players with valid input
def test_ask_num_players_valid(mocker):
    mocker.patch('builtins.input', return_value='2')
    response = UserInterface._ask_num_players()
    assert response == 2

# 8. Test for _ask_continue_game with valid input
def test_ask_continue_game_valid(mocker):
    mocker.patch('builtins.input', return_value='yes')
    response = UserInterface._ask_continue_game()
    assert response == True

# 9. Test for get_player_id with valid input
def test_get_player_id_valid(mocker):
    mocker.patch('builtins.input', return_value='player1')
    response = UserInterface.get_player_id(1, set())
    assert response == 'player1'

# 10. Test for show_game_over
def test_show_game_over(mocker):
    mocker.patch('builtins.print')
    UserInterface.show_game_over()
    print.assert_called_once_with("\n*** Game over! Thanks for playing! :) ***\n")