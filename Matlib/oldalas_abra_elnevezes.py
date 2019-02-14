import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates

ax1 = plt.subplot2grid((1,1), (0,0))

#Part 1
'''
import csv

x = []
y = []

with open('example.txt', 'r') as csvfile:
    plots = csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label= 'Loaded from file')
'''
#Part 2
x, y = np.loadtxt('example.txt', delimiter=',', unpack = True)

ax1.plot(x,y, label= 'Loaded from file')
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)
    ax1.grid(True)


plt.xlabel('x')
plt.ylabel('y')
plt.title('Intresto ')
plt.legend()
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()
