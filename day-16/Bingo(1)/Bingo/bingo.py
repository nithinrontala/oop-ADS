# # # class BingoBoard:
# # #     def __init__(self, board, size=5):
# # #         self.board = board
# # #         self.marks = []
# # #         self.size = size
# # #         for i in range(self.size):
# # #             r = []
# # #             for j in range(self.size):
# # #                 r.append(0)
# # #             self.marks.append(r)

# # #     def mark_numbers(self, called_numbers):
# # #         for i in range(self.size):
# # #             for j in range(self.size):
# # #                 for num in called_numbers:
# # #                     if self.board[i][j] == num:
# # #                         self.marks[i][j] = 1

# # #     def is_row_complete(self, r):
# # #         for j in range(self.size):
# # #             if not self.marks[r][j]:
# # #                 return False
# # #         return True

# # #     def is_column_complete(self, c):
# # #         for i in range(self.size):
# # #             if not self.marks[i][c]:
# # #                 return False
# # #         return True

# # #     def is_main_diagonal_complete(self):
# # #         for i in range(self.size):
# # #             if not self.marks[i][i]:
# # #                 return False
# # #         return True

# # #     def is_anti_diagonal_complete(self):
# # #         for i in range(self.size):
# # #             if not self.marks[i][self.size - 1 - i]:
# # #                 return False
# # #         return True

# # #     def print_board(self):
# # #         for i in range(self.size):
# # #             r = ""
# # #             for j in range(self.size):
# # #                 if self.marks[i][j]:
# # #                     r += "X  "
# # #                 else:
# # #                     r += str(self.board[i][j]) + "  "
# # #             print(r.strip())


# # # class Player:
# # #     def __init__(self, name, board):
# # #         self.name = name
# # #         self.board = board
# # #         self.letters = []

# # #     def strike_letter(self):
# # #         if len(self.letters) < 5:  # There are 5 possible bingo letters: B, I, N, G, O
# # #             self.letters.append("BINGO"[len(self.letters)])

# # #     def print_result(self):
# # #         if len(self.letters) == 5:
# # #             result = "Bingo Achieved! " + self.name + " wins!"
# # #             print(result)
# # #             return True
# # #         return False


# # # class BingoGame:
# # #     l = ["B", "I", "N", "G", "O"]

# # #     def __init__(self, players, called_numbers):
# # #         self.players = players
# # #         self.called_numbers = called_numbers
# # #         self.current_turn = 0  # Start with the first player

# # #     def play(self):
# # #         while True:
# # #             current_player = self.players[self.current_turn]
# # #             if len(self.called_numbers) < 5:
# # #                 print("more required")
# # #                 break
# # #             print(f"\n{current_player.name}'s turn")

# # #             # Mark numbers for the current player
# # #             current_player.board.mark_numbers(self.called_numbers)

            
# # #             # Check for row/column/diagonal completion
# # #             for i in range(5):
# # #                 if current_player.board.is_row_complete(i):
# # #                     current_player.strike_letter()
# # #                 if current_player.board.is_column_complete(i):
# # #                     current_player.strike_letter()
# # #             if current_player.board.is_main_diagonal_complete():
# # #                 current_player.strike_letter()
# # #             if current_player.board.is_anti_diagonal_complete():
# # #                 current_player.strike_letter()
            
# # #             # Print the board for the current player
# # #             current_player.board.print_board()

# # #             # Check if the current player has achieved Bingo
# # #             if current_player.print_result():
# # #                 break  # Game ends as soon as one player wins

# # #             # Move to the next player
# # #             self.current_turn = (self.current_turn + 1) % len(self.players)

# # #         print("\nGame Over!")


# # # def main():
# # #     num_players = int(input("Enter number of players: "))
# # #     players = []

