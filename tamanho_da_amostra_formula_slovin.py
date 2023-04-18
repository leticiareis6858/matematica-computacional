# Tamanho da amostra pela fórmula de Slovin

from math import ceil
N = 150000
e = 0.02
n = ceil (N / (1+N*e**2))
print(f'Tamanho da amostra: {n}')

# Tamanho da amostra pela fórmula de Slovin-outro jeito

N = 150000
e = 0.02
n = (N / (1+N*e**2))
print(f'Tamanho da amostra: {n}')