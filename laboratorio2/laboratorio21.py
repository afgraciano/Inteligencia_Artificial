import numpy as np

#Task 1: Palindrome
''' 
palindromo(n=3456543)
True

palindromo(n=543)
False

'''
def palindromo(n): # assume n is an integer
    
    # your code here
    r =  str(n) == str(n)[::-1]
    return r # r must be boolean True/False
print (palindromo(12321))
print (palindromo(12322))

#Task 2: Money Change

'''change_money(n=55)
[5,0,2]

change_money(n=200)
None

change_money(n=47)
[2,2,1]'''


def change_money(n):
    if n < 1 or n > 99:
        return None

    r = [0, 0, 0]  # Inicializamos la lista con ceros: [n_1, n_10, n_25]

    # Cálculo de monedas de 25 centavos
    r[2] = n // 25
    n %= 25

    # Cálculo de monedas de 10 centavos
    r[1] = n // 10
    n %= 10

    # Cálculo de monedas de 1 centavo
    r[0] = n

    return r

# Ejemplos de ejecución
print(change_money(55))   # [5, 0, 2]
print(change_money(200))  # None
print(change_money(47))   # [2, 2, 1]
#Esta función calcula la cantidad de monedas de 25, 10 y 1 centavo necesarias para devolver la cantidad n. Si n es menor que 1 o mayor que 99, se devuelve None.


#Task 3: Fibonacci se pone 0, 1 y luego se empiezan a sumar los 2 numeros anteriores de la sucesion, 0+1=1 1+1=2 2+1=3 3+2=5 5+3=8

'''fibonacci(10)
55

fibonacci(36)
14930352'''

'''def fibonacci(n):
    f_1=1
    f_2=1
    suma=0
    
    # tu codigo aqui
    
    return suma'''

def fibonacci(n):
    # Comprobar si n es 0
    if n == 0:
        return 0
    # Comprobar si n es 1
    elif n == 1:
        return 1
    else:
        f_1 = 1
        f_2 = 1

        # Calcular la sucesión de Fibonacci hasta n
        for i in range(2, n):
            suma = f_1 + f_2
            f_2 = f_1
            f_1 = suma

        return f_1

fibonacci(10), fibonacci(36)

# Ejemplos de ejecución
# Imprimir la sucesión para n=10
print("Sucesión para n=10:")
for i in range(10):
    print(fibonacci(i), end=", ")  # Imprimir términos separados por comas
print("El resultado de la sucesion fibonacci para n=10 es:", fibonacci(10))   # Imprimir el valor final 55


# Imprimir la sucesión para n=36
print("\nSucesión para n=36:")
for i in range(36):
    print(fibonacci(i), end=", ")  # Imprimir términos separados por comas
print("El resultado de la sucesion fibonacci para n=36 es:",fibonacci(36))   # Imprimir el valor final 14930352
#Este código completo calcula el n-ésimo término de la serie de Fibonacci. Comienza con los casos base de 0 y 1 y luego itera para calcular los términos subsiguientes hasta llegar al término n.


