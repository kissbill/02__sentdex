example = ['left','right','up','down']

#for i in range(len(example)):
#	print(i, example[i])



for i, j in enumerate(example):
	print(i ,j)

#dictionary creation
new_dict = dict(enumerate(example))

print(new_dict)
#{0: 'left', 1: 'right', 2: 'up', 3: 'down'}

[print(i,j) for i,j in enumerate(new_dict)]

#0 0
#1 1
#2 2
#3 3