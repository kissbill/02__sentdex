#More on list comp and generators

input_list = [ 5 , 6 ,10, 115, 4, 33, 35, 30, 65,55,67]

def div_by_five(num):
	if num % 5 == 0:
		return True
	else:
		return False
##############################################################
kaka = (i for i in input_list if div_by_five(i))
#print(kaka)
#kaka = []
#for i in input_list:
#	print(i)
#	if div_by_five(i):
#		kaka.append(i)
##############################################################
#for i in kaka:
#	print(i)

#[print(i) for i in kaka]
##############################################################
kaka = [i for i in input_list if div_by_five(i)]
#print(kaka)
##############################################################
#nem csinal semmit, ez objektum lesz , nem tudja kiporgetni
proba = (print(i) for i in kaka)

for i in proba:
	i
#maga az i kerul fentrol kinyomasra