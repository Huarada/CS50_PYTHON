entrada = input("equation: ")
equation = entrada.replace(" ", "")

#print(equation)

index = 0
# need to know the position of the y operand
for term in equation:
    if (term != '+') and (term != '-') and (term != '/') and (term != '*'):
        index += 1



x = float(equation[0:index - 1])
y = equation[index - 1]
z = float(equation[index:])


result = 0

if (y == '+'):
    result = x + z

elif (y == '-'):
    result = x - z

elif (y == '*'):
    result = x * z

elif (y == '/'):
    result = x /z


print(result)



