import numpy as np
import pandas as pd
import itertools
import time

# Función para crear una baraja de cartas
def create_deck(n_heaps, cards_per_heap, shuffle=False):
    n_cards = n_heaps * cards_per_heap # Número total de cartas en la baraja
    
    chars = [chr(i) for i in np.arange(26)+65] # Crear letras del alfabeto
    names = [i+j for i,j in itertools.product(chars, chars)]    # Combinar letras para nombres de cartas

    assert n_cards < len(names), "no puede haber más de %d cartas"%len(name)
    
    c = np.r_[names[:n_cards]]
    if shuffle:
        c = np.random.permutation(c)
    return c
create_deck(n_heaps=3, cards_per_heap=10, shuffle=False)
create_deck(n_heaps=3, cards_per_heap=7, shuffle=True)
create_deck(n_heaps=3, cards_per_heap=10, shuffle=True)

#elige una carta: la siguiente función elige aleatoriamente una carta de una baraja

def pick_card(c):
    return np.random.choice(c)

c = create_deck(n_heaps=3, cards_per_heap=7, shuffle=True)
n = pick_card(c)
n

#Tarea 1. Hacer los montones
'''Completa la siguiente función para que el escritorio dado (como lista devuelta por create_deck) 
distribuya las cartas de n_heapsacuerdo al procedimiento del truco de cartas que se muestra en el video.

Los montones deben ser una lista de n_heapslistas, cada una con len(c)/n_heapsnombres de cartas.

n_heapsserá un número impar (para que luego podamos poner el montón elegido en medio de los demás), 
y debe ser divisor del número total de cartas de la baraja (para que todos los montones tengan el mismo número de cartas)'''

'''Por ejemplo:

n_heaps = 3
c = create_deck(n_heaps=n_heaps, cards_per_heap=7)
h = make_heaps(c, n_heaps)
print("deck", c)
print("heaps")
h   

deck ['AA' 'AB' 'AC' 'AD' 'AE' 'AF' 'AG' 'AH' 'AI' 'AJ' 'AK' 'AL' 'AM' 'AN'
 'AO' 'AP' 'AQ' 'AR' 'AS' 'AT' 'AU']
heaps
[['AA', 'AD', 'AG', 'AJ', 'AM', 'AP', 'AS'],
 ['AB', 'AE', 'AH', 'AK', 'AN', 'AQ', 'AT'],
 ['AC', 'AF', 'AI', 'AL', 'AO', 'AR', 'AU']]

 o tambien 

n_heaps = 5
c = create_deck(n_heaps=n_heaps, cards_per_heap=3, shuffle=True)
h = make_heaps(c, n_heaps)
print("deck", c)
print("heaps")
h

deck ['AA' 'AJ' 'AM' 'AK' 'AH' 'AF' 'AD' 'AN' 'AB' 'AC' 'AG' 'AE' 'AL' 'AI'
 'AO']
heaps
[['AA', 'AF', 'AG'],
 ['AJ', 'AD', 'AE'],
 ['AM', 'AN', 'AL'],
 ['AK', 'AB', 'AI'],
 ['AH', 'AC', 'AO']]'''


# Función para hacer montones de cartas

def make_heaps(c, n_heaps=3):
    assert n_heaps % 2 == 1, "debe tener un número impar de montones"
    assert len(c) % n_heaps == 0, "la longitud de la baraja debe ser un múltiplo del número de montones"
    
    # Calculate how many cards each pile should have
    cartas_por_monton = len(c) // n_heaps

    # Initialize a list to store the piles
    montones = [[] for _ in range(n_heaps)]

    # Divide the cards into piles
    for i, carta in enumerate(c):
        monton_actual = i % n_heaps
        montones[monton_actual].append(carta)

    return montones

n_heaps = 3
c = create_deck(n_heaps=n_heaps, cards_per_heap=7)
h = make_heaps(c, n_heaps)

print("deck", c)
print("heaps")
print(h)

n_heaps = 5
c = create_deck(n_heaps=n_heaps, cards_per_heap=3, shuffle=True)
h = make_heaps(c, n_heaps)

print("deck", c)
print("heaps")
print(h)


#Tarea 2: Organizar los montones 
'''Complete la siguiente función para que se le dé un conjunto de montones (como los devueltos por la función de la tarea anterior) y un nombre de tarjeta:

Encuentra cuál es el montón que contiene la tarjeta.

Forma aleatoriamente dos grupos de n_heaps//2montones de los montones restantes.

si n_heaps=3estos serán dos grupos de un montón cada uno, ya que3//2=1

si n_heaps=5, serán dos grupos de dos montones cada uno, ya que5//2=2

etc. (observar //es la división de números enteros)

Concatena las tarjetas en un grupo con las tarjetas en el montón que contienen el nombre de la tarjeta dada. con las cartas del segundo grupo'''

def collect_heaps(heaps, card):
    # Inicializamos target_heap como None
    target_heap = None
    
    # Encuentra cuál es el montón que contiene la tarjeta
    for heap in heaps:
        if card in heap:
            target_heap = heap
            break
     # Si no encontramos el montón que contiene la tarjeta, retornamos None
    if target_heap is None:
        return None
    
    # Forma aleatoriamente dos grupos de montones de los montones restantes
    remaining_heaps = [heap for heap in heaps if heap != target_heap] # Creamos una lista de los montones restantes (que no contienen la tarjeta)
    np.random.shuffle(remaining_heaps) # Barajamos (shuffle) aleatoriamente los montones restantes
    
    # Asegurémonos de que solo haya un montón en el medio
    middle_heap = target_heap
    middle_index = len(remaining_heaps) // 2
    
    # Concatena las tarjetas en un grupo con las tarjetas en el montón que contiene el nombre de la tarjeta dada
    result = remaining_heaps[:middle_index] + [middle_heap] + remaining_heaps[middle_index:] # Concatenamos los montones de manera que el montón objetivo esté en el medio
    flattened_result = [card for sublist in result for card in sublist]# Aplanamos la lista de listas en una lista simple
    
    return flattened_result


