def triangulo_pascal(numero_filas):
    lista_pascal = []

    for numero_fila in range(numero_filas):
        fila =[]
        for index in range(numero_fila+1):
            if index == 0 or index == numero_fila:
                fila.append(1)
            else:
                valor= lista_pascal[numero_fila-1][index-1] + lista_pascal[numero_fila-1][index]
                fila.append(valor)
        lista_pascal.append(fila)
    return lista_pascal

def imprimir_triangulo(lista_triangulo):
    for elemento in lista_triangulo:
        print(elemento)
    
imprimir_triangulo(triangulo_pascal(4))