from typing import List, Tuple
import json
from emoji import emoji_list
from collections import Counter
import time
from functools import wraps

# Construimos el decorador timeit
def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timeit
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Función que lee un archivo de tweets en formato JSON y devuelve los 10 emojis más utilizados.
    
    Args:
    file_path (str): Ruta al archivo de tweets en formato JSON.
    
    Returns:
    List[Tuple[str, int]]: Lista de tuplas con los 10 emojis más comunes y su respectiva frecuencia.
    """
    # Leer todo el contenido del archivo de una vez
    with open(file_path, 'r') as f:
        tweets = f.readlines()

    # Concatenar los contenidos de los tweets en un solo string
    single_string = ''.join(json.loads(tweet)['content'] for tweet in tweets)

    # Obtener todos los emojis presentes en el string
    emojis = [emoji['emoji'] for emoji in emoji_list(single_string)]

    # Contar los emojis y devolver los 10 más utilizados
    return Counter(emojis).most_common(10)