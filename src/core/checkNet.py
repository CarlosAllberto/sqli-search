from colorama import Fore
import requests
from headers import headers

#verifica conexão com internet
def checkNet():
    try:
        requests.get("https://http.cat", headers=headers)
    except:
        print(f"{Fore.RED}[-] internet: OFF{Fore.RESET}")
        exit()