import requests
import hashlib
import uuid

base_url = "http://127.0.0.1:3000"

def fingerprint(response):
    return (
        response.status_code,
        len(response.content),
        hashlib.sha256(response.content).hexdigest()
    )

# Random missing page
baseline = requests.get(
    base_url + "/" + str(uuid.uuid4()),
    timeout=5
)

print("=== DirHunt Lab Test ===")
print("Baseline:", fingerprint(baseline))

# Known homepage
response = requests.get(base_url + "/", timeout=5)

print("Homepage:", fingerprint(response))

if fingerprint(response) == fingerprint(baseline):
    print("Homepage matches fallback response")
else:
    print("Homepage response is different")
