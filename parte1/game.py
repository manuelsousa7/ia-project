
#TAI group (grupo de pos)
group = [];

#TAI board (lista 2D)
board = [];

# TAI color
# no color = 0
# has color > 0
def get_no_color():
	return 0
def no_color (c):
	return c == 0
def color (c):
	return c > 0

# TAI pos
def make_pos (l, c):
	return (l, c)
def pos_l (pos):
	return pos[0]
def pos_c (pos):
	return pos[1]


#TO DO

#Recommended, print board values to console

#	Return:  List with all the groups of pieces in this board
def board_find_groups(searchBoard):
	return 0

#	Removes given group from board and "compresses" the board accordingly
#	IMPORTANT: Do not alter given board, create copy instead
#	Return: Modified board
def board_remove_group(searchBoard, searchGroup):
	newBoard = searchBoard;
	#Saves the column index interval that should be modified
	min_col = -1
	max_col = -1
	#Stores the board's column indexes that should be shifted
	shiftIndexes = []

	#Set all the coordinates in the group to 0 in the board and set min_col and max_col
	for coord in searchGroup:
		newBoard[pos_l(coord)][pos_c(coord)] = 0
		if (min_col == -1 or pos_l(coord) < min_col):
			min_col = pos_c(coord)

		if (max_col == -1 or pos_l(coord) > max_col):
			max_col = pos_c(coord)

	for i in range(max_col - min_col):
		#Go up the board
		currentLine = len(newBoard) - 1
		lastLine = currentLine
		while currentLine >= 0:
			#Se encontrar uma cor, move-a para baixo
			if (color(newBoard[currentLine][i+min_col])):
				newBoard[lastLine][i+min_col] = newBoard[currentLine][i+min_col]
				newBoard[currentLine][i+min_col] = get_no_color()
				lastLine += 1

			currentLine -= 1

		#If column is empty, increment shiftIndexes
		if (lastLine == len(newBoard) - 1):
			shiftIndexes.append(i+min_col)

	for j in range(len(shiftIndexes)-1):
		for c in range(len(newBoard[0]) -j -shiftIndexes[j]):
			for l in len(newBoard):
				newBoard[l][c+shiftIndexes[j]-j] = newBoard[l][c+shiftIndexes[j]-j+1]
				newBoard[l][c+shiftIndexes[j]-j+1] = get_no_color()

	return newBoard

#	Prints the board to the screen
def print_board(board):
	linha = ""
	for line in board:
		for color in line:
			linha += " " + str(color)
		print(linha)
		linha = ""

b1 = [[0,0,0,0,0],[0,2,3,3,0],[1,2,1,3,0],[2,2,2,2,0]]
board_remove_group(b1,[(1,1),(2,1),(3,1),(3,2),(3,3),(3,0)])
