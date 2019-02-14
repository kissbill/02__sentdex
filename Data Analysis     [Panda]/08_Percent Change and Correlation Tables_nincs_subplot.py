import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


# Not necessary, I just do this so I do not show my API key.
api_key = open('quandlapikey.txt','r').read()

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]
    

def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        #lekerdezes FMAC/HPI_UT az adott allamot hozza letre es kerdezi le ra az adatokat
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        #oszlop atnevezes
        df.rename(columns = {'Value':str(abbv)}, inplace = True)
        
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0                       
        
        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    #print(main_df.head())    
    pickle_out = open('fiddy_states3.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()        

def HPI_Benchmark():
  df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
  print(df.head())
  df.rename(columns = {'Value':str('United Sates')}, inplace = True)
  df["United Sates"] = (df["United Sates"] - df["United Sates"][0]) / df["United Sates"][0] * 100.0
    #ha nem tudjuk a nevet az oszlopnak akkor print(df.head())
  return df
  
##grab_initial_state_data()



HPI_data = pd.read_pickle('fiddy_states3.pickle') #grabin data

#korelacio
HPI_State_Correlation = HPI_data.corr() #data frame ez
print(HPI_State_Correlation)

#statisztika kiiratasa 
print(HPI_State_Correlation.describe())
