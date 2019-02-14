
input_list = [ 5 , 6 ,10, 115, 4, 33, 35, 30, 65,55,67]

def div_by_five(num):
	if num % 5 == 0:
		return True
	else:
		return False

kaka = [i for i in input_list if div_by_five(i)]
#print(kaka)

#nem csinal semmit, ez objektum lesz , nem tudja kiporgetni
[[print(i,ii) for ii in range(5)] for i in range(5) ]
#fenti kifejtve
#for i in range(5):
#	for ii in range(5):
#		print(i, ii)
######################################################################

tuples = [[(i,ii) for ii in range(5)] for i in range(5) ]
print('TUPLES')
print(tuples)
######################################################################


lists = [[[i,ii] for ii in range(5)] for i in range(5) ]
print(" LISTA ")
print(lists)

######################################################################
#generator expression -> objektum lesz
generalExpression = ([[i,ii] for ii in range(5)] for i in range(5) )
#iteraljuk 

print([i for i in generalExpression])