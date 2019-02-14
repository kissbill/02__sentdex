import quandl
import pandas as pd

# Not necessary, I just do this so I do not show my API key.
api_key = open('quandlapikey.txt','r').read()
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

main_df = pd.DataFrame()

for abbv in fiddy_states[0][0][1:]:
    query = "FMAC/HPI_"+str(abbv)
    df = quandl.get(query, authtoken=api_key)
##    df.coulmns = [str(abbv)]
    df.rename(columns = {'Value':str(abbv)}, inplace = True)

    if main_df.empty:
        main_df = df
    else:
        main_df = main_df.join(df)

## it is caused by each new df having a column name 'Value'
## so the tables to be joined have 'overlapping columns' --> (this appears to be the default name?)
