import numpy as np

#Task 1: Cauchy Matrix:  los elementos de la matriz son el resultado de restar las posiciones correspondientes en la x y y vectores donde las filas corresponden a x y las columnas para y.

def cauchy(x, y):
    # Verificar si hay alguna división entre cero
    if any(x - y == 0):
        raise ValueError("División entre cero no permitida")

    # Crear la matriz de Cauchy
    r = 1.0 / (x.reshape(-1, 1) - y)
    return r
# Ejemplo de ejecución
x = np.array([45, 31, 67, 75, 54])
y = np.array([17,  7, 15, 15, 18])
resultado = cauchy(x, y)
print(resultado)

'''#la siquiente ejecución debería generar una ValueErrorexcepción que indica que division por cero no permitida
x = np.array([45, 31, 67, 75, 54])
y = np.array([17,  7, 15, 75, 18])
cauchy(x,y)'''

#Task 2: Position of closest scalar (Posición del escalar más cercano)Dado un vector 1Dx, encuentre la posición del elemento más cercano av
'''En este código, np.abs(x - v) calcula el valor absoluto de la diferencia entre cada elemento en x y v, lo que nos da las distancias entre v y cada elemento en x.
Luego, np.argmin encuentra la posición del valor mínimo en esas distancias, que corresponde al elemento más cercano a v'''
def minimo(x, v):
    # Encuentra la posición del elemento más cercano a v en x
    return np.argmin(np.abs(x - v))

# Ejemplo de ejecución
x = np.arange(25, 55, 3)
v = 34
minimo(x, v)
print("La posición del elemento más cercano a", v, "es:", minimo(x, v))

#Task 3: Substracting row mean(Restar la media de la fila) Dada una matriz, su función debe devolver una nueva con las mismas dimensiones en la que a cada componente se le resta la media de su propia fila.
'''En este código, np.mean(X, axis=1, keepdims=True) calcula la media de cada fila de la matriz X y mantiene las 
dimensiones de la media para que se pueda realizar la radiodifusión adecuadamente. Luego, se resta la media de cada fila a 
la matriz original X, lo que resulta en la matriz deseada.'''

def media(X):
    # Calcula la media de cada fila
    media_filas = np.mean(X, axis=1, keepdims=True)
    
    # Resta la media de cada fila a la matriz original
    return X - media_filas

# Ejemplo de ejecución
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
media(X)
print(media(X))

#Task 4:Double the diagonal (Duplicar la diagonal)Complete la siguiente función de manera que devuelva la misma matriz recibida en X pero con su diagonal multiplicada por 2. Supongamos X es una matriz cuadrada (con el mismo número de filas y columnas).
'''En este código, np.eye(X.shape[0]) crea una matriz de identidad del mismo tamaño que la matriz X, y luego se multiplica por 2 y se suma a X para duplicar la diagonal.'''

def doublediag(X):
    # Duplica la diagonal multiplicándola por 2
    X = X + np.diag(np.diag(X) * (2 - 1))
    # Devuelve la matriz con la diagonal duplicada
    return X

# Ejemplo de ejecución
X = np.array([[79, 45, 67,  8, 37],
              [47, 40,  5, 79, 86],
              [72, 25, 44, 45, 22],
              [12, 85,  8, 53, 28],
              [ 4, 37, 36, 40, 16]])
print("La matriz de prueba inicial es\n", X)


doublediag(X)
print("La matriz con diagonal principal al doble de cada numero es\n", doublediag(X))

