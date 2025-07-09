import pyfiglet
from colorama import Fore

frase = input('>>>')

frase_ascii =  pyfiglet.figlet_format(frase, font="5lineoblique")

print(Fore.CYAN + frase_ascii)