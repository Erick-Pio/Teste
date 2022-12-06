import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
import pandas as pd
import sys
import os
import statsmodels.api as sm
import matplotlib


matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'

print(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_excel("C:/Users/Aluno/Downloads/Teste/eKran.xlsm")
SP = df.loc[df['Estado'] == 'São Paulo']
    
cols = ['ID do pedido', 'Empresa','Estado', 'Lucro']
SP.drop(cols, axis=1, inplace=True)
SP = SP.sort_values('Data')
SP.isnull().sum()

SP = SP.groupby('Data')['Vendas'].sum().reset_index()

SP = SP.set_index('Data')
SP.index

y = SP['Vendas'].resample('MS').mean()

y.plot(figsize=(15,6))
# plt.show()

plt.savefig('my_plot.png')

