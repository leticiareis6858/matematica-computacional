# Programa para converter número binário em decimal e hexadecimal

# Solicita ao usuário para digitar um número binário
binario = input("Digite um número binário: ")

# Conversão para decimal
decimal = 0
for digito in binario:
  decimal = decimal * 2 + int(digito)

# Conversão para hexadecimal
hexadecimal = hex(decimal)[2:]

# Exibição dos resultados
print(f'O número decimal é: {decimal}')
print(f'O número hexadecimal é: {hexadecimal}')
