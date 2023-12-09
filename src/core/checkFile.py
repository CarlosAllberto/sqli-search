from colorama import Fore

#verifica se o arquivo de dorks esta presente
def checkFile():
    try:
        dorksFile = open("./dorksFile.txt", "r")
        dorksFile.close()
    except:
        print(f"{Fore.RED}[-] arquivo com dorks não encontrado{Fore.RESET}")
        print(f"{Fore.RED}tente criar: dorksFile.txt{Fore.RESET}\n")