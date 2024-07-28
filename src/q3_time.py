from typing import List, Tuple
from collections import Counter
import json
import os
import time
from functools import wraps

def timeit(func):
    """
    Decorador para medir el tiempo de ejecución de una función.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timeit
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Función que lee un archivo de tweets en formato JSON y devuelve los 10 usuarios más mencionados,
    optimizada para tiempo de ejecución.

    Args:
    file_path (str): Ruta al archivo de tweets en formato JSON.

    Returns:
    List[Tuple[str, int]]: Lista de tuplas con los 10 usuarios más mencionados y su respectiva frecuencia.
    """
    users_counter = Counter()
    
    with open(file_path, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            mentioned_users = tweet.get('mentionedUsers')
            
            if mentioned_users:
                for user in mentioned_users:
                    users_counter[user['username']] += 1
    
    return users_counter.most_common(10)