
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
		stack = [(x, y)]
		resF = []
		while len(stack) > 0:
			x, y = stack.pop()
			if m[x][y] != oC:
				continue
			resF = resF + [(x,y)]
			m[x][y] = nC
			if(y < len(m[0]) - 1):
				stack.append((x, y + 1))  # baixo
			if(x > 0):
				stack.append((x - 1, y))  # esquerda
			if(y > 0):
				stack.append((x, y - 1))  # cima
			if(x < len(m) - 1):
				stack.append((x + 1, y))  # direita
		return resF
	for i in range(0,len(m)):
		for ii in range(0,len(m[0])):
			if(m[i][ii] != -1):
					res = res + [floodfill(i,ii,m[i][ii],-1)]
	return res


print board_find_groups([[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]])

#	Removes given group from board and "compresses" the board accordingly
#	IMPORTANT: Do not alter given board, create copy instead
#	Return: Modified board
def board_remove_group(searchBoard, searchGroup):
	newBoard = [];
	# Do stuff
	return newBoard

#	Prints the board to the screen
def print_board(board):
	linha = ""
	for line in board:
		for color in line:
			linha += " " + str(color)
		print(linha)
		linha = ""
