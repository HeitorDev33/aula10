import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

#somente as 5 primeiras linhas
#-print(df.head())

#somente as ultimas 5 linhas
#-print(df.tail())

#print(df.shape) #imprime a qntd de linhas e colunas

#mostra nomes das colunas
#-print(df.columns)

#mostra colunas detalhadas:
for i, coluna in enumerate (df.columns):
    #print("Coluna: ", coluna)
    print(f"{i}º Coluna: {coluna}")