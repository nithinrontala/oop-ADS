
from Solution import Board, Player, Game
# ----------------------------------------------------
# Test Cases for the Board Class
# ----------------------------------------------------
def run_tests():
    print("\n----- Running Tests -----\n")
    
    # Test 1: Board Initialization (3x3)
    board3 = Board(3)
    all_empty = True
    for i in range(board3.size):
        for j in range(board3.size):
            if board3.grid[i][j] != ' ':
                all_empty = False
    if all_empty:
        print("Test 1 Passed: 3x3 board initialized with all cells empty.")
    else:
        print("Test 1 Failed: 3x3 board initialization error.")
    
    # Test 2: is_valid_move Method (3x3)
    if board3.is_valid_move(1, 1):
        print("Test 2.1 Passed: (1,1) is a valid move on 3x3 board.")
    else:
        print("Test 2.1 Failed: (1,1) should be valid.")
    
    if not board3.is_valid_move(-1, 0):
        print("Test 2.2 Passed: (-1,0) correctly identified as invalid.")
    else:
        print("Test 2.2 Failed: (-1,0) should be invalid.")
    
    if not board3.is_valid_move(3, 0):
        print("Test 2.3 Passed: (3,0) correctly identified as invalid (index equal to size).")
    else:
        print("Test 2.3 Failed: (3,0) should be invalid.")
    
    # Test 3: place_move Method (3x3)
    result = board3.place_move(0, 0, 'X')
    if result and board3.grid[0][0] == 'X':
        print("Test 3.1 Passed: Successfully placed 'X' at (0,0).")
    else:
        print("Test 3.1 Failed: Could not place 'X' at (0,0).")
    
    # Attempt to place a move in a non-empty cell.
    result = board3.place_move(0, 0, 'O')
    if not result and board3.grid[0][0] == 'X':
        print("Test 3.2 Passed: Cannot override cell (0,0) which is already occupied.")
    else:
        print("Test 3.2 Failed: Overriding cell (0,0) should not be allowed.")
    
    # Attempt an out-of-bound move.
    result = board3.place_move(3, 3, 'X')
    if not result:
        print("Test 3.3 Passed: Move at (3,3) correctly identified as out-of-bound.")
    else:
        print("Test 3.3 Failed: (3,3) is out-of-bound and move should not be allowed.")
    
    # Test 4: check_win Method
    # 4.1 Row win test.
    board_win = Board(3)
    board_win.place_move(0, 0, 'O')
    board_win.place_move(0, 1, 'O')
    board_win.place_move(0, 2, 'O')
    if board_win.check_win('O'):
        print("Test 4.1 Passed: Row win detected for 'O' in first row.")
    else:
        print("Test 4.1 Failed: Row win was not detected.")
    
    # 4.2 Column win test.
    board_win = Board(3)
    board_win.place_move(0, 0, 'X')
    board_win.place_move(1, 0, 'X')
    board_win.place_move(2, 0, 'X')
    if board_win.check_win('X'):
        print("Test 4.2 Passed: Column win detected for 'X' in first column.")
    else:
        print("Test 4.2 Failed: Column win was not detected.")
    
    # 4.3 Main diagonal win test.
    board_win = Board(3)
    board_win.place_move(0, 0, 'X')
    board_win.place_move(1, 1, 'X')
    board_win.place_move(2, 2, 'X')
    if board_win.check_win('X'):
        print("Test 4.3 Passed: Main diagonal win detected for 'X'.")
    else:
        print("Test 4.3 Failed: Main diagonal win was not detected.")
    
    # 4.4 Anti-diagonal win test.
    board_win = Board(3)
    board_win.place_move(0, 2, 'O')
    board_win.place_move(1, 1, 'O')
    board_win.place_move(2, 0, 'O')
    if board_win.check_win('O'):
        print("Test 4.4 Passed: Anti-diagonal win detected for 'O'.")
    else:
        print("Test 4.4 Failed: Anti-diagonal win was not detected.")
    
    # 4.5 No win condition test.
    board_win = Board(3)
    board_win.place_move(0, 0, 'X')
    board_win.place_move(0, 1, 'O')
    board_win.place_move(0, 2, 'X')
    if not board_win.check_win('X') and not board_win.check_win('O'):
        print("Test 4.5 Passed: No win detected as expected on mixed moves.")
    else:
        print("Test 4.5 Failed: Incorrect win detection on mixed moves.")
    
    # Test 5: check_draw Method
    # 5.1 Not full board should not be a draw.
    board_draw = Board(3)
    board_draw.place_move(0, 0, 'X')
    board_draw.place_move(0, 1, 'O')
    if not board_draw.check_draw():
        print("Test 5.1 Passed: Board not full correctly returns no draw.")
    else:
        print("Test 5.1 Failed: Board not full incorrectly reported as draw.")
    
    # 5.2 Full board with no win should return a draw.
    board_draw = Board(3)
    board_draw.place_move(0, 0, 'X')
    board_draw.place_move(0, 1, 'O')
    board_draw.place_move(0, 2, 'X')
    board_draw.place_move(1, 0, 'X')
    board_draw.place_move(1, 1, 'X')
    board_draw.place_move(1, 2, 'O')
    board_draw.place_move(2, 0, 'O')
    board_draw.place_move(2, 1, 'X')
    board_draw.place_move(2, 2, 'O')
    if board_draw.check_draw():
        print("Test 5.2 Passed: Full board with no win correctly detected as draw.")
    else:
        print("Test 5.2 Failed: Full board with no win not detected as draw.")
    
    # Test 6: Testing on a Different Board Size (4x4)
    board4 = Board(4)
    all_empty = True
    for i in range(board4.size):
        for j in range(board4.size):
            if board4.grid[i][j] != ' ':
                all_empty = False
    if all_empty:
        print("Test 6.1 Passed: 4x4 board initialized with all cells empty.")
    else:
        print("Test 6.1 Failed: 4x4 board initialization error.")
    
    result = board4.place_move(2, 3, 'Z')
    if result and board4.grid[2][3] == 'Z':
        print("Test 6.2 Passed: Successfully placed 'Z' at (2,3) on 4x4 board.")
    else:
        print("Test 6.2 Failed: Move at (2,3) on 4x4 board failed.")
    
    if not board4.is_valid_move(4, 0):
        print("Test 6.3 Passed: (4,0) correctly detected as out-of-bound on 4x4 board.")
    else:
        print("Test 6.3 Failed: (4,0) should be out-of-bound for 4x4 board.")
    
    print("\n----- Tests Completed -----\n")


# ----------------------------------------------------
# Main Execution
# ----------------------------------------------------
if __name__ == '__main__':
    # Uncomment the following line to run tests.
    run_tests()

    # Uncomment the following block to play the game interactively.
    board_size = int(input("Enter board size (n for an n x n board): "))
    player1 = Player('X', "Player 1")
    player2 = Player('O', "Player 2")
    players = [player1, player2]
    
    game = Game(board_size, players)
    game.start()
