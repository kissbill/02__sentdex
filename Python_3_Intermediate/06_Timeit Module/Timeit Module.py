import timeit

#input_list = range(100)

#def div_by_five(num):
#	if num % 5 == 0:
#		return True
#	else:
#		return False
####################################
#xxx = ( i for i in input_list if div_by_five(i))

#xxx = [ i for i in input_list if div_by_five(i)]


print(timeit.timeit('''

input_list = range(100)

def div_by_five(num):
	if num % 5 == 0:
		return True
	else:
		return False
####################################
xxx = ( i for i in input_list if div_by_five(i))
	''', number= 5000))