# # #     # Input Bingo boards for each player
# # #     for p in range(num_players):
# # #         print(f"\nEnter board for Player {p + 1}:")
# # #         board = []
# # #         for i in range(5):
# # #             r = list(map(int, input().split()))
# # #             board.append(r)
# # #         bingo_board = BingoBoard(board)
# # #         player_name = input(f"Enter name for Player {p + 1}: ")
# # #         players.append(Player(player_name, bingo_board))

# # #     # Input called numbers
# # #     called_numbers = list(map(int, input("\nEnter called numbers (comma-separated): ").split(',')))

# # #     # Start the game
# # #     game = BingoGame(players, called_numbers)
# # #     game.play()


# # # if __name__ == "__main__":
# # #     main()


# # class BingoBoard:
# #     def __init__(self, board, size=5):
# #         self.board = board
# #         self.marks = []
# #         self.size = size
# #         for i in range(self.size):
# #             r = []
# #             for j in range(self.size):
# #                 r.append(0)
# #             self.marks.append(r)

# #     def mark_numbers(self, called_numbers):
# #         for i in range(self.size):
# #             for j in range(self.size):
# #                 if self.board[i][j] in called_numbers:
# #                     self.marks[i][j] = 1

# #     def is_row_complete(self, r):
# #         for j in range(self.size):
# #             if not self.marks[r][j]:
# #                 return False
# #         return True

# #     def is_column_complete(self, c):
# #         for i in range(self.size):
# #             if not self.marks[i][c]:
# #                 return False
# #         return True

# #     def is_main_diagonal_complete(self):
# #         for i in range(self.size):
# #             if not self.marks[i][i]:
# #                 return False
# #         return True

# #     def is_anti_diagonal_complete(self):
# #         for i in range(self.size):
# #             if not self.marks[i][self.size - 1 - i]:
# #                 return False
# #         return True

# #     def print_board(self):
# #         for i in range(self.size):
# #             r = ""
# #             for j in range(self.size):
# #                 if self.marks[i][j]:
# #                     r += "X  "
# #                 else:
# #                     r += str(self.board[i][j]) + "  "
# #             print(r.strip())


# # class Player:
# #     def __init__(self, name, board):
# #         self.name = name
# #         self.board = board
# #         self.letters = []

# #     def strike_letter(self):
# #         if len(self.letters) < 5:  # There are 5 possible bingo letters: B, I, N, G, O
# #             self.letters.append("BINGO"[len(self.letters)])

# #     def print_result(self):
# #         if len(self.letters) == 5:
# #             result = "Bingo Achieved! " + self.name + " wins!"
# #             print(result)
# #             return True
# #         return False


# # class BingoGame:
# #     l = ["B", "I", "N", "G", "O"]

# #     def __init__(self, players):
# #         self.players = players
# #         self.called_numbers = []  # Start with no numbers called
# #         self.current_turn = 0  # Start with the first player

# #     def play(self):
# #         while True:
# #             current_player = self.players[self.current_turn]
# #             previous_player = self.players[self.current_turn]
# #             print(f"\n{current_player.name}'s turn")

# #             # Let the player call numbers for this turn
# #             player_called_numbers = list(map(int, input(f"Enter numbers called by {current_player.name} (comma-separated): ").split(',')))

# #             # Ensure no duplicate numbers are called by the player
# #             for num in player_called_numbers:
# #                 if num in self.called_numbers:
# #                     print(f"Number {num} has already been called. Please try again.")
# #                     return  # exit the game since player reused a number

# #             # Add the new numbers to the called numbers list
# #             self.called_numbers.extend(player_called_numbers)

# #             # Mark numbers for the current player
# #             current_player.board.mark_numbers(player_called_numbers)

# #             # Check for row/column/diagonal completion
# #             for i in range(5):
# #                 if current_player.board.is_row_complete(i):
# #                     current_player.strike_letter()
# #                     previous_player.strike_letter()
# #                 if current_player.board.is_column_complete(i):
# #                     current_player.strike_letter()
# #                     previous_player.strike_letter()
# #             if current_player.board.is_main_diagonal_complete():
# #                 current_player.strike_letter()
# #                 previous_player.strike_letter()
# #             if current_player.board.is_anti_diagonal_complete():
# #                 current_player.strike_letter()
# #                 previous_player.strike_letter()

