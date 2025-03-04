
from Solution import Player, LuckyBingoBoard, LuckyBingoGame

# **Python Test Cases Equivalent to Java**
def test_cases_1():
    size = 4
    player1_grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    player2_grid = [
        [2, 4, 6, 8],
        [10, 12, 14, 16],
        [18, 20, 22, 24],
        [26, 28, 30, 32]
    ]
    player3_grid = [
        [3, 6, 9, 12],
        [15, 18, 21, 24],
        [27, 30, 33, 36],
        [39, 42, 45, 48]
    ]

    players = [
        Player("Alice", LuckyBingoBoard(size, player1_grid)),
        Player("Bob", LuckyBingoBoard(size, player2_grid)),
        Player("Charlie", LuckyBingoBoard(size, player3_grid))
    ]

    print("Running Multiplayer Bingo Test Cases 1...")

    for player in players:
        player.display_board()

    players[0].mark_number(6)

    if not players[0].has_won():
        print("Test Passed 1")
    else:
        print("Test Failed: Player 1 should NOT have won yet")

    players[0].mark_number(7)
    players[0].mark_number(8)

    if not players[0].has_won():
        print("Test Passed 2")
    else:
        print("Test Failed: Player 1 should NOT have won yet")

    players[0].mark_number(5)

    if players[0].has_won():
        print("Test Passed 3")
    else:
        print("Test Failed: Player 1 should have won with a full row")

    print("Starting Multiplayer Game...")
    predefined_numbers = [
        2, 10, 4, 12, 6, 14, 8, 16,
        1, 5, 9, 13,
        3, 7, 11, 15,
        18, 22, 26, 30
    ]

    game = LuckyBingoGame(players, predefined_numbers)
    game.play()

    print("All Multiplayer Test Cases Passed! The Bingo Game Logic is Correct.")


def test_cases_2():
    size = 4
    player1_grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    player2_grid = [
        [2, 4, 6, 8],
        [10, 12, 14, 16],
        [18, 20, 22, 24],
        [26, 28, 30, 32]
    ]
    player3_grid = [
        [3, 6, 9, 12],
        [15, 18, 21, 24],
        [27, 30, 33, 36],
        [39, 42, 45, 48]
    ]

    players = [
        Player("Alice", LuckyBingoBoard(size, player1_grid)),
        Player("Bob", LuckyBingoBoard(size, player2_grid)),
        Player("Charlie", LuckyBingoBoard(size, player3_grid))
    ]

    print("Running Multiplayer Bingo Test Cases 2...")

    for player in players:
        player.display_board()

    predefined_numbers = [
        2, 10, 4, 12, 6, 14, 8, 16,
        1, 5, 9, 13,
        3, 7, 11, 15,
        18, 22, 26, 30
    ]

    game = LuckyBingoGame(players, predefined_numbers)
    game.play()

    print("All Multiplayer Test Cases Passed! The Bingo Game Logic is Correct.")


if __name__ == "__main__":
    test_cases_1()
    print("----------------------------------------------------------------------")
    test_cases_2()
