# Programa para descriptografar mensagens com letras maiúsculas

from string import ascii_uppercase
# ascii_uppercase é uma string que contém todas as letras maiúsculas do alfabeto em ordem
a = list(ascii_uppercase)
# Cria uma lista 'a' que contém todas as letras maiúsculas do alfabeto em ordem
mc = input('Digite a mensagem criptografada: ')
mc = mc.upper()
# Converte a mensagem criptografada para letras maiúsculas
m=""
# Cria uma string vazia 'm', que será usada para armazenar a mensagem decodificada
for l in mc:
# Começa um loop 'for' que percorre cada caractere da mensagem criptografada
  i = ord(l)-65
# Converte o caractere atual para seu valor ASCII e subtrai 65 para obter um valor entre 0 e 25
  if l in a:
# Verifica se o caractere atual está na lista 'a'. Se estiver, ele executa o código dentro do bloco 'if'. Do contrário, ele adiciona o caractere atual a 'm' sem modificá-lo.
    m += a[(i-3)%26]
# Adiciona a letra correspondente à mensagem decodificada.Subtraindo 3 do índice atual e o usando para acessar a letra correspondente na lista 'a' e adiciona essa letra a 'm'
  else:
    l
print(f'Mensagem original: {m}')
