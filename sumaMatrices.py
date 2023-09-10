def suma_matrices(a, b):
    # Obtenemos el número de filas y asumimos que todas las filas tienen la misma longitud
    rows = len(a)
    cols = len(a[0])
    
    # Creamos una matriz de ceros del mismo tamaño para almacenar el resultado
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Bucle externo para recorrer las filas de las matrices
    for i in range(rows):
        # Bucle interno para recorrer las columnas de las matrices
        for j in range(cols):
            # Sumamos los elementos correspondientes de las matrices 'a' y 'b'
            result[i][j] = a[i][j] + b[i][j]
    
    return result


import numpy as np
a = np.random.randint(10, size=(3,2))
b = np.random.randint(10, size=(3,2))
print (a)
print (b)
print (suma_matrices(a,b))