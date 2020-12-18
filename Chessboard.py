#from helper_functions import get_h_value

class Node:
	n = 0
	initial_state = ''
	current_state = ''
	# for steepest hill-climbing
	h_value = ''
	fitness_value = ''
	fitness_value_percent = ''


	def __init__(self, init_state, board_size):
		self.n = board_size
		self.initial_state = init_state
		self.current_state = self.initial_state
		self.h_value = h_value(self.current_state, self.n)


	def __lt__(self, another_node):
		if self.get_h_value() < another_node.get_h_value():
			return True
		else:
			return False

	def __eq__(self, another_node):
		if self.get_current_state() == another_node.get_current_state():
			return True
		else:
			return False


	def get_n(self):
		return self.n

	def get_initial_state(self):
		return self.initial_state

	def get_current_state(self):
		return self.current_state

	def get_h_value(self):
		return self.h_value


# col is the column number, > 0
def same_row_attacks(col, state, n):
	number_of_row_attacks = 0

	index = col - 1
	# stores the column number of the queen of interest.
	row_of_the_queen = state[index]
	for c in range(index + 1, n):
		if row_of_the_queen == state[c]:
			number_of_row_attacks += 1
	# for r in range(row + 1, self.n):
	# 	for c in range(col + 1, self.n):
	return number_of_row_attacks


# given the assumption that every column has exactly one queen, there is no possible way to
# have 2 or more queens on the same column
#def same_col(self, row, col):

# input: col = the column of the queen of interest
def same_diagonal_attacks(col, state, n):
	number_of_diagonal_attacks = 0	


	index = col - 1
	row_of_the_queen = int(state[index]) - 1
	col_of_the_queen = col - 1

	######################################################################################
	# check upper diagonal (one that extends upwards and rightwards)
	
	# for the upmost row, the column number that is on the same diagonal as the queen is
	#   the same as the row of the queen. Then, as we move down, the column is decremented 
	#   by one to stay on the same diagonal
	
	diagonal_column = row_of_the_queen + col_of_the_queen
	if diagonal_column >= n:
		diagonal_row = diagonal_column - (n - 1)
		diagonal_column = n - 1
		#print('diagonal_column = ' + str(diagonal_column))
	else:
		diagonal_row = 0	

	while diagonal_column > col_of_the_queen:
		row = int(state[diagonal_column]) - 1 
		#print(diagonal_column)
		#print(row)
		#print(diagonal_row)
		
		if str(row) == str(diagonal_row):
			number_of_diagonal_attacks += 1

		diagonal_column -= 1
		diagonal_row += 1
		#print('--------------------')


	#print(number_of_diagonal_attacks)
	######################################################################################
	# check lower diagonal (one that extends downwards and rightwards)
	diagonal_column = (n - 1 - row_of_the_queen) + col_of_the_queen 
	if diagonal_column >= n:
		#print('diagonal_row = ' + str(diagonal_row))
		#print('diagonal_column = ' + str(diagonal_column))
		diagonal_row = n - (diagonal_column - (n - 1)) - 1			
		diagonal_column = n - 1

	else:
		diagonal_row = n - 1

	while diagonal_column > col_of_the_queen:
		row = int(state[diagonal_column]) - 1
		# print(diagonal_column)
		# print(row)
		# print(diagonal_row)

		if str(row) == str(diagonal_row):
			number_of_diagonal_attacks += 1

		diagonal_column -= 1
		diagonal_row -= 1

		#print('-----------------------------------')

	#print(number_of_diagonal_attacks)

	return number_of_diagonal_attacks

# arguments:
# takes in the column and row of the queen and calculates the number of attacks on it
#    in the current state

def number_of_attacks(col, state, n):
	number_of_attacks = 0

	number_of_attacks = same_row_attacks(col, state, n)
	number_of_attacks += same_diagonal_attacks(col, state, n)

	return number_of_attacks

def h_value(state, n):
	h = 0

	for i in range(1, n + 1):
		h += number_of_attacks(i, state, n)

	return h
