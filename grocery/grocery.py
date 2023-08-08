
dic = {}
while True:

    try:

        item = input("")
        if item.upper() in dic:
            dic[item.upper()] += 1
        else: dic[item.upper()] = 1
        continue

    except  EOFError:     #sees if the user inputed control-d
        print()
        for key in dic:
            print(dic[key],key)
        break
