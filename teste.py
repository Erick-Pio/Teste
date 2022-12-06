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
#RJ = df.loc[df['Estado'] == 'Rio de Janeiro']
#AP = df.loc[df['Estado'] == 'Amapá']
    
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

from pylab import rcParams
rcParams['figure.figsize'] = 18, 8
decomposition = sm.tsa.seasonal_decompose(y, model='additive')
ig = decomposition.plot()
plt.savefig('plot2.png')

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

mod = sm.tsa.statespace.SARIMAX(y,
                               order=(1, 1, 1),
                               seasonal_order=(1, 1, 0, 12),
                               enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

results.plot_diagnostics(figsize=(16, 8))
plt.savefig('plot3.png')