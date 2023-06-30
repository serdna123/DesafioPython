def factorial(numero):
    fact = 1
    for i in range(numero):
        fact += fact*i
    return fact

print(factorial(0))
print(factorial(3))
print(factorial(4))
print(factorial(5))

def factoria_recursivo(numero):
    if numero == 1 or numero == 0:
        return 1
    return numero * factoria_recursivo(numero-1) 

print(factoria_recursivo(0))
print(factoria_recursivo(3))
print(factoria_recursivo(4))
print(factoria_recursivo(5))