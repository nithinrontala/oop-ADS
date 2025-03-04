class BingoBoard:
    def __init__(self, board,size = 5):

        self.board = board
        self.marks = []
        self.size = size

        for i in range(self.size):
            r = []
            for j in range(self.size):
                r.append(False)
            self.marks.append(r)

    def mark_numbers(self, called_numbers):
        # print(called_numbers)
        for i in range(self.size):

            for j in range(self.size):
                # print(self.marks[i][j])
                for num in called_numbers:
                    if self.board[i][j] == num:
                        self.marks[i][j] = True

    def is_row_complete(self, r):
        for j in range(self.size):
            # print(self.marks[r][j])
            if self.marks[r][j] == False:
                return False
        return True

    def is_column_complete(self, called_numbersol):
        for i in range(self.size):
            if self.marks[i][called_numbersol] == False:
                return False
        return True

    def is_main_diagonal_complete(self):
        for i in range(self.size):
            if not self.marks[i][i]:
                return False
        return True

    def is_anti_diagonal_complete(self):
        for i in range(self.size):
            if not self.marks[i][self.size - 1 - i]:
                return False
        return True

    def print_board(self):
        for i in range(self.size):
            r = ""
            for j in range(self.size):
                # print(self.marks[i][j])
                if self.marks[i][j] == True:
                    r += "X  "
                else:
                    r += str(self.board[i][j]) + "  "
            print(r.strip())

class BingoGame:
    l = ["B", "I", "N", "G", "O"]

    def __init__(self, board, called_numbers):

        self.board = board
        self.called_numbers = []
        for num in called_numbers:
            self.called_numbers.append(num)
        self.letters = []

    def play(self):
        self.board.mark_numbers(self.called_numbers)
        for i in range(5):
            if self.board.is_row_complete(i):
                self.strike_letter()
            if self.board.is_column_complete(i):
                self.strike_letter()
        if self.board.is_main_diagonal_complete():
            self.strike_letter()
        if self.board.is_anti_diagonal_complete():
            self.strike_letter()
        self.board.print_board()
        self.print_result()

    def strike_letter(self):
        # print(len(self.letters), len(self.l))
        if len(self.letters) < len(self.l):

            self.letters.append(self.l[len(self.letters)])
        # print(self.letters)

    def print_result(self):

        if len(self.letters) == len(self.l):
            result = ""
            for letter in self.letters:
                result += letter + " "
            print()
            print(result.strip())
            print("Game Completed!")
        else:
            print()
            result = "Remaining Letters: "
            for i in range(len(self.letters), len(self.l)):
                result += self.l[i] + " "
            print(result.strip())

def main():
    board = []
    for i in range(5):
        r = list(map(int, input().split()))
        board.append(r)
    called_numbers = []
    a = input().strip().split(',')
    for num in a:
        called_numbers.append(int(num))
    bingo_board = BingoBoard(board)
    game = BingoGame(bingo_board, called_numbers)
    game.play()

if __name__ == "__main__":
    main()