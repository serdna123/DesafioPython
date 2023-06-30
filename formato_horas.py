def cambiar_formato_veinticuatro_horas(hora_doce_horas_formato):
    hora_minusculas = hora_doce_horas_formato.lower()
    hora_lista = hora_minusculas.split(":")
    if "am" in hora_minusculas:
        if hora_lista[0] == "12":
            hora_lista[0] = "00"
    else:
        if hora_lista[0] != 12:
            hora_lista[0] = str(int(hora_lista[0])+12)
    hora_minusculas = ":".join(hora_lista)

    return hora_minusculas[:-2]


print(cambiar_formato_veinticuatro_horas("09:00 AM"))
print(cambiar_formato_veinticuatro_horas("09:00 PM"))
