def primer_caracter_repetido(palabra):
    palabra_minusculas  = palabra.lower()
    palabra_sin_espacios = palabra_minusculas.replace(" ", "")
    lista_letras = []
    for letra in palabra_sin_espacios:
        if letra in lista_letras:
            return letra
        else:
            lista_letras.append(letra)
    return 


print(primer_caracter_repetido("hola"))
print(primer_caracter_repetido('Hoola a probar'))
