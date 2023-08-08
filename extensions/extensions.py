filename = input("File name: ")

file = filename.lower()

if '.gif' in file:
    print("image/gif")

elif ('.jpg' in file) or ('.jpeg' in file):
    print("image/jpeg")
elif (".pdf" in file) or (".PDF" in file):
    print("application/pdf")
elif (".txt" in file):
    print("text/plain")

elif ".zip" in file:
    print("image/zip")

elif ".png" in file:
    print("image/png")

else: print("application/octet-stream")