import colorama
from colorama import init, Fore, Back, Style


init()
print(" Normal white color")
Back.RED + "🐪 " + Style.RESET_ALL 
Back.BLUE + "🐪 " + Style.RESET_ALL
Back.GREEN + "🐪 " + Style.RESET_ALL 
Back.YELLOW + "🐪 " + Style.RESET_ALL 
Back.MAGENTA + "🐪 " + Style.RESET_ALL



space_apart = 10
space = " "
print(Back.RED + "🐪 " + Style.RESET_ALL + (space*space_apart) + Back.BLUE + "🐪 " + Style.RESET_ALL)

print(Back.GREEN + "🐪 " + Style.RESET_ALL)
print(Back.YELLOW + "🐪 " + Style.RESET_ALL)
print(Back.MAGENTA + "🐪 " + Style.RESET_ALL)

print("🐪") 