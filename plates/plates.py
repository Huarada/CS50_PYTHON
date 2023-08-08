def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def two_letters(s):

    return False if not(s[:2].isalpha()) else True


def length(s):
    counter = 0
    for term in s:
        counter +=1
    return counter


def term_valid(s):
    for term in s:
        if (term == '.') or (term == '!') or (term == '/') :
            return False

    return True



def is_valid(s):

    counter = length(s)
    result = True

    result = two_letters(s)
    result = term_valid(s)

    if not(2 <= counter and counter <= 6): #protection
        return  False

    #last term must be digit if letter was digit
    if (s[counter-1].isalpha() and (s[counter-2].isdigit())):
        result = False


    for letter in s:
        if letter.isnumeric():  #see first number
            if letter == '0':
                result =  False
            break

    return result


main()