import random


def display_board(board):

	print("-------------")
	for row in board:
		print("|", end=" ")
		for cell in row:
			print(cell, "|", end=" ")
		print("\n-------------")


def player_move(board):

	while True:
		try:
			row = int(input("Enter row number (0, 1, or 2): "))
			col = int(input("Enter column number (0, 1, or 2): "))
			if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
				board[row][col] = "X"
				break
			else:
				print("Invalid move! Please try again.")
		except ValueError:
			print("Invalid input! Please enter a number.")


def computer_move(board):

	while True:
		row = random.randint(0, 2)
		col = random.randint(0, 2)
		if board[row][col] == " ":
			board[row][col] = "O"
			break


def check_winner(board, player):

	for row in board:
		if row.count(player) == 3:
			return True

	# Check columns
	for col in range(3):
		if [board[row][col] for row in range(3)].count(player) == 3:
			return True

	# Check diagonals
	if [board[i][i] for i in range(3)].count(player) == 3:
		return True
	if [board[i][2 - i] for i in range(3)].count(player) == 3:
		return True

	return False


def check_draw(board):

	for row in board:
		if " " in row:
			return False
	return True


def tic_tac_toe():

	board = [[" " for _ in range(3)] for _ in range(3)]
	display_board(board)

	while True:
		# Player's move
		player_move(board)
		display_board(board)
		if check_winner(board, "X"):
			print("Congratulations! You win!")
			break
		if check_draw(board):
			print("It's a draw!")
			break

		# Computer's move
		computer_move(board)
		display_board(board)
		if check_winner(board, "O"):
			print("Sorry, you lose!")
			break
		if check_draw(board):
			print("It's a draw!")
			break


# Start the Tic Tac Toe game
tic_tac_toe()
