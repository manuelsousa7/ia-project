
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
def board_remove_group(searchBoard, searchGroup)
	newBoard = [];
	#Do stuff
	return newBoard