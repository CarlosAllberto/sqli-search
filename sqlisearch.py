#!/usr/bin/python3

import requests
from sys import exit
import argparse
from os import system
from colorama import Fore
from time import sleep
from googlesearch import search
from dankware import align
from src.core.banner import banner
from src.core.checkFile import checkFile
from src.core.checkNet import checkNet
from src.core.printVuln import printVuln
from headers import headers

# recebe os argumentos passados
parse = argparse.ArgumentParser(description="SqliSearch")
parse.add_argument("-f", "--find", type=str, help="pesquisa algo especifico")
parse.add_argument("-u", "--url", type=str, help="passe uma url para testar sqli")
args = parse.parse_args()
find = args.find
url = args.url

class SqliSearch:
    def __init__(self):
        banner()
        checkNet()
        checkFile()

    # verifica se o site é vulnerável à sqli
    def testSqli(self, url):
        fileVulner = open("sites-vulneraveis.txt", "a")
        rq = requests.session()
        try:
            response = rq.get(f"{url}\'", headers=headers, timeout=10).text
            if "mysql_fetch_array()" in response or "MySQL" in response:
                printVuln(url, True)
                fileVulner.write(f"{url}\n")
            else:
                printVuln(url, False)
        
        except KeyboardInterrupt:
            exit(f"{Fore.GREEN}todos os sites vulneraveis foram salvos em: sites-vulneraveis.txt{Fore.GREEN}\n")
        except:
            pass
        fileVulner.close()

    # função principal
    def main(self):
        if find:
            try:
                for result in search(f"{find} inurl: php?id=", num_results=200):
                    self.testSqli(result)

            except KeyboardInterrupt:
                exit(f"{Fore.GREEN}todos os sites vulneraveis foram salvos em: sites-vulneraveis.txt{Fore.GREEN}\n")
            except ConnectionRefusedError:
                exit("tente usar uma vpn.\n")

        else:
            cont = 0
            for dork in open("dorksFile.txt", "r").read().split():
                try:
                    for result in search(dork, num_results=5):
                        self.testSqli(result)
                    if cont >= 10:
                        # adiciona um sleep de dois minutos para não ser bloqueado pelo Google
                        print(align(f"{Fore.CYAN}[Z] sleeping for 120 seconds, be patient please. \t(ᴗ˳ᴗ) zzZZzzZZ{Fore.RESET}\n"))
                        sleep(120)
                        cont = 0
                    else:
                        cont += 1

                except KeyboardInterrupt:
                    exit(f"{Fore.GREEN}todos os sites vulneraveis foram salvos em: sites-vulneraveis.txt{Fore.GREEN}\n")
                except ConnectionRefusedError:
                    exit("tente usar uma vpn.\n")
                except:
                    exit("erro desconhecido. por favor relate em: https://github.com/CarlosAllberto/SqliSearch/issues")

if __name__ == "__main__":
    if url:
        SqliSearch().testSqli(url)
    else: 
        SqliSearch().main()
