import requests
import json

url = "http://192.168.43.174:5000/send_data"
temp = 999
humidity = 999
noise = 999
lum = 999
data = {"temperatura": temp, "umidade": humidity, "ruido": noise, "luminosidade": lum}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

resp = requests.post(url, headers=headers, data=json.dumps(data))
print(resp.status_code)

# $ curl -X POST -H "Content-type: application/json" -d "{\"name\" : \"John\", \"age\" : \"5\"}" "localhost:5000/string_example"
