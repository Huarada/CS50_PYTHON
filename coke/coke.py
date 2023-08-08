
price = 50
own = 0

while (own < price):
    insert = 0

    print("Amount Due:",price - own)
    insert = int(input("Insert Coin: "))
    if (insert == 5) or (insert == 25 ) or (insert == 10):
        own += insert

print("Change Owed:", own - price)