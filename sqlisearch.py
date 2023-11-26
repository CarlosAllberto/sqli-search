#!/usr/bin/python3

import requests
import argparse
from os import system
from colorama import Fore, Style
from time import sleep
from googlesearch import search
from dankware import align
import subprocess

#verifica plataforma android
platform = subprocess.run("uname -o", stdout=subprocess.PIPE, shell=True)

#configuração de argumentos por cli
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

#cabecalho de requisição
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0",
    "accept-language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "referer": "https://google.com/",
}

#função imprimir banner
def banner():
    system("clear")
    #se for android
    if "android" in str(platform.stdout.lower()):
        print(align(f"{Fore.YELLOW}{Style.BRIGHT}{bannerAndroid}{Style.RESET_ALL}"))
    #se não for android
    else:
        print(align(f"{Fore.YELLOW}{Style.BRIGHT}{bannerString}{Style.RESET_ALL}"))
    print(align(f"{Fore.YELLOW}[-]              Version: 1.0.0              [-]{Fore.RESET}"))
    print(align(f"{Fore.YELLOW}[-]          Author: Carlos Alberto          [-]{Fore.RESET}"))
    print(align(f"{Fore.YELLOW}[-]   GitHub: www.github.com/CarlosAllberto  [-]{Fore.RESET}"))
    print(align(f"[*]            *****************             [*]"))
    print(align(f"{Fore.RED}SqliScan is an automation in python \nto facilitate the search of sites vulnerable to sql injection. \nit also helps when hacking using gui with tkinter and sqlmap. \ni hope it helps you.{Fore.RESET}\n"))

class SqliSearch:
    def __init__(self):
        banner()
        self.checkNet()
        self.checkFile()

    #verifica conexão com internet
    def checkNet(self):
        try:
            requests.get("https://http.cat", headers=headers)
        except:
            print(f"{Fore.RED}[-] internet: OFF{Fore.RESET}")
            exit()
        else:
            pass

    #verifica se o arquivo de dorks esta presente
    def checkFile(self):
        try:
            dorksFile = open("./dorksFile.txt", "r")
            dorksFile.close()
        except:
            print(f"{Fore.RED}[-] arquivo com dorks não encontrado{Fore.RESET}")
            print(f"{Fore.RED}tente criar: dorksFile.txt{Fore.RESET}\n")

    #verifica se o site é vulneravel sqli
    def testSqli(self, url):
        rq = requests.session()
        fileVulner = open("sites-vulneraveis.txt", "a")
        try:
            response = rq.get(f"{url}\'", headers=headers, timeout=10)
            if "mysql_fetch_array()" in response.text or "MySQL" in response.text:
                if "android" in str(platform.stdout.lower()):
                    print(f"{Fore.GREEN}[+] {url}{Fore.RESET}\n")
                else:
                    print(f"{Fore.GREEN}[+] {'Vulnerable!:':<15}{url}{Fore.RESET}\n")
                fileVulner.write(f"{url}\n")
            else:
                if "android" in str(platform.stdout.lower()):
                    print(f"[-] {url}\n")
                else:
                    print(f"[-] {'Not Vuln:':<15}{url}\n")
        except:
            pass
        fileVulner.close()

    #função principal
    def main(self):
        if search:
            dork = "inurl: php?id="
            try:
                for result in search(f"{search} {dork}", sleep_interval=5, num_results=200):
                    self.testSqli(result)
                    #adiciona um sleep de dois minutos para não ser bloqueado 
                    print(align(f"{Fore.CYAN}sleeping for 60 seconds, be patient please. \t(ᴗ˳ᴗ) zzZZzzZZ{Fore.RESET}\n"))
                    sleep(60)

            except KeyboardInterrupt:
                print("saindo\n")
                print(f"{Fore.GREEN}todos os sites vulneraveis foram salvos em: sites-vulneraveis.txt{Fore.GREEN}\n")
                exit()
            except ConnectionRefusedError:
                print("tente usar uma vpn.\n")
                exit()
            except:
                pass

        else:
            for dork in open("dorksFile.txt", "r").read().split():
                try:
                    for result in search(dork, sleep_interval=5, num_results=200):
                        self.testSqli(result)
                    #adiciona um sleep de dois minutos para não ser bloqueado 
                    print(align(f"{Fore.CYAN}[Z] sleeping for 60 seconds, be patient please. \t(ᴗ˳ᴗ) zzZZzzZZ{Fore.RESET}\n"))
                    sleep(60)
                except KeyboardInterrupt:
                    print("saindo\n")
                    print(f"{Fore.GREEN}todos os sites vulneraveis foram salvos em: sites-vulneraveis.txt{Fore.GREEN}\n")
                    exit()
                except ConnectionRefusedError:
                    print("tente usar uma vpn.\n")
                    exit()
                except:
                    pass

if __name__ == "__main__":
    if url:
        SqliSearch().testSqli(url)
    else: 
        SqliSearch().main()
