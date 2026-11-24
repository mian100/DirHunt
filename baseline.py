import requests
import hashlib
import uuid

# Apni local Juice Shop
base_url = "http://127.0.0.1:3000"

# Random nonexistent path banana
path = str(uuid.uuid4())

# HTTP request
response = requests.get(base_url + "/" + path, timeout=5)

# Baseline information
status = response.status_code
length = len(response.content)
content_hash = hashlib.sha256(response.content).hexdigest()

print("=== 404 Baseline ===")
print("Random Path:", path)
print("Status Code:", status)
print("Content Length:", length)
print("Content Hash:", content_hash)
