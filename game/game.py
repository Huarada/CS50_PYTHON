import random

while True:
    try:
        n = int(input("Level: "))

    except ValueError:
        continue

    if n <= 0:
        continue
    choice = random.randint(1, n)
    break

while True:

    try:
        guess = int(input("Guess: "))

        if(guess > choice):
            print("Too large!")
        elif(guess < choice):
            print("Too small!")
        else:
            print("Just right!")
            break

        continue

    except (ValueError):
        continue
    except  EOFError:     #sees if the user inputed control-d

        break
