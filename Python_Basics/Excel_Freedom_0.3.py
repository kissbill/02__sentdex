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

NoNames = []
twoWeeksDate = []
twoWeeksBinary = []
startDate = 0
endDate = 0
#======= 2 ===========
# get date
todayDate = (now.strftime("%Y.%m.%d"))
#======= 3 ===========
#Convert to array
noname_array = df.values
#======= 4 ===========
# Get NoNames
for i in range(4,24):
	NoNames.append(noname_array[i][0])
#Printout NoNames 1 - 19
#for i in range(0,len(NoNames)):
#	print(NoNames[i])

# Dates 2017.10.01 - 2018.09.28
# Checking with the full date queue
for i in range(1,341):
		
	if noname_array[3][i] == todayDate: # today date printed out with + 13 day
		#print(noname_array[3][i])
		startDate = i
		for k in range(0,10):
			#print(noname_array[3][i + k]) #
			twoWeeksDate.append(noname_array[3][i + k]) # datumok 2 hetre
			#print(i)
			endDate = i + k

# Not Nice need to mend it some other way -- 9 -> 10 as Counter
endDate = endDate + 1 			


# 2 weeks 0 or 1 
for j in range(4,24):

	for i in range(startDate, endDate):
		twoWeeksBinary.append(noname_array[j][i])



# 20 ppl for 2 weeks	
x = np.array_split(twoWeeksBinary, 20)



# columns date 
columnsDate = twoWeeksDate



y = pd.DataFrame(x, columns = columnsDate)



print(y)


#df = pd.DataFrame({'NoNames': [y]})


#################### WRITING INTO FILE ##############    

NoNames
print(len(NoNames))

df1 = pd.DataFrame(x , index=NoNames, columns=twoWeeksDate)


df1.to_excel("output.xlsx")


writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1')

writer.save()
#####################################################
