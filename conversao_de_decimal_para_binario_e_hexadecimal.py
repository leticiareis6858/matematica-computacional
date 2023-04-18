# Programa para converter número decimal em binário e hexadecimal

num = int(input('Digite o número inteiro:'))

# Armazena o valor original de num para conversão em hexadecimal
original = num

# Conversão para binário
binario = ''
while num > 0:
    binario = str(num % 2) + binario
    num = num // 2

# Conversão para hexadecimal
hexadecimal = hex(original)[2:]

# Exibição dos resultados
print(f'O número binário é: {binario}')
print(f'O número hexadecimal é: {hexadecimal}')
