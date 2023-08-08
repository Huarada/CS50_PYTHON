def main():

    time = input("What time is it? ")

    agenda = convert(time)

    if (7 <= agenda) and (agenda <= 8 ):
        print("breakfast time")
    elif (12 <= agenda) and (agenda <= 13):
        print("lunch time")
    elif (18 <= agenda) and (agenda <= 19):
        print("dinner time")


def convert(time):
    index = 0
    for term in time:
        if (term != ":"):
            index += 1

    hour = int(time[:index - 2])

    minute =  int(time[index- 1:])/60

    total = hour+ minute

    return total



if __name__ == "__main__":
    main()
