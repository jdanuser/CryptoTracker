### Get list of all IDs
### Get top 50 list 
### Run top 50 list to get top movers
### Suggest buys

### Module Imports
import requests
import json
import csv

crypto_ids_list = "https://api.coingecko.com/api/v3/coins/list"

headers = {
    "x-cg-demo-api-key" : "CG-sVDcZNtAoYfUVnW531RSBdeu"
}



def get_ids():
    response = requests.get(crypto_ids_list)

    json_data = response.json() 
    print(json.dumps(json_data, indent=4))

    output = json.loads(json_data)
    return output

ids_dict = get_ids()

def get_top_50s():
    output_list = []
    with open('C:\\Users\\Jake\\Documents\\Python\\Fluent\\Chapter1\\top_50_crypto.csv', 'r', newline='\n') as file:
        reader = csv.DictReader(file) 
        for row in reader:
            print(row)
            output_list.append(row)
    return output_list

top50 = get_top_50s()



