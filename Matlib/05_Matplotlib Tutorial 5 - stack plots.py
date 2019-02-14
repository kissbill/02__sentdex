import matplotlib.pyplot as plt

day = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,2,7,13]
playing =  [8,5,12,3,0]

plt.plot([],[], color='m' , label = 'Sleeping' , linewidth = 5)
plt.plot([],[], color='c' , label = 'eating', linewidth = 5)
plt.plot([],[], color='b' , label = 'working', linewidth = 5)
plt.plot([],[], color='r' , label = 'playing', linewidth = 5)

plt.stackplot(day, sleeping,eating,working,playing, colors=['m','c','b','r'])

plt.xlabel('Days')
plt.ylabel('Activites')
plt.legend()
plt.show()
