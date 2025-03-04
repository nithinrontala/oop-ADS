class Board:
    """ Represents the Tic Tac Toe game board. """

    def __init__(self):
        self.size = 3
        self.grid = [['-' for _ in range(self.size)] for _ in range(self.size)]  # 3x3 board initialized with '-'

    def print_board(self):
        """ Prints the Tic Tac Toe board. """
        for row in self.grid:
            print(" | ".join(row))
        print()

    def is_valid_move(self, row, col):
        """ Checks if the move is valid (within bounds and not occupied). """
        return 0 <= row < self.size and 0 <= col < self.size and self.grid[row][col] == '-'

    def place_move(self, row, col, symbol):
        """ Places the player's move on the board. """
        self.grid[row][col] = symbol

    def check_win(self, symbol):
        """ Checks if the player with the given symbol has won. """
        # Check rows & columns
        for i in range(self.size):
            if all(self.grid[i][j] == symbol for j in range(self.size)) or \
               all(self.grid[j][i] == symbol for j in range(self.size)):
                return True
        # Check diagonals
        if all(self.grid[i][i] == symbol for i in range(self.size)) or \
           all(self.grid[i][self.size - 1 - i] == symbol for i in range(self.size)):
            return True
        return False

    def is_full(self):
        """ Checks if the board is full (draw). """
        for row in self.grid:
            for cell in row:
                if cell == '-':
                    return False
        return True


class Player:
    """ Represents a player with a name and symbol (X or O). """

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    """ Manages the Tic Tac Toe game logic. """

    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1  # Player 1 starts

    def switch_player(self):
        """ Switches the turn to the next player. """
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def play(self):
        """ Runs the game loop until a win or draw occurs. """
        while True:
            self.board.print_board()
            print(f"{self.current_player.name}'s turn ({self.current_player.symbol})")

            row, col = self.get_valid_move()
            self.board.place_move(row, col, self.current_player.symbol)

            if self.board.check_win(self.current_player.symbol):
                self.board.print_board()
                print(f"🎉 {self.current_player.name} wins!")
                break
            elif self.board.is_full():
                self.board.print_board()
                print("It's a draw!")
                break

            self.switch_player()

    def get_valid_move(self):
        """ Prompts the current player to enter a valid move. """
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if self.board.is_valid_move(row, col):
                    return row, col
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter two numbers between 0-2.")


if __name__ == "__main__":
    # Get player names
    player1 = Player(input("Enter Player 1 name: "), 'X')
    player2 = Player(input("Enter Player 2 name: "), 'O')

    # Start the game
    game = Game(player1, player2)
    game.play()
