print(__doc__)
import xlrd
import pylab as pl
import numpy as np
import urllib

import pandas as pd
import datetime

now = datetime.datetime.now()

#======= 0 ===========
    # links
#outputFolder = r'C:/_Kodeek/02__sentdex/Python_Basics\\'


#======= 1 ===========

# Load spreadsheet
xl = pd.ExcelFile('noname.xlsx')
df = xl.parse('Sheet1')
# Oszlop db kiolvasasa
lenght = len(df.columns)


#======= 2 ===========
# get date
#print (now.strftime("%Y.%m.%d"))
#print(df.ix[5])
#print(df.iloc[4])

#print (df._slice(slice(5,5))) 
#noname_2 = df._slice(slice(4, 5))
#print (df._slice(slice(0, 2), 1))
#noname_1 = df._slice(slice(300, 309),1) #4 - 6oszlop

#noname_array = noname_1.values
noname_array = df.values


for i in range(4,23):
	print(noname_array[i][0])

for i in range()
print(noname_array[3][10])
print(noname_array[7][10])
#print(noname_1)
#print('----------')
#print(noname_2)


#################### WRITING INTO FILE ##############    
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

#noname_1.to_excel(writer, sheet_name='Sheet1')

writer.save()
#####################################################
