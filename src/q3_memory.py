from typing import List, Tuple
import json
from collections import Counter
from memory_profiler import profile
import time
from functools import wraps

#Construimos el timeint que nos servira para monitorear el tiempo empleado por la función
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
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Función que lee un archivo de tweets en formato JSON y devuelve los 10 usuarios más mencionados.
    
    Args:
    file_path (str): Ruta al archivo de tweets en formato JSON.
    
    Returns:
    List[Tuple[str, int]]: Lista de tuplas con los 10 usuarios más mencionados y su respectiva frecuencia.
    """
    users_counter = Counter()
    
    with open(file_path, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            mentioned_users = tweet.get('mentionedUsers', None)
            
            if mentioned_users:
                usernames = [user['username'] for user in mentioned_users]
                users_counter.update(usernames)

    return users_counter.most_common(10)