
def main():
    greeting = input("greeting: ")
    print(value(greeting))


def value(greeting):

    low_greet = greeting.lower()

    if low_greet[0:5] == "hello":
        value = 0
    elif low_greet[0] == 'h':
        value = 20
    else: value = 100

    return value

if __name__ == "__main__":
    main()


