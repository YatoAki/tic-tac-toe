# tic-tac-toe

<h2>Programmed by using the object oriented programming concepts</h2>

## Preview

![Alt Text](https://github.com/YatoAki/tic-tac-toe/blob/master/tic-tac-toe.gif)

## Features

1. Two Players
2. Custom Player Name

## How to run the game

1. First, clone this repo to your local mechine with __git__ command.
* `git clone https://github.com/YatoAki/tic-tac-toe`
2. Go to the cloned source code dictionary.
* `cd ./tic-tac-toe`
3. Run the `game.py` file with python interpretor.
* `python3 game.py`

## Game Architecture

### Game Class - `game.py`

1. The main file of our program which is composed with `player.py` & `board.py`
2. Allow two player to play taking turn

### Player Class - `player.py`

1. Get player-name and his play-sign to build an player object
2. Get move from the user

### Board Class - `board.py`

1. Build an empty board at the start of the game
2. Display board
3. Check status of each square
4. Check for the winning condition
