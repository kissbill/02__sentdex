import quandl
import pandas as pd
import pickle


def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]
        
def grab_initial_state_data():
    sates = state_list()
    main_df = pd.DataFrame()        

    for abbv in sates:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken="QzWMoCBauqxixFgx8xWz")
        df.rename(columns = {'Value':str(abbv)}, inplace = True)
       
        if main_df.empty:
            main_df = df                        
        else:
            main_df = main_df.join(df)

    print(main_df.head())
#ez arrajo, hogy ne kelljen mindig letolteni az adatokat
    # serializalja
    pickle_out = open('fiddy_states.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()
    

##grab_initial_state_data()
pickle_in = open('fiddy_states.pickle', 'rb')
HPI_data = pickle.load(pickle_in)
print(HPI_data)

#kevesebb sor es gyorsabb is
HPI_data.to_pickle('pickle.pickle')
HPI_data2 = pd.read_pickle('pickle.pickle')
print(HPI_data2)
                   
