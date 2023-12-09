import subprocess
from colorama import Fore, Style
from dankware import align
from os import system

bannerString = """
███████╗ ██████╗ ██╗     ██╗███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔════╝██╔═══██╗██║     ██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
███████╗██║   ██║██║     ██║███████╗█████╗  ███████║██████╔╝██║     ███████║
╚════██║██║▄▄ ██║██║     ██║╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
███████║╚██████╔╝███████╗██║███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
"""

bannerAndroid = """
███████  ██████  ██      ██ 
██      ██    ██ ██      ██ 
███████ ██    ██ ██      ██ 
     ██ ██ ▄▄ ██ ██      ██ 
███████  ██████  ███████ ██ 
            ▀▀              
███████ ███████  █████  ██████   ██████ ██   ██ 
██      ██      ██   ██ ██   ██ ██      ██   ██ 
███████ █████   ███████ ██████  ██      ███████ 
     ██ ██      ██   ██ ██   ██ ██      ██   ██ 
███████ ███████ ██   ██ ██   ██  ██████ ██   ██                                              
"""

#verifica plataforma android
platform = subprocess.run("uname -o", stdout=subprocess.PIPE, shell=True)

#função imprimir banner
def banner():
    system("clear")
    #se for android
    if "android" in str(platform.stdout.lower()):
        print(align(f"{Fore.YELLOW}{Style.BRIGHT}{bannerAndroid}{Style.RESET_ALL}\n"))
    #se não for android
    else:
        print(align(f"{Fore.YELLOW}{Style.BRIGHT}{bannerString}{Style.RESET_ALL}"))
    print(align(f"{Fore.YELLOW}[-]               Version: 1.1               [-]{Fore.RESET}"))
    print(align(f"{Fore.YELLOW}[-]          Author: Carlos Alberto          [-]{Fore.RESET}"))
    print(align(f"{Fore.YELLOW}[-]   GitHub: www.github.com/CarlosAllberto  [-]{Fore.RESET}"))
    print(align(f"[*]            *****************             [*]"))
    print(align(f"{Fore.RED}SqliScan is an automation in python \nto facilitate the search of sites vulnerable to sql injection. \nit also helps when hacking using gui with tkinter and sqlmap. \ni hope it helps you.{Fore.RESET}\n"))
    print()