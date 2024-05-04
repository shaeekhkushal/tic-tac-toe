def display_board(board):
    """
    Display the Tic Tac Toe board.
    """
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, "|", end=" ")
        print("\n-------------")

# Test display_board function
test_board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
display_board(test_board)
