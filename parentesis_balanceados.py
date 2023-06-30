def esta_balanceado(texto):
    cont = 0
    for parentesis in texto:
        if parentesis == "(":
            cont += 1
        elif parentesis == ")":
            cont -= 1
            if cont < 0:
                return False
    return cont == 0


print(esta_balanceado("(()sadas())"))
print(esta_balanceado("(s)(asa)(d)"))
print(esta_balanceado(")(()"))
