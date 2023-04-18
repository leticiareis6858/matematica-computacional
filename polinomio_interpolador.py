# Programa para obter o polinômio interpolador

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import *
x=[50000, 15, 30000]
y=[50000, 17, 28000]
p=lagrange(x, y)
print(p)