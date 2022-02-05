
import matrix
from character import *
#from character import Direction

rows, columns = 23, 40

game_matrix = matrix.Matrix(rows, columns)

main_symbol = MainSymbol('u')

while True:
	game_matrix.print_matrix()
	direction = input('where to next? ')
	if direction == 'q': break
	elif direction not in (Direction.NORTH, Direction.SOUTH, Direction.WEST, Direction.EAST):
            continue
   
