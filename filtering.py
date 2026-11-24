import requests
import hashlib

base_url = "http://127.0.0.1:3000"

# Response ka fingerprint banana
def fingerprint(response):
    return (
        response.status_code,
        len(response.content),
        hashlib.sha256(response.content).hexdigest()
    )

# Missing page ka baseline
baseline = requests.get(
    base_url + "/testing-not-found-123",
    timeout=5
)

# Doosra missing page test karna
response = requests.get(
    base_url + "/testing-not-found-456",
    timeout=5
)

print("Status:", response.status_code)
print("Length:", len(response.content))

if fingerprint(response) == fingerprint(baseline):
    print("Soft-404 detected - Filtered")
elif response.status_code == 404:
    print("Not Found")
else:
    print("Different response - Needs verification")
