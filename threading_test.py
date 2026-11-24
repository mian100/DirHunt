from concurrent.futures import ThreadPoolExecutor
import time

# Sample lab responses
paths = ["/", "/test1", "/test2", "/test3", "/test4",
         "/test5", "/test6", "/test7", "/test8", "/test9"]

def check_path(path):
    # Request processing ki simulation
    time.sleep(0.5)
    return path

def run_test(workers):
    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(check_path, paths))

    end = time.perf_counter()

    print("Workers:", workers)
    print("Results:", results)
    print("Time:", round(end - start, 2), "seconds")
    print("----------------------")

run_test(1)
run_test(10)
