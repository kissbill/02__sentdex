#List comprehension and generator expressions

#An example of list comprehension:
#ez bekerul a memoriaba tovabb tart 
kaka = [i for i in range(5000000)] #lista objektum

#kaka = []
#for i in range(500):
#	kaka.append(i)

#print (list(kaka)[:5]) # 5-ig kiirja
print('done')

#An example of a generator expression:
#nem kerul a memoriaba
kaka = (i for i in range(5000000)) #lista objektum

#kaka = []
#for i in range(500):
#	kaka.append(i)

print (list(kaka)[:5]) # 5-ig kiirja
#print(kaka)


