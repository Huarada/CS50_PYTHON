
camel = input("CamelCase: ")

snake = []

for letter in camel:
    if letter.isupper():
        snake.append("_")
    snake.append(letter.lower())

str = "".join(snake)
print(str)