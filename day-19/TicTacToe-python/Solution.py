class Board:
    def __init__(self, size):
        self.size = size
        self.grid = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(' ')
            self.grid.append(row)

    def display(self):
        for row in self.grid:
            print(" | ".join(row))
        print()

    def is_valid_move(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            if self.grid[row][col] == ' ':
                return True
        return False

    def place_move(self, row, col, symbol):
        if self.is_valid_move(row, col):
            # print("sdfghj")
            self.grid[row][col] = symbol
            return True
        return False

    def check_win(self, symbol):
        for i in range(self.size):
            row_win = True
            for j in range(self.size):
                if self.grid[i][j] != symbol:
                    row_win = False
                    break
            if row_win:
                return True

            col_win = True
            for j in range(self.size):
                if self.grid[j][i] != symbol:
                    col_win = False
                    break
            if col_win:
                return True

        diag1_win = True
        diag2_win = True
        for i in range(self.size):
            if self.grid[i][i] != symbol:
                diag1_win = False
            if self.grid[i][self.size - 1 - i] != symbol:
                diag2_win = False

        if diag1_win or diag2_win:
            return True

        return False

    def check_draw(self):
        for row in self.grid:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell == ' ':
                    return False
        return True


class Player:
    def __init__(self, symbol, name):
        self.name = name
        self.symbol = symbol


class Game:
    def __init__(self, size, players):
        self.board = Board(size)
        self.player1 = players[0]
        self.player2 = players[1]
        self.current_player = self.player1 

    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def start(self):
        while True:
            self.board.display()
            print(f"{self.current_player.name}'s turn ({self.current_player.symbol})")

            row, col = self.get_valid_move()
            self.board.place_move(row, col, self.current_player.symbol)

            if self.board.check_win(self.current_player.symbol):
                self.board.display()
                print(f"🎉 {self.current_player.name} wins!")
                break
            elif self.board.check_draw():
                self.board.display()
                print("It's a draw!")
                break

            self.switch_player()

    def get_valid_move(self):
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if self.board.is_valid_move(row, col):
                    return row, col
                else:
                    print("Invalid move. Try again.")
            except:
                print("Invalid input. Enter two numbers between 0-2.")


