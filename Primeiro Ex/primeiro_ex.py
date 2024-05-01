import pandas as pd
from datetime import date

#data = {
#    'name': ["Guilherme", "Maria", "John", "Luis", "Anna", "Gustavo"],
#    'email': ["guilherme.veras@200dev.com", "maria@gmail.com", "john@outlook.com", "luis@ibm.com", "anna@yahoo.com", "vinhola@gmail.com"],
#    'birthday': [date(2000, 4, 11), date(1995, 9, 22), date(1988, 7, 15), date(1979, 3, 5), date(2002, 11, 30), date(2008, 6, 27)],
#    'country': ["Brazil", "USA", "Canada", "Spain", "Germany", "Switzerland"]
#}

#df = pd.DataFrame(data)
#df.to_csv('Pessoas.csv', index=False)

df = pd.read_csv('Pessoas.csv')
df['birthday'] = pd.to_datetime(df['birthday'])

qtd_maiores = 0
maiores = []

for i in range(len(df)):
    if (df['birthday'][i].year <= date.today().year - 18):
        qtd_maiores += 1
        maiores.append(df['name'][i])

maiores.sort()

with open("Maioridade.txt", "w") as arq:
    arq.write(f"Existem {qtd_maiores} pessoas maiores de 18 anos\n")
    for i in maiores:
        idade = date.today().year - df.loc[df['name'] == i, 'birthday'].dt.year.iloc[0]
        dif = idade - 18
        arq.write(f"{i} tem mais {dif} anos\n")
