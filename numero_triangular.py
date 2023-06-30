def numero_triangular(fila):
    numero_triangular = 0
    for numero in range(1, fila+1):
        numero_triangular += numero

    return numero_triangular


print(numero_triangular(3))
print(numero_triangular(4))
print(numero_triangular(6))
