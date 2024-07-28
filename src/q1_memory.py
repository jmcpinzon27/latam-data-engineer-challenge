from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict
import time
from memory_profiler import memory_usage

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Usamos el decorador para imprimir el análisis del uso de memoria de la función
@timeit
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Usamos defaultdict para contar los tweets por cada usuario y por cada fecha
    dates_dict = defaultdict(lambda: defaultdict(int))

    with open(file_path, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            tweet_date = tweet['date'].split('T')[0]
            username = tweet['user']['username']
            dates_dict[tweet_date][username] += 1

    # Ordenamos las fechas de acuerdo a la cantidad total de tweets en orden descendente
    top_dates = sorted(dates_dict.keys(), key=lambda date: sum(dates_dict[date].values()), reverse=True)[:10]

    # Obtenemos el usuario con más tweets por cada una de las fechas principales
    top_users = [max(dates_dict[date], key=dates_dict[date].get) for date in top_dates]

    # Convertimos las fechas a objetos datetime.date usando fromisoformat para que queden según ISO 8601
    top_dates = [datetime.fromisoformat(date_str).date() for date_str in top_dates]

    return list(zip(top_dates, top_users))