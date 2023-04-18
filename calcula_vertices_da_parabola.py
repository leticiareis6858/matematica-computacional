# entrada dos coeficientes da parábola
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# cálculo do vértice da parábola
x_vertice = -b / (2*a)
y_vertice = a*x_vertice**2 + b*x_vertice + c

# exibição do resultado
print("O vértice da parábola é (%.2f, %.2f)" % (x_vertice, y_vertice))