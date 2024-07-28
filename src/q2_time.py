from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter
from emoji import emoji_list
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
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Función que lee un archivo de tweets en formato JSON y devuelve los 10 emojis más utilizados.
    
    Args:
    file_path (str): Ruta al archivo de tweets en formato JSON.
    
    Returns:
    List[Tuple[str, int]]: Lista de tuplas con los 10 emojis más comunes y su respectiva frecuencia.
    """
    emoji_counter = Counter()
    
    with open(file_path, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            tweet_content = tweet.get('content', '')
            
            tweet_emojis = [emoji['emoji'] for emoji in emoji_list(tweet_content)]
            emoji_counter.update(tweet_emojis)
    
    return emoji_counter.most_common(10)