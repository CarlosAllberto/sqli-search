import subprocess
from colorama import Fore

#verifica plataforma android
platform = subprocess.run("uname -o", stdout=subprocess.PIPE, shell=True).stdout.lower()

def printVuln(url, vuln):
    if vuln:
        if "android" in str(platform):
            print(f"{Fore.GREEN}[+] {url}{Fore.RESET}\n")
        else:
            print(f"{Fore.GREEN}[+] {'VULN:':<15}{url}{Fore.RESET}\n")
    else:
        if "android" in str(platform):
            print(f"[-] {url}\n")
        else:
            print(f"[-] {'NOT VULN:':<15}{url}\n")