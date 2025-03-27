import pyfiglet
from termcolor import colored
text = pyfiglet.figlet_format("I'm Michael", font="slant")
print(colored(text,"red"))