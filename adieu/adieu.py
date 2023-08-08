


names = []

while True:

    try:
        name = input("Name: ")
        names.append(name)
        continue

    except (KeyError):
        continue
    except  EOFError:     #sees if the user inputed control-d
        print()
        joined = ", ".join(names[:-1])

        if len(names) == 1:
            print("Adieu, adieu, to",names[0])
        else:
            print("Adieu, adieu, to ",joined , ", and ",names[-1], sep = "")

        break
