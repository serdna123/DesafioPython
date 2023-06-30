def ordenar_lista(lista):
    for i in range(len(lista)):
        
       
        for j in range(0,len(lista)-i-1):
            print(f"{lista[j]} estoy en la : {i}")
            if lista[j]  > lista[j+1]:
                temporal=lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temporal
    return lista

print(ordenar_lista([5,3,4,2,1]))
