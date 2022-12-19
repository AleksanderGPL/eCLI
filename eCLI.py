import sys
import os
import platform
import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.BLUE + "eCLI on " + Fore.RED + platform.system(),platform.machine())
print(Fore.BLUE + "Type " + Fore.RED + "help" + Fore.BLUE + " for help.")
print(" ")


while True:
    command = input(Fore.BLUE + "eCLI>" + Fore.GREEN + " ")
    if command == "exit":
        print("Goodbye!")
        sys.exit()
    elif command == "clear":
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    elif command == "pcinfo":
        print(Fore.YELLOW + "=============================================================")
        print(Fore.RED + "PC Name: " + Fore.GREEN + platform.node())
        print(Fore.RED + "PC Type: " + Fore.GREEN + platform.machine())
        print(Fore.RED + "Architecture: " + Fore.GREEN + platform.architecture()[0])
        print(Fore.RED + "OS: " + Fore.GREEN + platform.system())
        print(Fore.RED + "OS Version: " + Fore.GREEN + platform.version())
        print(Fore.RED + "OS Release: " + Fore.GREEN + platform.release())
        print(Fore.RED + "OS Platform: " + Fore.GREEN + platform.platform())
        print(Fore.YELLOW + "=============================================================") 
    elif command == "help":
        print(Fore.YELLOW + "=============================================================")
        print(Fore.RED + "eCLI Help")
        print(Fore.YELLOW + "=============================================================")
        print(Fore.RED + "pcinfo" + Fore.GREEN + " - Displays information about the computer")
        print(Fore.RED + "info" + Fore.GREEN + " - Displays information about eCLI")
        print(Fore.RED + "help" + Fore.GREEN + " - Displays this help menu")
        print(Fore.RED + "clear" + Fore.GREEN + " - Clears the screen")
        print(Fore.RED + "exit" + Fore.GREEN + " - Exits the program")
        print(Fore.YELLOW + "=============================================================")
    elif command == "info":
        print(Fore.YELLOW + "=============================================================")
        print(Fore.RED + "eCLI Info")
        print(Fore.YELLOW + "=============================================================")
        print(Fore.RED + "Version: " + Fore.GREEN + "1.0")
        print(Fore.RED + "Author: " + Fore.GREEN + "@AleksanderGPL")
        print(Fore.RED + "Github: " + Fore.GREEN + "https://github.com/AleksanderGPL/eCLI")
        print(Fore.YELLOW + "=============================================================")
    else:
        print(Fore.RED + "Unknown command: " + Fore.GREEN + command)
        print(Fore.BLUE + "Type " + Fore.RED + "help" + Fore.BLUE + " for help.")
        print(" ")