print(__doc__)
import xlrd
import pylab as pl
import numpy as np
import urllib
#from sklearn.lda import LDA
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

#======= 0 ===========
    # links
outputFolder = r'E:\02_SOURCEs\Aniko_LDA\Program LDA Aniko final\Output\\'


#======= 1 ===========
    # File reading

    # user input asking
filename = input('Enter a file name: ')
    # Assign spreadsheet filename to `file`
file = filename + '.xls'

    # Load spreadsheet
xl = pd.ExcelFile(file)
    # Load a sheet into a DataFrame by name: df
# TBD --> if else ha angol spreadsheet1 vagy hiba uzi, hogy atvan nevezve az xlsx lap
##df = xl.parse('Munka1')
df = xl.parse('Results table')
    # Oszlop db kiolvasasa
lenght = len(df.columns)


#======= 2 ===========
    #Formating the DataFrame

    #replacing the index to column
df.reset_index(level=0,inplace=True)
    #renaming the[0] coloumn to Anyag
new_columns = df.columns.values;
new_columns[0] = 'anyag';
df.columns = new_columns
    #anyag a sor vegere
cols = df.columns.tolist()
cols = cols[-lenght:] + cols[:-lenght]
df = df[cols]


#======= 3 ===========
    #LDA

    # Betort_uveg_minta_1,Betort_uveg_minta_2, stb
meres_target = df["anyag"]
    #print(meres_target)

    # a Betort_uveg_minta_1-ben levo anyagok oszlopai, ezek lesznek az X tengely

    # for ciklus, az aktualis excel oszlop szamaihoz
oszlop = []
for x in range(0,lenght):
   oszlop.append(x)
    # dataframe db oszlop megadasa    
   X = df[oszlop].values
    # cel megadasa 
   y = df['anyag'].values
   target_names = ['1','2','3','4','5','6','7','8','9','10','11',]
##   target_names = ['10','9','8','7','6','5','4','3','2','1']
   
    # Linear Discriminant Analysis
lda = LinearDiscriminantAnalysis(n_components=4)
X_r2 = lda.fit(X, y).transform(X)


#print(X_r2)

#======= 4 ===========
    #The Plotting
colors = ['navy', 'turquoise', 'darkorange','purple','r','y','m','k','b','c']
lw = 2


    # Linear Discriminant Analysis ploting
##plt.figure()
##for color, i, target_name in zip(colors, [1,2,3,4,5,6,7], target_names):
##   plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], alpha=.8, color=color, label=target_name)
##           
##   plt.legend(loc='upper center', shadow=False, scatterpoints=1)
##   plt.title('LDA of Glass dataset')
##
##plt.show()

#======= 5 ===========
    #Writing into a file
#np.savetxt(r'C:\Users\Hanokri2\Documents\Python\Aniko_LDA\Program LDA Aniko final\Output\\' + filename + '.txt', X_r2)
np.savetxt(outputFolder + filename + '.txt', X_r2)
