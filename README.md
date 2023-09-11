# Battleship Game[🚢](https://emojipedia.org/zh/%E8%88%B9/)

You and your opponents are competing navy commanders at sea. You have a fleet of ships positioned at secret coordinates and take turns firing torpedoes at each other. The goal is to be the last to survive while sinking other person’s whole fleet.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

- Python (version 3.x recommended)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yuxil2/battleship.git
   ```

### Navigate to the game directory:

```sh
	cd battlegame
```

### Run the game:

```sh
	python game.py
```

## How to Play

* Each player will start by positioning their ships on their board.
* Players will then take turns choosing a target coordinate on the opponent's board to attack.
* The game will notify players if their hit was successful, missed, or sank an opponent's ship.
* The game ends when all the ships of a player are sunk, declaring the other player the winner.
* For detailed game rules, refer to the Game Design Documentation.

For detailed game rules, refer to the [Game Design Documentation](https://chat.openDesign documentation.mdai.com/c/link_to_documentation_if_available).

## Features

* Text-based user interface for easy interaction.
* Dynamic board sizes and ship configurations.
* Engaging gameplay with hits, misses, and sunk notifications.

## Game Flow

* Initialization: Define configurations, instantiate players, and initiate a game round.
* Setup Phase: Decide board dimensions, add ships to fleets, and position ships on the board.
* Combat Phase: Players take turns, select targets, and register hits or misses.
* Endgame Phase: Declare the winner and provide an option to play another round.

## Future Improvements

* GUI Integration: Implement a graphical user interface.
* Scoring System: Add a scoring mechanism for multi-round games.
