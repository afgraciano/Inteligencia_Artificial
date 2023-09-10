import numpy as np
import pandas as pd

#Tarea 1: Extraer datos. tenemos un dataframe de artículos con un precio y, en ocasiones , con una columna extra ( margin).
def create_df(missing=False, n=10):
    # La función create_df genera un DataFrame simulado con datos aleatorios.
    # Parámetros:
    # - missing: Booleano que indica si se deben simular valores faltantes en la columna de precios.
    # - n: Número de elementos a generar en el DataFrame (por defecto, 10 elementos).

    # Genera identificadores de elementos aleatorios entre 1000 y 100000
    itemid   = np.random.randint(100000, size=n)+1000
    # Asigna aleatoriamente categorías (valores enteros entre 0 y 2) a los elementos
    category = np.random.randint(3, size=n)
    # Simula los precios de los elementos con una distribución normal, con media en 100 y desviación estándar de 10
    price    = np.round(np.random.normal(loc=100, scale=10, size=n),2)
    # Simula los márgenes de los elementos con una distribución normal, con media en 10 y desviación estándar de 1
    margin   = np.round(np.random.normal(loc=10, scale=1, size=n),2)
    # Si se especifica missing como True, simula valores faltantes en la columna de precios
    if missing:
        # Determina aleatoriamente cuántos valores faltantes se deben generar, entre 2 y la mitad de los elementos
        nmissing = np.random.randint(len(price)//2)+2                                     
        # Selecciona índices aleatorios y establece esos valores en NaN para simular valores faltantes en la columna de precios
        price[np.random.permutation(len(price))[:nmissing]] = np.nan
    # Crea un DataFrame a partir de las columnas de precio, categoría y margen, con el índice basado en itemid
    d = pd.DataFrame(np.r_[[price, category, margin]].T, index=itemid, columns=["price", "category", "margin"])
    # Asigna el nombre "itemid" al índice del DataFrame
    d.index.name="itemid"
    # Con una probabilidad del 50%, elimina una columna aleatoria del DataFrame
    if np.random.random()>.5:
        d = d[d.columns[:2]]
    # Devuelve el DataFrame generado    
    return d
# Llama a la función create_df y almacena el DataFrame simulado en la variable d
d = create_df()
#imprime la tabla d
print("\nTabla1:\n",d,"\n")



def select_items(df):
    # Asegúrate de hacer una copia en caso de que modifiques el dataframe original
    df = df.copy()
    
    # Filtra las filas con precio mayor que 100
    mask_price = df['price'] > 100
    
    # Inicializa una máscara para las filas con margen mayor que 10 (si la columna existe)
    mask_margin = np.zeros(len(df), dtype=bool)
    
    # Verifica si la columna 'margin' está presente en el DataFrame
    if 'margin' in df.columns:
        mask_margin = df['margin'] > 10
    
    # Combina las máscaras para obtener las filas que cumplen cualquiera de los criterios
    mask_combined = mask_price | mask_margin
    
    # Devuelve una lista con los identificadores de elementos de las filas seleccionadas
    result = df.index[mask_combined].tolist()
    
    return result

d = create_df()
print("Tabla2:\n",d)
select_items(d)
print("\nItemid seleccionado cuyo margen > 10 si existe y cuyo precio > 100: ", select_items(d),"\n")



#Tarea 2: Estadísticas de grupo.Complete la siguiente función para que devuelva un marco de datos con los precios promedio, máximo y mínimo por categoría.

'''Este código toma el DataFrame df, lo copia para evitar modificaciones accidentales y luego realiza las siguientes operaciones:

Agrupa el DataFrame por la columna 'category' y calcula la media, el máximo y el mínimo de los precios ('price') en cada grupo utilizando df.groupby('category')['price'].agg(['mean', 'max', 'min']).

Renombra las columnas del resultado según las especificaciones del problema.

Reinicia el índice del DataFrame resultante para que 'category' sea una columna en lugar del índice mediante result.reset_index(inplace=True).

Finalmente, devuelve el DataFrame resultante.'''

def get_stats(df):
    # Asegúrate de hacer una copia en caso de que modifiques el dataframe original
    df = df.copy()
    
    # Agrupa el DataFrame por la columna 'category' y calcula la media, máximo y mínimo de 'price' en cada grupo
    result = df.groupby('category')['price'].agg(['mean', 'max', 'min'])
    
    # Renombra las columnas del resultado según las especificaciones
    result.columns = ['media', 'maximo', 'minimo']
    
    # Reinicia el índice del DataFrame resultante para que 'category' sea una columna en lugar del índice
    result.reset_index(inplace=True)
    
    # Convierte el índice a tipo int
    result['category'] = result['category'].astype(int)
    
    # Establece 'category' como el índice del DataFrame
    result.set_index('category', inplace=True)
    
    # Cambia el nombre del índice a 'categoria'
    result.index.name = 'categoria'

    #result = ...

    return result

# Comprueba manualmente tu respuesta con el DataFrame creado previamente
d = create_df()
print(d)
get_stats(d)
print(get_stats(d))



#Tarea 3: Completar los datos faltantes. Complete los datos que faltan en la columna de precio con el siguiente procedimiento:

'''calcular la media y el estándar de los precios disponibles
muestra de una distribución normal con la media calculada y el estándar (ver [ np.random.normal])
( https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html ), tantas muestras como datos faltantes
sustituir los valores faltantes con las muestras'''
d = create_df(missing=True)
print("\n",d)
def fillna(df):
    # Asegúrate de hacer una copia en caso de que modifiques el dataframe original
    df = df.copy()
    
    # Paso 1: Calcular la media y el estándar de los precios disponibles
    mean_price = df['price'].mean()
    std_price = df['price'].std()
    
    # Paso 2: Muestra de una distribución normal con la media y el estándar
    missing_count = df['price'].isna().sum()
    samples = np.random.normal(mean_price, std_price, missing_count)
    
    # Paso 3: Sustituir los valores faltantes con las muestras
    df.loc[df['price'].isna(), 'price'] = samples
    
    return df

# Comprueba manualmente tu respuesta
d = create_df(missing=True)
print("\n",d)
fillna(d)
print("\n",fillna(d),"\n")