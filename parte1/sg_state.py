class sg_state:

	def __init__(self, newBoard):
		#Other useful slots can be added!
		self.board = newBoard;

	def __lt__(self, other_state):
		return 0