# #             # Print the board for the current player
# #             current_player.board.print_board()

# #             # Check if the current player has achieved Bingo
# #             if current_player.print_result():
# #                 break  # Game ends as soon as one player wins

# #             # Move to the next player
# #             self.current_turn = (self.current_turn + 1) % len(self.players)

# #         print("\nGame Over!")


# # def main():
# #     num_players = int(input("Enter number of players: "))
# #     players = []

# #     # Input Bingo boards for each player
# #     for p in range(num_players):
# #         print(f"\nEnter board for Player {p + 1}:")
# #         board = []
# #         for i in range(5):
# #             r = list(map(int, input().split()))
# #             board.append(r)
# #         bingo_board = BingoBoard(board)
# #         player_name = input(f"Enter name for Player {p + 1}: ")
# #         players.append(Player(player_name, bingo_board))

# #     # Start the game
# #     game = BingoGame(players)
# #     game.play()


# # if __name__ == "__main__":
# #     main()


# class BingoBoard:
#     def __init__(self, board, size=5):
#         self.board = board
#         self.marks = []
#         self.size = size
#         for i in range(self.size):
#             r = []
#             for j in range(self.size):
#                 r.append(0)
#             self.marks.append(r)

#     def mark_number(self, number):
#         for i in range(self.size):
#             for j in range(self.size):
#                 if self.board[i][j] == number:
#                     self.marks[i][j] = 1

#     def is_row_complete(self, r):
#         for j in range(self.size):
#             if not self.marks[r][j]:
#                 return False
#         return True

#     def is_column_complete(self, c):
#         for i in range(self.size):
#             if not self.marks[i][c]:
#                 return False
#         return True

#     def is_main_diagonal_complete(self):
#         for i in range(self.size):
#             if not self.marks[i][i]:
#                 return False
#         return True

#     def is_anti_diagonal_complete(self):
#         for i in range(self.size):
#             if not self.marks[i][self.size - 1 - i]:
#                 return False
#         return True

#     def print_board(self):
#         for i in range(self.size):
#             r = ""
#             for j in range(self.size):
#                 if self.marks[i][j]:
#                     r += "X  "
#                 else:
#                     r += str(self.board[i][j]) + "  "
#             print(r.strip())


# class Player:
#     def __init__(self, name, board):
#         self.name = name
#         self.board = board
#         self.letters = []

#     def strike_letter(self):
#         if len(self.letters) < 5:  # There are 5 possible bingo letters: B, I, N, G, O
#             self.letters.append("BINGO"[len(self.letters)])

#     def print_result(self):

#         if len(self.letters) == 5:
#             result = "Bingo Achieved! " + self.name + " wins!"
#             print(result)
#             return True
#         return False


# class BingoGame:
#     l = ["B", "I", "N", "G", "O"]

#     def __init__(self, players):
#         self.players = players
#         self.called_numbers = []  # Start with no numbers called
#         self.current_turn = 0  # Start with the first player

#     def play(self):
#         while True:
#             current_player = self.players[self.current_turn]
#             print(f"\n{current_player.name}'s turn")

#             # Let the player call one number on their turn
#             player_called_number = int(input(f"Enter a number called by {current_player.name}: "))

#             # Ensure no duplicate numbers are called
#             if player_called_number in self.called_numbers:
#                 print(f"Number {player_called_number} has already been called. Please try again.")
#                 continue

#             # Add the new number to the called numbers list
#             self.called_numbers.append(player_called_number)

#             # Mark this number on all players' boards
#             for player in self.players:
#                 player.board.mark_number(player_called_number)

#             # Print the boards for all players
#             for player in self.players:
#                 print(f"\n{player.name}'s Board:")
#                 player.board.print_board()

