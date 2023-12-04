# Battleship Game

## Introduction

This is a simple console-based implementation of the classic game Battleship in Python. The game is played on an 8x8 grid, and the player competes against the computer to sink each other's battleships.

## How to Play

1. **Setup:**
    - The game begins by placing battleships on the player's and computer's grids.
    - Ships are represented by letters (A, B, C, D, E) and have varying lengths (2 to 5 cells).

2. **Player's Turn:**
    - The player is prompted to guess a cell on the computer's grid by entering row and column numbers.
    - The result of the guess is displayed, indicating whether it's a hit or a miss.

3. **Computer's Turn:**
    - The computer randomly selects a cell on the player's grid to guess.
    - The result is displayed, showing whether the computer's guess is a hit or a miss.

4. **Game Progress:**
    - The game continues with alternating turns until one player sinks all of the opponent's battleships.

5. **Game End:**
    - The game ends when either the player or the computer sinks all the opponent's battleships.
    - The result is displayed, indicating whether the player won or lost.

## Running the Game