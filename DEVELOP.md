# Detailed Battleship Game Design Documentation

## Objective

Implement a creative version of the Battleship game, allowing multiple players to engage in a strategic naval combat scenario. The game is text-based, with players placing ships on their boards and taking turns to target and sink their opponent's ships.

## Tech Stack
* Language: This project is primarily developed in Python, leveraging its simplicity and extensive libraries for quick and efficient game development.
* User Interface: A text-based interface ensures easy interaction and engagement. Input prompts guide players through game setup and turns, with clear feedback on game outcomes.
* Testing: Unit Testing is implemented for validating the correctness of small, isolated pieces of functionality within the game. Integration Testing is implemented for ensuring that different components of the game (e.g., ship placement, combat mechanics, game state management) work seamlessly together as intended.
* Version Control: GitHub is used for code hosting and versioning. Facilitates contributions and ongoing development.

## Contribution Process
* For new feature development, please ensure code adheres to the project's current coding style.
* Before committing, run flake8 to ensure your code conforms to the project's style guidelines.
* Make sure to write unit tests for your new features, covering the main functionality. Utilize the pytest framework for testing.
* Once you push, GitHub Actions (if integrated in the project) will automatically start running the tests.


## Components

### Configurations (config.py)

- **MIN_BOARD_SIZE**: Minimum allowable dimension of the board. Ensures that the board has a reasonable size to place ships.
- **MAX_BOARD_SIZE**: Maximum allowable dimension of the board. Restricts the board from being overly large, making gameplay manageable.
- **valid_choices**: A dictionary that defines valid input choices for various scenarios like ship orientation (horizontal/vertical).

### NodeStatus Enum (config.py)

- **EMPTY**: Node has no ship.
- **OCCUPIED**: Node contains part of a ship.
- **HITTED_EMPTY**: An empty node that's been targeted and hit.
- **HITTED_OCCUPIED**: A node containing a ship that's been hit.

### ShipConfig Enum (config.py)

Describes different ship types. Each type has:

- **length**: Defines the length of the ship.
- **width**: Represents the width of the ship (usually 1, as ships are often 1 cell wide).
- **name**: A friendly descriptor of the ship's size/type (e.g., "small").

### Node (node.py)

Represents a cell on the board.

**Attributes**:

- **status**: Enum value indicating the node's status.
- **ship_id**: Holds the ship's ID if the node is occupied by a ship, or None if it's empty.

### Player (player.py)

Represents a participant.

**Attributes**:

- **player_id**: Unique identifier for the player.
- **ships**: Dictionary mapping ship IDs to their corresponding Ship objects.
- **board**: The board on which the player places ships and registers hits.

**Methods**:

- **assign_board**: Associates a board with the player.
- **add_ships**: Adds ships to the player's fleet.
- **remove_ship**: Removes a sunk ship.
- **place_ships**: Places the ships on the board.
- **has_ships_left**: Checks if any ships are still intact.

### Round (round.py)

Represents a single round/session.

**Attributes**:

- **ui**: Instance of the UserInterface, enabling interaction.
- **players**: List of participating players.
- **ship_counts**: Dict specifying the number of each ship type for the players.
- **board_size**: Tuple indicating board dimensions.

**Methods**:

- **initialize**: Prepares the game (board setup, ship addition, ship placement).
- **play**: The main gameplay loop, where players take turns targeting opponents.
- **reset**: Resets the game state for a new round.

### Ship (ship.py)

Represents ships that players deploy.

**Attributes**:

- **ship_id**: Unique identifier for each ship.
- **player_id**: Identifier of the ship's owner.
- **config**: The ship's configuration.
- **remaining_hits**: Number of hits the ship can take before sinking.

**Methods**:

- **hit**: Registers a hit on the ship.
- **is_alive**: Checks if the ship is still afloat.

### UserInterface (user_interface.py)

Text-based interface for user interaction.

**Methods**:

- **ask_board_size**: Gets board dimensions.
- **ask_ship_placement**: Gets ship placement details.
- **ask_ship_counts**: Queries the number of each ship type.
- **get_valid_count_input**: Validates input count.
- **get_valid_string**: Validates string choices.
- **inform_invalid_placement**: Notifies invalid placement.
- **ask_target_for_hit**: Gets the player's target.
- **ask_coordinates_for_hit**: Gets coordinates for attack.
- **show_empty_hit**: Indicates a miss.
- **show_hit_ship**: Indicates a successful hit.
- **show_ship_destroyed**: Shows a ship has been sunk.
- **show_winner**: Declares the winner of the round.

## Future Improvements

- **Enhanced Error Handling**: More robust error checks for all user inputs.
- **GUI Integration**: Implement a graphical user interface.
- **AI Player**: Introduce computer opponents with varied difficulty levels.
