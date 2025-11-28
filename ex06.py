import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

#filtra musicas lançadas apos 1980
#print(df[df['Year']>1980])

# filtra por ano e pela musica
print(df[df['Year']>1980][['Year','Track']])

