# Calcula o valor do seno e cosseno de um ângulo em graus

from numpy import pi # Importa a constante pi da biblioteca numpy
from math import factorial # Importa a função factorial da biblioteca math
x_graus=float(input('Informe o valor do ângulo, em graus: ')) # Solicita que digite um valor de ângulo em graus e armazena o valor digitado na variável x_graus
x_radianos=pi*x_graus/180 # Converte o valor de x_graus de graus para radianos e armazena o resultado na variável x_radianos
seno=0 # Inicializa a variáveL seno com o valor zero
cosseno=0 # Inicializa a variáveL cosseno com o valor zero
for n in range(10): # inicia um loop for que executa 10 vezes
  seno=seno+(-1)**n*x_radianos**(2*n+1)/factorial(2*n+1) # Série de Taylor para seno
  cosseno=cosseno+(-1)**n*x_radianos**(2*n)/factorial(2*n) # Série de Taylor para cosseno
print(f"O valor de seno é: {seno}") #  Imprime o valor aproximado do seno
print(f"O valor de cosseno é: {cosseno}") #  Imprime o valor aproximado do cosseno
