from LolzteamApi import LolzteamApi, Types
import requests
import re
from time import sleep

api = LolzteamApi(token='ENTER_YOUR_TOKEN', language="en")

n = 0
array = []
checker = False
game = None

with open('temp', 'r') as file:
    for line in file: # enter id cycle in array
        values = [int(x) for x in line.split()]
        array.extend(values)
        n+=1
print("Steam Inventory Parsing v1.1.")
print("Available game inventories: CS2, Dota.")
while (checker == False):
    game = input("Enter game: ")
    if (game == 'Dota' or game == 'CS2'):
        checker = True;
    else:
        print("Incorrect input. ")
sum = 0.0
for i in range(0, n):
    if (i == 19):
        sleep(60)
    total_value = 0.0
    if (game == 'CS2'):
        data = api.market.steam_value(url=f"https://steamcommunity.com/profiles/{array[i]}",currency=Types.Market.Currency.rub,app_id=Types.Market.App_Ids.CS2)
    if (game == 'Dota'):
        data = api.market.steam_value(url=f"https://steamcommunity.com/profiles/{array[i]}",currency=Types.Market.Currency.rub,app_id=Types.Market.App_Ids.Dota)
    #print(data)
    total_value = data.get('data', {}).get('totalValue', None)
    if (isinstance(total_value, float) == False):
        print(array[i],". No access to inventory, this account won't be included in the checksum.")
    if (isinstance(total_value, float) == True):
        print(f"{i+1}/{n}")
        sum+=total_value
print("Sum of all", game, "inventories =",  sum)
