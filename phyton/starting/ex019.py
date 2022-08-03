import pandas as pd

dados = {
    'frutas' : ['banana','laranja','uva'],
    'cores' : ['amarelo','laranja','roxo']
}
tabela = pd.DataFrame(dados)

print(tabela)
print("Primeira fruta:", tabela.loc[0])

timesFutebol = ['Palmeiras','Corinthians','Flamengo']
tabela =  pd.Series(timesFutebol, index=['Primeiro','Segundo','Terceiro'])

print("\n")
print(tabela)