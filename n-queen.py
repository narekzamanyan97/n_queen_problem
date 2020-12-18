
from Chessboard import Node

from helper_functions import *

def main():
	n = 8
	state = randomly_generate_state(n)

	select = '1'

	while select == '1':
		print('Select')
		print('[1] Solve n-queen problem using Steepest Ascent Hill Climbing')
		print('[2] Solve n-queen problem using Genetic Algorithm ')
		print('[3] Exit')		

		select = input()
		total_elapsed_time = 0
		total_search_cost = 0
		number_of_solved_cases = 0
		if select == '1':
			success = 0
			failure = 0

			for i in range(0, 100):
				state = randomly_generate_state(n)
				print('Case ' + str(i + 1) + ':')
				solution = steepest_ascent_hill_climbing(state, n) 
				if solution is not None:
					print('*******************************************')
					print('Solution Found:')
					print('Input instance: ')
					print_board(state, n)
					print('Solution:')
					number_of_solved_cases += 1
					total_elapsed_time += solution[0]
					total_search_cost += solution[1]
					solution_state = solution[2]
					print_board(solution_state.get_current_state(), n)
					success += 1
				else:
					print('*******************************************')
					print('Solution Not Found:')
					failure += 1
			print('Solved: ' + str(success))
			print('Not solved: ' + str(failure))
			print('Percent of Solved: ' + str(success) + '%')
		elif select == '2':
			n = 8
			k = 10

			print('Time (in seconds) you would like to allow for each case, before the algorithm gives up')
			print('Enter 0 to use the default value of 2.22 seconds')
			seconds = input()
			seconds = int(seconds)

			for i in range(0, 100):
				print('Case ' + str(i + 1) + ':')
				if seconds != 0:
					solution = genetic_algorithm(n, k, seconds)
				else:
					solution = genetic_algorithm(n, k)
				if solution is not None:
					number_of_solved_cases += 1
					total_elapsed_time += solution[0]
					total_search_cost += solution[1]
					print_board(solution[2].get_current_state(), n)
				print('*******************************************')
		else:
			break

		average_elapsed_time = round(total_elapsed_time / number_of_solved_cases, 2)
		average_search_cost = round(total_search_cost / number_of_solved_cases, 2)

		print("number_of_solved_cases = " + str(number_of_solved_cases))
		print("average_elapsed_time = " + str(average_elapsed_time))
		print("average_search_cost = " + str(average_search_cost))

if __name__ == "__main__":
	main()