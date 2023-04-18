# Programa para calcular a média de valores

import pandas as pd
x={'Velocidades':[67.8, 78.6, 54.4, 98.6, 99.4, 130.8, 142.6, 161.6, 142.5, 158.4]}
p=pd.DataFrame(x)
media=p['Velocidades'].mean()
print(f'A velocidade média de download foi de {media} Mbps')