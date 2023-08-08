def main():
    msg = input()

    outcome = convert(msg)
    print(outcome)



def convert(str):

    str1 = str.replace(":)", '🙂' )

    str2 = str1.replace(":(", '🙁')

    return str2

main()