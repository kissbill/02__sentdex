import matplotlib.pyplot as plt

population_ages = [12,15,17,33,27,67,53,50,34,21,11,14,17,57,67,69,86,45,32,69,112,87,90,32,31,96,76,43,77,40,41]
#ids = [x for x in range(len(population_ages))]



bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages, bins, histtype ='bar', rwidth =0.7)


plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cimeeee')

plt.legend()

plt.show()
