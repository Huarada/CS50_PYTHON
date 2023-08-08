
while True:
    try:
        fuel = input("Fraction: ")
        index = fuel.find("/")
        x = int(fuel[:index])
        y = int(fuel[index + 1:])
        z = int((x/y) *100)
        letter = str(z) + "%"
        joined = letter.replace(" ","")

        if x > y :
            continue
        if (x == y or z == 99):
            print("F")
        elif (x == 0 or z == 1):
            print("E")
        else:
            print(joined)
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else: break


