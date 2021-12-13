import requests
import json
import base64

url = "https://dev106436.service-now.com/api/now/table/incident"
username = "admin"
password = "123456Aa"
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vYzg2ZjljMDAtNTY5Yi0xMWVjLThjNmUtYjE2MmM5MjUxYmVl"

payload = {
    "description": "Al intentar llamar a una extensión recibo tono de ocupado.",
    "short_description": "Tiquete abierto desde Python",
    "category": "Network",
    "caller_id": "abraham.lincoln@example.com"
}

data = json.dumps(payload)

headers = {
  "Content-Type": "application/json"
}

response = requests.post(url, auth=(username, password), headers=headers, data=data)

print(response.text)