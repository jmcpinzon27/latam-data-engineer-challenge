from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter, defaultdict
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
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Diccionario para contar los tweets por fecha
    date_counter = Counter()
    # Diccionario de diccionarios para contar los usuarios por fecha
    user_counter = defaultdict(Counter)

    with open(file_path, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            tweet_date = tweet['date'].split('T')[0]
            username = tweet['user']['username']
            date_counter[tweet_date] += 1
            user_counter[tweet_date][username] += 1
    
    # Obtener las 10 fechas más comunes
    most_common_dates = date_counter.most_common(10)
    
    # Obtener el usuario con más tweets por cada una de las fechas más comunes
    most_common_users = [user_counter[date[0]].most_common(1)[0][0] for date in most_common_dates]
    
    # Convertir las fechas a objetos datetime.date
    top_dates = [datetime.fromisoformat(date[0]).date() for date in most_common_dates]
    
    return list(zip(top_dates, most_common_users))