
answer = input ("What is the Answer to the Great Question of Life, the Universe and Everything? ")

test = answer.lower()

if (test == "42") or (test == "forty-two" ) or (test == "forty two"):
    print("Yes")
else:
    print("No")