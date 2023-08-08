menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
sum = 0
while True:

    try:
        item = input("Item: ")

        index = item.lower()
        sum += menu[index]

        #screen = "$"+ str(sum)
        print("total: $", f"{sum:.2f}", sep = "")
        continue

    except (KeyError):
        continue
    except  EOFError:     #sees if the user inputed control-d
        print()
        break
