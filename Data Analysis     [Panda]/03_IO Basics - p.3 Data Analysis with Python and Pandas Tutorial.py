import pandas as pd

#original csv reading in
df = pd.read_csv('BUDAPESTSE-BUX.csv')

print(df.head())
print('==================================================================')

#setting the index 0. to date
df.set_index('Date', inplace=True)
df.to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv')
print(df.head())

print('==================================================================')
df = pd.read_csv('newcsv2.csv', index_col=0)
print(df.head())
#oszlopok kezzel elnevezese, atirasa 4db szoval 4 nevet var
df.columns = ['Nyitas','Zaro ar','Maximum','Minimum']
print(df.head())

#lementes uj oszlop nevekkel
df.to_csv('newcsv3.csv')
#header nelkuli lementes
df.to_csv('newcsv4_no_head.csv', header= False)
#nincs semmi header , es nem irom at, hanem ujat adok meg neki
df = pd.read_csv('newcsv4_no_head.csv', names=['Nyitas','Zaro ar','Maximum','Minimum'],index_col = 0)
df.to_html('weblaposkimentes.html')

df = pd.read_csv('newcsv4_no_head.csv',names=['Nyitas','Zaro ar','Maximum','Minimum'])
print(df.head())

df.rename(columns={'Maximum':'Maximus'}, inplace= True)
print(df.head())