#             # Check if the current player has achieved Bingo
#             if current_player.print_result():
#                 break  # Game ends as soon as one player wins

#             # Move to the next player
#             self.current_turn = (self.current_turn + 1) % len(self.players)

#         print("\nGame Over!")


# def main():
#     num_players = int(input("Enter number of players: "))
#     players = []

#     # Input Bingo boards for each player
#     for p in range(num_players):
#         print(f"\nEnter board for Player {p + 1}:")
#         board = []
#         for i in range(5):
#             r = list(map(int, input().split()))
#             board.append(r)
#         bingo_board = BingoBoard(board)
#         player_name = input(f"Enter name for Player {p + 1}: ")
#         players.append(Player(player_name, bingo_board))

#     # Start the game
#     game = BingoGame(players)
#     game.play()


# if __name__ == "__main__":
#     main()

class BingoBoard:
    def __init__(self, board, size=5):
        self.board = board
        self.marks = []
        self.size = size
        for i in range(self.size):
            r = []
            for j in range(self.size):
                r.append(0)
            self.marks.append(r)

    def mark_number(self, number):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == number:
                    self.marks[i][j] = 1

    def is_row_complete(self, r):
        for j in range(self.size):
            if not self.marks[r][j]:
                return False
        return True

    def is_column_complete(self, c):
        for i in range(self.size):
            if not self.marks[i][c]:
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
                if self.marks[i][j]:
                    r += "X  "
                else:
                    r += str(self.board[i][j]) + "  "
            print(r.strip())


class Player:
    l = ["B", "I", "N", "G", "O"]
    def __init__(self, name, board):
        self.name = name
        self.board = board
        self.letters = []

    def strike_letter(self, letter, completion_type):
        if letter not in self.letters:
            self.letters.append(letter)
            print(f"{self.name} completes a {completion_type}! Letter: {letter}")

    def print_result(self):
        if len(self.letters) == 5:
            result = f"Bingo Achieved! {self.name} wins!"
            print(result)
            return True
        return False


class BingoGame:
    l = ["B","I", "N","G","O"]
    def __init__(self, players):
        self.players = players
        self.called_numbers = []
        self.current_turn = 0

    def play(self):
        while True:
            current_player = self.players[self.current_turn]
            print(f"\n{current_player.name}'s turn")

            player_called_number = int(input(f"Enter a number called by {current_player.name}: "))

            if player_called_number in self.called_numbers:
                print(f"Number {player_called_number} has already been called. Please try again.")
                continue

            self.called_numbers.append(player_called_number)

            for player in self.players:
                player.board.mark_number(player_called_number)

            for player in self.players:
                print(f"\n{player.name}'s Board:")
                player.board.print_board()

            for player in self.players:
                for i in range(5):
                    if player.board.is_row_complete(i) and self.l[i] not in player.letters:
                        player.strike_letter(self.l[i], f"row {i + 1}")
                    if player.board.is_column_complete(i) and self.l[i] not in player.letters:
                        player.strike_letter(self.l[i], f"column {i + 1}")

                if player.board.is_main_diagonal_complete() and 'N' not in player.letters:
                    player.strike_letter(self.l[2], "main diagonal")
                if player.board.is_anti_diagonal_complete() and 'I' not in player.letters:
                    player.strike_letter(self.l[1], "anti-diagonal")

                if player.print_result():
                    print(f"{player.name} has won!")
                    return

            self.current_turn = (self.current_turn + 1) % len(self.players)

        print("\nGame Over!")


def main():
    num_players = int(input("Enter number of players: "))
    players = []

    for p in range(num_players):
        print(f"\nEnter board for Player {p + 1}:")
        board = []
        for i in range(5):
            r = list(map(int, input().split()))
            board.append(r)
        bingo_board = BingoBoard(board)
        player_name = input(f"Enter name for Player {p + 1}: ")
        players.append(Player(player_name, bingo_board))

    game = BingoGame(players)
    game.play()


if __name__ == "__main__":
    main()