# Generamos un mazo de cartas y elegimos una carta al azar
n_heaps = 3
c = create_deck(n_heaps=n_heaps, cards_per_heap=7, shuffle=True)
n = pick_card(c)
print ("card picked", n)
# Creamos montones a partir del mazo
h = make_heaps(c, n_heaps)
h   
# Recolectamos los montones con respecto a la carta elegida
new_c = collect_heaps(h, n)
print (new_c)


#Tarea 3: ejecutar el truco de cartas.
'''Complete la siguiente función de modo que, cuando se le dé una baraja de cartas c, 
una carta elegida ny un número de montones n_heaps, devuelva la posición de la carta elegida
después de realizar tres veces la recolección. El número de posición debe comenzar en cero'''

# Definición de la función 'run' que calcula la posición de una carta después de tres recolecciones de montones.
def run(c, n, n_heaps=3):
    # Inicializamos la posición en 0
    position = 0
    
    # Realizamos tres veces la recolección
    for _ in range(3):
        # Creamos los montones
        heaps = make_heaps(c, n_heaps)
        
        # Recolectamos los montones con respecto a la carta elegida
        c = collect_heaps(heaps, n)
        
        # Encontramos la nueva posición de la carta elegida
        position = c.index(n)
    
    return position

# Configuración para el primer ejemplo
n_heaps = 3
c = create_deck(n_heaps=n_heaps, cards_per_heap=7)
picked = "AA"
print("desk", c)  # Imprime el mazo de cartas inicial
pos = run(c, picked, n_heaps=n_heaps)  # Calcula la posición final de la carta elegida
print("position of card %s is %d" % (picked, pos))  # Imprime la posición final de la carta elegida

# Configuración para el segundo ejemplo
n_heaps = 3
c = create_deck(n_heaps=n_heaps, cards_per_heap=4)
picked = "AI"
print("deck", c)  # Imprime el mazo de cartas inicial
pos = run(c, picked, n_heaps=n_heaps)  # Calcula la posición final de la carta elegida
print("position of card %s is %d" % (picked, pos))  # Imprime la posición final de la carta elegida

#Tarea 4: ejecutar el truco usando las matemáticas
'''Dado:
nh:varios montones
ch:el número de tarjetas por montón
i:la posición de una tarjeta
La nueva posición de la tarjeta después de un ciclo de hacer y recolectar los montones será:
ch(nh÷2)+i÷nh
Completa la siguiente función para que tenga la misma funcionalidad de la tarea anterior, pero aplicando solo esta fórmula sin utilizar la simulación anterior
Debes obtener los mismos resultados que la tarea anterior.'''

def mrun(c, picked_card, n_heaps=3):
    assert len(c) % n_heaps == 0, "the number of heaps must be a divisor of the deck length"
    # Asegura que el número de montones sea un divisor de la longitud del mazo de cartas
    
    ch = len(c) // n_heaps  # Calcula el número de cartas por montón
    nh = n_heaps
    
    # Encuentra la posición inicial de la tarjeta en el mazo c
    i = np.argwhere(c == picked_card)[0][0]# initial position of the card on the deck c
    # Utiliza NumPy para encontrar la posición de la tarjeta seleccionada en el mazo
    
    # Calcula las nuevas posiciones de la tarjeta después de cada ronda
    p1 = (ch * (nh // 2) + i // nh) % len(c)
    # Calcula la posición después de la primera ronda
    p2 = (ch * (nh // 2) + p1 // nh) % len(c)
    # Calcula la posición después de la segunda ronda
    p3 = (ch * (nh // 2) + p2 // nh) % len(c)
    # Calcula la posición después de la última ronda
    
    return p3

n_heaps = 3  # Número de montones
c = create_deck(n_heaps=n_heaps, cards_per_heap=4)  # Crea un mazo de cartas
picked = "AI"  # Carta seleccionada
print("deck", c)  # Imprime el mazo de cartas
pos = mrun(c, picked, n_heaps=n_heaps)  # Calcula la nueva posición de la carta seleccionada
print("position of card %s is %d" % (picked, pos))  # Imprime la posición final de la carta

'''Estás listo. Ahora, algunas consideraciones 
¡Usar las matemáticas siempre es más rápido! '''


# Define el número de montones y crea un mazo de cartas con un número específico de cartas por montón
n_heaps = 3
c = create_deck(n_heaps=n_heaps, cards_per_heap=4)
picked = "AI"
print("deck", c)

# Antes de la llamada a la función
start_time = time.time()

# Llama a la función que deseas medir
result = run(c, picked, n_heaps=n_heaps)

# Después de la llamada a la función
end_time = time.time()

# Calcula el tiempo transcurrido
elapsed_time = end_time - start_time

# Imprime el tiempo transcurrido
print("Tiempo de ejecución para 'run':", elapsed_time)

# Define el número de montones y crea un mazo de cartas con un número específico de cartas por montón
n_heaps = 3
cards_per_heap = 7
c = create_deck(n_heaps, cards_per_heap)

# Antes de la llamada a la función
start_time = time.time()

# Llama a la función que deseas medir
result = mrun(c, picked, n_heaps=n_heaps)

# Después de la llamada a la función
end_time = time.time()

# Calcula el tiempo transcurrido
elapsed_time = end_time - start_time

# Imprime el tiempo transcurrido
print("Tiempo de ejecución para 'mrun':", elapsed_time)


