# Battleship Game 🚢

You and your opponents are competing navy commanders at sea. You have a fleet of ships positioned at secret coordinates and take turns firing torpedoes at each other. The goal is to be the last to survive while sinking other person’s whole fleet.

## Development Guide

Interested in contributing or diving deeper into the design? Check out [DEVELOP.md](https://github.com/yuxil2/battleship/blob/main/DEVELOP.md) for a comprehensive overview of the object-oriented design, as well as guidelines for extending this project.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

- Python (version 3.x recommended)

### Installation

Clone the repository:

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

## Features

* Text-based user interface for easy interaction.
* Dynamic board sizes and ship configurations.
* Engaging gameplay with hits, misses, and sunk notifications.

## Game Flow

* Game Initialization: players have the options to define game configurations, instantiate players, and initiate a game round.
* Round Setup Phase: Entering a round, questions will be asked to decide board dimensions and add ships to fleets; Each player will need to position all ships on the board.
  each player will start by positioning their ships on their board.
* Combat Phase: Players will then take turns choosing a target coordinate on the selected opponent's board to attack. The game will notify players if their hit was successful, missed, or sank an opponent's ship.
* Endgame Phase: The game concludes when only one player has unsunk ships, crowning them the winner.
