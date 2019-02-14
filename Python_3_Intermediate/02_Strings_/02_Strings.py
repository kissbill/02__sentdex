names = ['Jessi' , ' Lolle' , ' eriko']

#for name in names:
#	print('Names is :' + name)
	#print('---------------------------------')
	#print (' '.join(['Hello there' , name])) # hatekonyabb elmeletileg

#print(', '.join(names))

#elmeletileg amikor kettonel tobb string van akkor erdemes mar a joint hasznalni
#-------------------------------------------------------------------------------------
#import os 

#location_of_files = 'K:\\02_SOURCEs\\02__sentdex\\Python_3_Intermediate\\02_Strings_'
#file_name = 'pelda.txt'

#print(location_of_files + '\\' + file_name)

#automatikusan hozzzaadja a \\-eket a os.path
#with open(os.path.join(location_of_files, file_name)) as f:
#	print(f.read())

#-----------------------------------------------
#String formating

who = 'Blea'
how_many = 12


print (who , 'eat many' , how_many, 'apples')

print('{} vett {} almat mama'.format(who, how_many)) # 3.6
print('{1} vett {0} almat mama'.format(who, how_many)) # 2.7 verziora , felcserelheto a sorrend