# ENTENDER ESSA FORMULA

import pandas as pd
x = {'Pesos' : [ 8, 7, 9, 10, 2, 7, 9, 10, 9, 3, 8, 5] }
print(x['Pesos'][4])

p = pd.DataFrame(x)
#print(f'p = {p}')

media = p['Pesos'].mean()
moda = p['Pesos'].mode()
mediana = p['Pesos'].median()
print(f'media = {media:.4f}')
print(f'moda = {moda}')
print(f'mediana = {mediana}')