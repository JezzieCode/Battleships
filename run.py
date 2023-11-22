# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Fixing commit
# Adding info in commit
import random

class BattleshipGame:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.player_grid = [['O' for _ in range(grid_size)] for _ in range(grid_size)]
        self.computer_grid = [['O' for _ in range(grid_size)] for _ in range(grid_size)]
        self.ships = [(2, 'A'), (3, 'B'), (3, 'C'), (4, 'D'), (5, 'E')]
        self.place_ships(self.player_grid)
        self.place_ships(self.computer_grid)

    def place_ships(self, grid):
        for ship_size, ship_label in self.ships:
            self.place_ship(grid, ship_size, ship_label)

    def place_ship(self, grid, ship_size, ship_label):
        while True:
            orientation = random.choice(['H', 'V'])
            if orientation == 'H':
                row = random.randint(0, self.grid_size - 1)
                col = random.randint(0, self.grid_size - ship_size)
                if all(grid[row][col + i] == 'O' for i in range(ship_size)):
                    for i in range(ship_size):
                        grid[row][col + i] = ship_label
                    break
            else:
                row = random.randint(0, self.grid_size - ship_size)
                col = random.randint(0, self.grid_size - 1)
                if all(grid[row + i][col] == 'O' for i in range(ship_size)):
                    for i in range(ship_size):
                        grid[row + i][col] = ship_label
                    breakimport random

class BattleshipGame:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.player_grid = [['O' for _ in range(grid_size)] for _ in range(grid_size)]
        self.computer_grid = [['O' for _ in range(grid_size)] for _ in range(grid_size)]
        self.ships = [(2, 'A'), (3, 'B'), (3, 'C'), (4, 'D'), (5, 'E')]
        self.place_ships(self.player_grid)
        self.place_ships(self.computer_grid)

    def place_ships(self, grid):
        for ship_size, ship_label in self.ships:
            self.place_ship(grid, ship_size, ship_label)

    def place_ship(self, grid, ship_size, ship_label):
        while True:
            orientation = random.choice(['H', 'V'])
            if orientation == 'H':
                row = random.randint(0, self.grid_size - 1)
                col = random.randint(0, self.grid_size - ship_size)
                if all(grid[row][col + i] == 'O' for i in range(ship_size)):
                    for i in range(ship_size):
                        grid[row][col + i] = ship_label
                    break
            else:
                row = random.randint(0, self.grid_size - ship_size)
                col = random.randint(0, self.grid_size - 1)
                if all(grid[row + i][col] == 'O' for i in range(ship_size)):
                    for i in range(ship_size):
                        grid[row + i][col] = ship_label
                    break