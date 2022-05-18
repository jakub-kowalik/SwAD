import pandas as pd

mieszkania = pd.read_csv('mieszkania.csv', delimiter=';')
print(len(mieszkania))
mieszkania['Wartosc'] = pd.to_numeric(mieszkania['Wartosc'], errors='coerce')
mieszkania['Kod'] = pd.to_numeric(mieszkania['Kod'])
mieszkania['Rok'] = pd.to_numeric(mieszkania['Rok'])

mieszkania = mieszkania.drop(mieszkania[mieszkania['Wartosc'] == 0].index)

mieszkania = mieszkania.dropna(axis=0, subset=['Wartosc']).drop(columns=['Atrybut'])
mieszkania

print(len(mieszkania))
mieszkania

import seaborn as sns
import matplotlib.pyplot as plt

# sns.displot(mieszkania['Wartosc'])

mylist = []

fig, ax = plt.subplots()

colors = ['red', 'white', 'black']

for idx, x in enumerate(mieszkania['Transakcje rynkowe'].unique()):
    sns.histplot(mieszkania[mieszkania['Transakcje rynkowe'] == x]['Wartosc'], kde=True, color=colors[idx], line_kws={'alpha': 1}, ax=ax)

# sns.displot(data=mieszkania, x='Wartosc', hue='Transakcje rynkowe', kde=True)
plt.show()
