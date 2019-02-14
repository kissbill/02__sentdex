import sqlite3
import pandas as pd

timeframes = ['2015-05']

for timeframe in timeframes:
	connection = sqlite3.connect('{}.db'.format(timeframe))
	c = connection.cursor()
	limit = 5000 #mennyit huzunk ki egyszerre a pandanak
	last_unix = 0 #bufferel minet a db-ben , ki
	#szedi az utolso unix timestamp-et,a kovetkezoo huzasnal magasabnak kell lennie mint az utolso unix time-nak
	cur_length = limit
	counter = 0
	test_done = False # megnenzi h teljesit a modell, erre kell ebben lesz az elso 5k adat 

	while cur_length == limit:	#format -> nagyobbnak kell lennie mint last unix 
		df = pd.read_sql("SELECT * FROM parent_reply WHERE unix > {} AND parent NOT NULL AND score > 0 ORDER BY unix ASC LIMIT {}".format(last_unix,limit),connection)
		#1. atadod a SQL lekerdezest 2.atadod a kapcsolodast 
		last_unix = df.tail(1)['unix'].values[0] #hol lett hagyjva utoljara
		cur_length = len(df) # az aktualis hosz az ami eppen az akt dataFrame hossz

		if not test_done: #append
			with open("test.from",'a', encoding='utf8') as f:
				for content in df['parent'].values:
					f.write(content + '\n')
			with open("test.to",'a', encoding='utf8') as f:
				for content in df['comment'].values:
					f.write(content + '\n')
			
			test_done = True
		else:
			with open("train.from",'a', encoding='utf8') as f:
				for content in df['parent'].values:
					f.write(content + '\n')
			with open("train.to",'a', encoding='utf8') as f:
				for content in df['comment'].values:
					f.write(content + '\n')

		counter += 1
		if counter % 20 == 0:
			print(counter*limit, 'rows completed so far') #minden 100k sor utan kiirja


