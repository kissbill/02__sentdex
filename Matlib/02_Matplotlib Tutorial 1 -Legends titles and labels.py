import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [5,7,4,3,7]


x2 = [1,3,5,7,9]
y2 = [5,7,4,3,8]


plt.bar(x,y, label = 'bars 1 ' ,color='r')
plt.bar(x2,y2, label = 'bars 2 ',color='c')


plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cimeeee')

plt.legend()

plt.show()
