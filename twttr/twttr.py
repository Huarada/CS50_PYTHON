entrada = input("Input: ")

saida= []
for letter in entrada:
    minus = letter.lower()
    if (minus != 'a') and (minus != 'e') and (minus != 'i') and (minus != 'o') and (minus != 'u'):
        saida.append(letter)

junto = "".join(saida)

print(junto)