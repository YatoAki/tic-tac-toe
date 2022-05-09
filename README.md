# tic-tac-toe

<h2>Programmed by using the object oriented programming concepts</h2>

## Preview

![Alt Text](https://github.com/YatoAki/tic-tac-toe/blob/master/tic-tac-toe.gif)

## Features

* Two Players
* Custom Player Name

## How to run the game

1. First, clone this repo to your local mechine with __git__ command.
* `git clone https://github.com/YatoAki/tic-tac-toe`
2. Go to the cloned source code dictionary.
* `cd ./tic-tac-toe`
3. Run the `game.py` file with python interpretor.
* `python3 game.py`

## Game Architecture

### Game Class - `game.py`

* The main file of our program which is composed with `player.py` & `board.py`
* Allow two player to play taking turn

### Player Class - `player.py`

* Get player-name and his play-sign to build an player object
* Get move from the user

### Board Class - `board.py`

* Build an empty board at the start of the game
* Display board
* Check status of each square
* Check for the winning condition
