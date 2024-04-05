import requests
import json

url = "http://192.168.43.57:5000/ledon"

resp = requests.get(url)
print(resp.status_code)
print(resp.content)