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
                def print_grid(self, grid):
        for row in grid:
            print(" ".join(row))

    def player_turn(self):
        while True:
            try:
                guess_row = int(input("Enter the row number to guess (0 to {}): ".format(self.grid_size - 1)))
                guess_col = int(input("Enter the column number to guess (0 to {}): ".format(self.grid_size - 1)))
                if 0 <= guess_row < self.grid_size and 0 <= guess_col < self.grid_size:
                    return guess_row, guess_col
                else:
                    print("Invalid input. Row and column must be between 0 and {}.".format(self.grid_size - 1))
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play(self):
        while True:
            print("Player's Grid:")
            self.print_grid(self.player_grid)

            print("Computer's Grid:")
            self.print_grid(self.computer_grid)

            player_guess = self.player_turn()
            result = self.check_guess(player_guess, self.computer_grid)
            print(result)

            if all(all(cell != 'O' for cell in row) for row in self.computer_grid):
                print("Congratulations! You sunk all the computer's battleships. You win!")
                break

            computer_guess = self.computer_turn()
            result = self.check_guess(computer_guess, self.player_grid)
            print(result)

            if all(all(cell != 'O' for cell in row) for row in self.player_grid):
                print("Game over! The computer sunk all your battleships. You lose!")
                break

    def computer_turn(self):
        guess_row = random.randint(0, self.grid_size - 1)
        guess_col = random.randint(0, self.grid_size - 1)
        return guess_row, guess_col
        def check_guess(self, guess, target_grid):
        row, col = guess
        if target_grid[row][col] != 'O':
            ship_label = target_grid[row][col]
            target_grid[row][col] = 'X'
            return "Hit! You hit the {} battleship.".format(ship_label)
        else:
            return "Miss! You missed the target."

if __name__ == "__main__":
    grid_size = int(input("Enter the grid size for the Battleships game: "))
    game = BattleshipGame(grid_size)
    game.play()