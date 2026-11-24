import requests
import time
from concurrent.futures import ThreadPoolExecutor

def test_request(number):
    response = requests.get(
        "http://127.0.0.1:3000/",
        timeout=5
    )
    return response.status_code

for workers in [1, 10]:
    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=workers) as pool:
        results = list(pool.map(test_request, range(10)))

    print("Workers:", workers)
    print("Results:", results)
    print("Time:", round(time.perf_counter() - start, 3))
