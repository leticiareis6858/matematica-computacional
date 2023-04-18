# Programa para calcular o desvio padrão de valores

import pandas as pd
x={'Velocidades':[8, 7, 9, 10, 2, 7, 9, 10, 9, 3, 8, 5]}
p=pd.DataFrame(x)
desviopadrao=p['Velocidades'].std()
print(f'O desvio padrão foi de {desviopadrao}')

# import pandas as pd
# x={'Velocidades':[8, 7, 9, 10, 2, 7, 9, 10, 9, 3, 8, 5]}
# p=pd.DataFrame(x)
# desviopadrao=p['Velocidades'].std()
# print(f'O desvio padrão foi de {desviopadrao} Mbps')