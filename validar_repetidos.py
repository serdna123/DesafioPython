# def devolver_duplicados(lista):
#     lista_repetidos = []
#     for i in range(len(lista)):
#         for j in range(i-1,-1,-1):
#             if lista[j] == lista[i]:
#                 lista_repetidos.append(lista[i])
#     return lista_repetidos

def devolver_duplicados(lista):
    lista_repetidos = []
    elementos =[]
    for elemento in lista:
        if elemento in elementos:
            lista_repetidos.append(elemento)
        else:
            elementos.append(elemento)
    return lista_repetidos
print(devolver_duplicados(["paco","ana","mig","pac o","ana","paco"]))