# Distribuição Normal - Para valores de X acima da média

import scipy.stats
media = 12000
desvio_padrao = 800
X = 10000
p=scipy.stats.norm(media,desvio_padrao).cdf(X)-0.5
print(p)