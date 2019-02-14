game = [[0,0,0],
		[0,0,0],
		[0,0,0],]

def game_board():
	print('   A  B  C')
	for count, row in enumerate(game):
		print(count,row)
	print()
game_board()


game [0][1] = 1 


x = game_board
x()