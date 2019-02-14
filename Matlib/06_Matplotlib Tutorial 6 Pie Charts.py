import matplotlib.pyplot as plt

day = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,2,7,13]
playing =  [8,5,12,3,0]

slices = [7,2,2,13]
activites = ['sleeping','eating','working','playing']
cols = ['c','m','b','k']
plt.pie(slices, labels = activites, colors = cols,startangle = 90, shadow = True , explode= (0,0.1,0,0))


plt.xlabel('Days')
plt.ylabel('Activites')
plt.legend()
plt.show()
