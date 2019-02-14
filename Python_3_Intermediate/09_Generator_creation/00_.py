#def simple_gen():
#	yield 'Oh'
#	yield 'Hello'
#	yield 'there'


#for i in simple_gen():
#	print(i)

CORRECT_COMBO = (3, 4 ,9 )
#found_combo = False
#for c1 in range(10):
#	if found_combo:
#		break
#	for c2 in range(10):
#		if found_combo:
#			break
#		for c3 in range(10):
#			if (c1,c2,c3) == CORRECT_COMBO:
#				print('Find the key: {}'.format((c1,c2,c3)))
#				found_combo = True
#				break
#			print (c1,c2,c3)


def combo_gen():
	for c1 in range(10):
		for c2 in range(10):
			for c3 in range(10):
				yield(c1,c2,c3)

#generator yield --> giving back data stream 
#gen-be meg lehet allitani
#vagy meghivva meg lehet

for (c1,c2,c3) in combo_gen():
	#print(c1,c2,c3)
	if (c1,c2,c3) == CORRECT_COMBO:
		print( 'Find the key: {}'.format( (c1,c2,c3) ) )
		break