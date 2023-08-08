
def main():
    word = input("word: ")

    print(shorten(word))




def shorten(word):
    saida= []
    for letter in word:
        minus = letter.lower()
        if (minus != 'a') and (minus != 'e') and (minus != 'i') and (minus != 'o') and (minus != 'u'):
            saida.append(letter)

    junto = "".join(saida)

    return junto

if __name__ == "__main__":
    main()

