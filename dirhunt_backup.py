import requests

# Local Juice Shop URL
base_url = "http://127.0.0.1:3000"

# Wordlist read karna
with open("wordlist.txt", "r") as file:
    words = file.readlines()

# Har lab path ko check karna
for word in words:
    path = word.strip()

    if path not in ["/", "testing-not-found-123",
                    "testing-not-found-456"]:
        continue

    url = base_url + "/" + path.lstrip("/")

    response = requests.get(url, timeout=5)

    print("URL:", url)
    print("Status:", response.status_code)
    print("Length:", len(response.content))
    print("--------------------")

