from search import *

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


#print board_find_groups([[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]])

#	Removes given group from board and "compresses" the board accordingly
#	IMPORTANT: Do not alter given board, create copy instead
#	Return: Modified board
def board_remove_group(searchBoard, searchGroup):

	newBoard = searchBoard;
	#Minimum and maximum column index to update
	min_col = -1
	max_col = -1

	print("Antes")
	print_board(newBoard)

	#Set all the coordinates in the group to 0 and the interval of modified columns
	for coord in searchGroup:
		newBoard[pos_l(coord)][pos_c(coord)] = get_no_color()
		if (min_col == -1 or pos_c(coord) < min_col):
			min_col = pos_c(coord)

		if (max_col == -1 or pos_c(coord) > max_col):
			max_col = pos_c(coord)


	#Stores the indexes of empty columns
	emptyColumns = []
	#Update only modified columns
	for c in range(min_col, max_col+1, 1):
		lastLine = len(newBoard) - 1
		#Update each column from bottom to top
		for l in range(len(newBoard)-1, -1, -1):
			#If a color is found, move it to bottom of board
			if (color(newBoard[l][c])):
				newBoard[lastLine][c] = newBoard[l][c]
				newBoard[l][c] = get_no_color()
				lastLine -= 1

		#If column is empty, add column index to emptyColumns
		if (lastLine == len(newBoard) - 1):
			emptyColumns.append(c)

	#Shift the board left once for every emptyColumn index
	for emptyIndex in range(0, len(emptyColumns)):
		for c in range(emptyColumns[emptyIndex] - emptyIndex, len(newBoard[0])-1, 1):
			for l in range(len(newBoard)):
				newBoard[l][c] = newBoard[l][c+1]
				newBoard[l][c+1] = get_no_color()

	print("\nDepois")
	print_board(newBoard)

	return newBoard

class same_game(Problem):
	"""
	Models a Same Game problem as a satisfaction problem.
	A solution cannot have pieces left on the board.
	"""
	def __init__(self, board):
		print ("")
	def actions(self, state):
		print ("")
	def result(self, state, action):
		print ("")
	def goal_test(self, state):
		print ("")
	def path_cost(self, c, state1, action, state2):
		print ("")
	def h(self, node):
		print ("")

#	Prints the board to the screen
def print_board(board):
	linha = ""
	for line in board:
		for color in line:
			linha += " " + str(color)
		print(linha)
		linha = ""

b1 = [[0,2,0,0,0,1,3,4,2],
	  [0,2,2,3,0,1,2,3,1],
	  [1,3,2,2,0,3,2,1,4],
	  [2,2,1,2,0,3,1,2,3],
	  [2,2,2,2,2,2,2,2,2]]

g1 = [(0,1),
	  (1,1),
	  (1,2),
	  (2,2),
	  (2,3),
	  (3,3),
	  (4,0),
	  (4,1),
	  (4,2),
	  (4,3),
	  (4,4),
	  (4,5),
	  (4,6),
	  (4,7),
	  (4,8)]

board_remove_group(b1,g1)