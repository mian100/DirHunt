import requests
import hashlib
import uuid
import argparse
import time
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "http://127.0.0.1:3000"

def fingerprint(response):
    return (
        response.status_code,
        len(response.content),
        hashlib.sha256(response.content).hexdigest()
    )

def fetch(path):
    return requests.get(
        BASE_URL + path,
        timeout=5,
        allow_redirects=False
    )

parser = argparse.ArgumentParser(description="DirHunt Lab Test")
parser.add_argument("-t", type=int, choices=[1, 10], default=1)
parser.add_argument("-o", default="results.txt")
args = parser.parse_args()

# Missing page baseline
baseline = fingerprint(fetch("/" + str(uuid.uuid4())))

print("=== DirHunt ===")
print("Baseline:", baseline)

paths = [
    "/",
    "/testing-not-found-123",
    "/testing-not-found-456"
]

def check(path):
    try:
        response = fetch(path)
        status = response.status_code

        if fingerprint(response) == baseline:
            result = "Baseline match - Filtered"
        elif status == 404:
            result = "Not Found"
        else:
            result = "Different response - Verify manually"

        return f"{path} | {status} | {result}"

    except requests.RequestException as error:
        return f"{path} | Error: {error}"

start = time.perf_counter()

with ThreadPoolExecutor(max_workers=args.t) as pool:
    results = list(pool.map(check, paths))

results.append(
    f"Time: {time.perf_counter() - start:.3f} seconds"
)

report = "\n".join(results)
print(report)

with open(args.o, "w") as file:
    file.write(report)

print("Report saved:", args.o)
