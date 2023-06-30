def es_palindromo(palindromo):
    letras = ""
    for index in range(len(palindromo)-1, -1, -1):
        letras += palindromo[index]
    #return letras.lower().replace(" ", "") == palindromo.lower().replace(" ", "")
    return palindromo.lower().replace(" ", "") == palindromo.lower().replace(" ", "")[::-1]
        
palindromo =  input(str("Ingrese un palindromo: "))

print(es_palindromo(palindromo))

