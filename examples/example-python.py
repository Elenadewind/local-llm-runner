import requests

response = requests.post(
    "http://localhost:8000/generate",
    json={
        "prompt": "Explain quantum computing simply",
        "max_tokens": 150,
        "temp": 0.7
    }
)
print(response.json()["text"])
