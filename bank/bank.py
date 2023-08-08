greet = input("Greeting: ")

low_greet = greet.lower()

if low_greet[0:5] == "hello":
    print("$0")
elif low_greet[0] == 'h':
    print("$20")
else: print("$100")
