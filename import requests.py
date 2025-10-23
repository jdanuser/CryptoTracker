import requests
import json

btc = "https://api.coingecko.com/api/v3/coins/list"

headers = {
    "x-cg-demo-api-key" : "CG-sVDcZNtAoYfUVnW531RSBdeu"
}

response = requests.get(btc)

json_data = response.json() 
print(json.dumps(json_data, indent=4))

