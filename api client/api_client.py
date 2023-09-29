import requests
import json


url = "http://127.0.0.1:8000/api/movies/"

response = requests.get(url)
response.json()

print(response.content)