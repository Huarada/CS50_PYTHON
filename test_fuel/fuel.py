
def main():
    fraction = input("fraction: ")
    z = convert(fraction)
    percent = gauge(z)

    print(percent)





def convert(fraction):
    index = fraction.find("/")
    x = int(fraction[:index])
    y = int(fraction[index + 1:])

    if x > y :
        raise ValueError
    elif y == 0 :
        raise ZeroDivisionError
    else:
        z = int((x/y) *100)
        return z

def gauge(percentage):

    if (percentage >= 99):
        percent = "F"
    elif (percentage <= 1):
        percent =  "E"
    else:
        percent = str(percentage) + '%'
    return percent



if __name__ == "__main__":
    main()