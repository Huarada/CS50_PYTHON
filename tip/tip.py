def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    without = d.replace("$","")
    num = float(without)
    return num

def percent_to_float(p):

    without1 = p.replace("%","")
    without2 = without1.replace("$","")
    num = float(without2)/100
    return num


main()