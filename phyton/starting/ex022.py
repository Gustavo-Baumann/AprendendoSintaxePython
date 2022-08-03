import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_json('starting/text.json')
print(tabela.head())
print(tabela.info())

tabela.drop_duplicates(inplace = True)
tabela["Duration"].fillna(60,inplace = True)
tabela["Duration"].dropna(inplace = True)
tabela["Duration"].plot(kind='hist')

plt.show()