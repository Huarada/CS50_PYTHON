import requests
import sys
import json


if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")

else :
    print("Missing comand-line argument")
    sys.exit(1)


import requests

try:
    site = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    resposta = site.json()
    #verify the value of one bitcoin
    bitcoin = resposta['bpi']['USD']['rate_float']
    quantity = bitcoin* value

    print(f"${quantity:,.4f}")
except requests.RequestException:
    print("Exception")