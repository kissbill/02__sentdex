#Function Parameters and Typing 

game = [[0,0,0],
		[0,0,0],
		[0,0,0],]

def game_board(game_map,player=0,row=0,column=0,just_display=False): #default
	try:
		print('   A  B  C')
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count,row)
		return game_map
	except IndexError as e:
		print(' Hiba : a sor \ oszlopot jol irtad be ? 0 1 2  lehet' ,e)

	except Exception as e:
		print('Valami nagyon nem OK ' ,e)
	else:
		pass
	finally:
		pass
		
game = game_board(game , just_display = True)
game = game_board(game_board ,player=1, row=1,column=3  )

