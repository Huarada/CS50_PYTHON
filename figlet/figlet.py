import sys
from pyfiglet import Figlet
import random



figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) == 1 :
    figlet.setFont(font = random.choice(fonts))

elif len(sys.argv) == 3:
    figlet.setFont(font= sys.argv[2])

else:
    sys.exit("Invalid usage")


anwser = input("Input: ")
print(figlet.renderText(anwser))
#print(figlet.renderText(s))