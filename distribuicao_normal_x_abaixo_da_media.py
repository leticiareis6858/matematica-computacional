# Distribuição Normal - Para valores de X abaixo da média

import scipy.stats
media = 1200
desvio_padrao = 800
X = 1000
p=0.5-scipy.stats.norm(media,desvio_padrao).cdf(X)
print(p)