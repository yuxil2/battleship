import pytest
from unittest.mock import patch
from game import Game

"""
Integration tests for the entire program.
It tests the game flow from start to finish and mocks the user input to simulate a real game.
It also tests the compenents of the game (e.g. Board, Ship, Player) in an integrated way.
"""

def test_game_integration():
    """
    Testing sceanrio:

    In a 20x20 board game involving three players named player1, player2, and player3, 
    each player placed their SUBMARINE vertically at positions (19, 2), (19, 4), and (19, 6) respectively. 
    In the first move, player1 targeted player2 and successfully hit player2's ship. 
    As a result of this strike, all of player2's ships were sunk. 
    Subsequently, player3 took their turn, targeting and hitting player1's ship. 
    With player1's ships also sunk, player3 emerged as the victor.
    """
    # Mocked user inputs for the game in the order they will be requested
    inputs = [
        '3',               # Number of players
        'player1',         # Player1 ID
        'player2',         # Player2 ID
        'player3',         # Player3 ID
        '0', '0', '0',     # BATTLESHIP, CRUISER, DESTROYER are 0
        '1',               # 1 Submarine
        '20', '20',        # Board size = 20x20
        '19', '2', 'vertical', # Player1 places SUBMARINE at (19,2) vertically
        '19', '4', 'vertical', # Player2 places SUBMARINE at (19,4) vertically
        '19', '6', 'vertical', # Player3 places SUBMARINE at (19,6) vertically
        'player2',         # Player1 targets Player2
        '19', '4',         # Player1 hits Player2's SUBMARINE
        'player1',         # Player3 targets Player1
        '19', '2',         # Player3 hits Player1's SUBMARINE
        'no'               # Do not continue the game
    ]
    
    # Store the output of the print function
    output = []
    def mock_print(*args, **kwargs):
        output.append(args[0])
    
    # Patch the built-in input and print functions
    with patch('builtins.input', side_effect=inputs):
        with patch('builtins.print', side_effect=mock_print):
            game = Game()
            game.start()

    # Assert game flow using the captured output
    assert "Congratulations Player player3 (with 1 ships)! You've won this round!" in ''.join(output)

@pytest.fixture(autouse=True)
def clear_game_data():
    # This will run before each test to ensure a fresh game state
    game = Game()
    game.reset_for_new_round()