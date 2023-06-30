def es_anagrama(palabra, palabra_dos):
    palabra= sorted(palabra.lower())
    palabra_dos= sorted(palabra_dos.lower())
    return palabra == palabra_dos

print(es_anagrama("lama","Mala"))
print(es_anagrama("calor","coral"))
print(es_anagrama("cama","casa"))
print(es_anagrama("mama","ama"))
