import numpy as np
import pandas as pd
import datetime
#======= 0 ===========
now = datetime.datetime.now()
NoNames = []
twoWeeksDate = []
twoWeeksBinary = []
startDate = 0
endDate = 0

#======= 1 ===========
xl = pd.ExcelFile('noname.xlsx')
df = xl.parse('Sheet1')
noname_array = df.values

#======= 2 ===========
todayDate = (now.strftime("%Y.%m."))
year, week, dow = datetime.datetime.today().isocalendar()
week_start = datetime.datetime.strptime(str(year) + "-" + str(week-1) + "-0", "%Y-%W-%w")
result = [(week_start + datetime.timedelta(days=x)).day for x in range(1,13)]
workWeekStart = todayDate + str(result[0])

#======= 4 ===========
# Get NoNames
for i in range(4,len(noname_array)):
	NoNames.append(noname_array[i][0])

#======= 5 ===========
for i in range(1,len(noname_array[0])-1):
	if noname_array[3][i] == workWeekStart: 
		startDate = i
		for k in range(0,12):			
			twoWeeksDate.append(noname_array[3][i + k])			
			endDate = i + k


endDate = endDate + 1 			

#======= 6 ===========
for j in range(4,len(noname_array)):

	for i in range(startDate, endDate):
		twoWeeksBinary.append(noname_array[j][i])


x = np.array_split(twoWeeksBinary, len(noname_array)-4 )

columnsDate = twoWeeksDate

#======= 7 ===========
Spa = pd.DataFrame([ x[11] ], 
	index=[ NoNames[11] ], 
	columns=twoWeeksDate)

Ltc = pd.DataFrame([ x[6],x[12],x[18] ], 
	index=[ NoNames[6],NoNames[12],NoNames[18] ], 
	columns=twoWeeksDate)

VWBaseP = pd.DataFrame([ x[0],x[1],x[9],x[13],x[17],x[22] ], 
	index=[ NoNames[0],NoNames[1],NoNames[9],NoNames[13],NoNames[17],NoNames[22] ], 
	columns=twoWeeksDate)

VWBaseM = pd.DataFrame([ x[5],x[10] ], 
	index=[ NoNames[5],NoNames[10] ], 
	columns=twoWeeksDate)

Daimler = pd.DataFrame([ x[8],x[14],x[20] ], 
	index=[ NoNames[8],NoNames[14],NoNames[20] ], 
	columns=twoWeeksDate)

P514 = pd.DataFrame([ x[4],x[15],x[21] ], 	
	index=[ NoNames[4],NoNames[15],NoNames[21] ], 	
	columns=twoWeeksDate)

Hw = pd.DataFrame([ x[23] ], 	
	index=[NoNames[23]], 	
	columns=twoWeeksDate)

TestAutomation = pd.DataFrame([ x[3] ],
	 index=[ NoNames[3] ], 
	 columns=twoWeeksDate)

#################### WRITING INTO FILE ############## 
writer = pd.ExcelWriter('output2.xlsx', engine='xlsxwriter')

Spa.to_excel(writer, sheet_name='SPA')
Ltc.to_excel(writer, sheet_name='L T C')
VWBaseP.to_excel(writer, sheet_name='VWBase+')
VWBaseM.to_excel(writer, sheet_name='VWBase-')
Daimler.to_excel(writer, sheet_name='Daimler')
P514.to_excel(writer, sheet_name='P514')
Hw.to_excel(writer, sheet_name='HW')
TestAutomation.to_excel(writer, sheet_name='TestAutomation')
writer.save()