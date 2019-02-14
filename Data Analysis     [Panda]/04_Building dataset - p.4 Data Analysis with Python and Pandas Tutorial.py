import quandl

import pandas as pd


df = quandl.get("FMAC/HPI_ODETX", authtoken="QzWMoCBauqxixFgx8xWz", start_date="1999-01-31")

print(df.head())

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#simple list:
##print(fiddy_states)

#print dateframe
##print(fiddy_states[0])

#print a column
print(fiddy_states[0][0])

#az elso sor nem kell
#elso dataframe es elso oszlop, es az 1. sortol kezdve kell
for abbreviation in fiddy_states[0][0][1:]:
##    print(abbreviation)
      print("FMAC/HPI_"+str(abbreviation))
