# Conversão de caractere em decimal, binário, e hexadecimal

caractere = input("Insira um caractere: ")

decimal = ord(caractere)
binario = bin(ord(caractere))[2:]
hexadecimal = hex(ord(caractere))[2:]

print(f"O caractere {caractere} em decimal é: {decimal}")
print(f"O caractere {caractere} em binário é: {binario}")
print(f"O caractere {caractere} em hexadecimal é: {hexadecimal}")
