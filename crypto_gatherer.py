### Get list of all IDs
### Get top 50 list 
### Run top 50 list to get top movers
### Suggest buys

### Module Imports
import requests
import json
import csv
from datetime import datetime



crypto_ids_list = "https://api.coingecko.com/api/v3/coins/list"

headers = {
    "x-cg-demo-api-key" : "REDACTED"
}



def get_ids():
    response = requests.get(crypto_ids_list)

    json_data = response.json() 
    # print(json.dumps(json_data, indent=4))

    output = json_data
    return output

ids_dict = get_ids()

def get_top_50s():
    output_list = []
    with open('C:\\Users\\Jake\\Documents\\Python\\Fluent\\Chapter1\\top_50_crypto.csv', 'r', newline='\n') as file:
        reader = csv.DictReader(file) 
        for row in reader:
            #print(row)
            output_list.append(row)
    return output_list

top50_no_info = get_top_50s()

class CryptoTicker:
    def _get_cg_data(self, name):
        result = next((c for c in ids_dict if c["name"] == name), None)
        return result
    
    def __init__(self, name, symbol): 
        self.name = name
        self.symbol = symbol
        self.cgdata = self._get_cg_data(name)
        
        try: 
            self.cgid = self.cgdata['id']
            self.info = self.get_info()
            self.price_btc = self.info['market_data']['current_price']['btc']
            self.price_usd = self.info['market_data']['current_price']['usd']
            self.price_eth = self.info['market_data']['current_price']['eth']
        except:
            print(self.name + "is not working.")

    def __getitem__(self):
       return self.name, self.symbol, self.price_btc        

    def get_info(self):
        url = "https://api.coingecko.com/api/v3/coins/" + self.cgid
        headers = {"x-cg-demo-api-key" : "CG-sVDcZNtAoYfUVnW531RSBdeu"}
        response = requests.get(url, headers=headers)
        return response.json()
    
    def refresh_info(self):
        return self.get_info()
    
    def __str__(self):
        return "Name: " + self.name + " Symbol: " + self.symbol + "BTC Price: " + self.price_btc + "\n"
    
top50 = []

def get_top_50():
    global top50
    for row in top50_no_info:
        addition = CryptoTicker(row["Name"], row["Symbol"])   
        top50.append(addition)



refresh_time = datetime.now()


