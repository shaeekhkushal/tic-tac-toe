import tkinter as tk
import random


def display_board(board):
	for i in range(3):
		for j in range(3):
			cell_label = tk.Label(root, text=board[i][j], font=('Arial', 30), width=5, height=2, relief="ridge")
			cell_label.grid(row=i, column=j)
			cell_label.bind("<Button-1>", lambda event, row=i, col=j: player_move(row, col))


def player_move(row, col):
	if board[row][col] == " ":
		board[row][col] = "X"
		display_board(board)
		if check_winner("X"):
			result_label.config(text="Congratulations! You win!")
			new_game_button.config(state=tk.NORMAL)
		elif check_draw():
			result_label.config(text="It's a draw!")
			new_game_button.config(state=tk.NORMAL)
		else:
			computer_move()


def computer_move():
	while True:
		row = random.randint(0, 2)
		col = random.randint(0, 2)
		if board[row][col] == " ":
			board[row][col] = "O"
			display_board(board)
			if check_winner("O"):
				result_label.config(text="Sorry, you lose!")
				new_game_button.config(state=tk.NORMAL)
			elif check_draw():
				result_label.config(text="It's a draw!")
				new_game_button.config(state=tk.NORMAL)
			break


def check_winner(player):
	for row in board:
		if row.count(player) == 3:
			return True

	for col in range(3):
		if [board[row][col] for row in range(3)].count(player) == 3:
			return True

	if [board[i][i] for i in range(3)].count(player) == 3:
		return True
	if [board[i][2 - i] for i in range(3)].count(player) == 3:
		return True

	return False


def check_draw():
	for row in board:
		if " " in row:
			return False
	return True


def start_new_game():
	global board
	board = [[" " for _ in range(3)] for _ in range(3)]
	display_board(board)
	result_label.config(text="")
	new_game_button.config(state=tk.DISABLED)


board = [[" " for _ in range(3)] for _ in range(3)]

root = tk.Tk()
root.title("Tic Tac Toe")

display_board(board)

result_label = tk.Label(root, text="", font=('Arial', 20))
result_label.grid(row=3, columnspan=3)

new_game_button = tk.Button(root, text="New Game", command=start_new_game)
new_game_button.grid(row=4, columnspan=3)

root.mainloop()
