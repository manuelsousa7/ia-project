
# TAI group (grupo de pos)
group = [];

# TAI board (lista 2D)
board = [];

# TAI color
# no color = 0
# has color > 0


def get_no_color():
	return 0


def no_color(c):
	return c == 0


def color(c):
	return c > 0

# TAI pos


def make_pos(l, c):
	return (l, c)


def pos_l(pos):
	return pos[0]


def pos_c(pos):
	return pos[1]


# TO DO

# Recommended, print board values to console

#	Return:  List with all the groups of pieces in this board O(MN)
def board_find_groups(m):
	res = []
	def floodfill(x, y, oC, nC):
		stack = [make_pos(x,y)]
		resF = []
		while len(stack) > 0:
			x, y = stack.pop()
			if m[x][y] != oC:
				continue
			resF = resF + [make_pos(x,y)]
			m[x][y] = nC
			if(y < len(m[0]) - 1):
				stack.append(make_pos(x,y+1))  # baixo
			if(x > 0):
				stack.append(make_pos(x-1,y))  # esquerda
			if(y > 0):
				stack.append(make_pos(x,y-1))  # cima
			if(x < len(m) - 1):
				stack.append(make_pos(x+1,y))  # direita
		return resF
	for i in range(0,len(m)):
		for ii in range(0,len(m[0])):
			if(color(m[i][ii])):
					res = res + [floodfill(i,ii,m[i][ii],-1)]
	return res


print board_find_groups([[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]])

#	Removes given group from board and "compresses" the board accordingly
#	IMPORTANT: Do not alter given board, create copy instead
#	Return: Modified board
def board_remove_group(searchBoard, searchGroup):
	newBoard = searchBoard;
	min_col = -1
	max_col = -1
	#Stores the board's column index that should be shifted
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
				newBoard[currentLine][i+min_col] = 0
				lastLine += 1

			currentLine -= 1

		#If column is empty, increment shiftAmount
		if (lastLine == len(newBoard) - 1):
			shiftIndexes.append(i+min_col)

	for j in range(len(shiftIndexes)-1):
		for c in range(len(newBoard[0]) -j -shiftIndexes[j]):
			for l in len(newBoard):
				newBoard[l][c+shiftIndexes[j]-j] = newBoard[l][c+shiftIndexes[j]-j+1]
				newBoard[l][c+shiftIndexes[j]-j+1] = 0

	return newBoard

#	Prints the board to the screen
def print_board(board):
	linha = ""
	for line in board:
		for color in line:
			linha += " " + str(color)
		print(linha)
		linha = ""

board_remove_group([[1,2,2],[1,1,2],[1,1,1]], [(0, 1), (0, 2), (1, 2)])