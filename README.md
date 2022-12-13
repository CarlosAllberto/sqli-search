<h1 align=center>🔎SqlSearch🔍</h1>

## License

[![License: MIT](https://img.shields.io/github/license/gcla/termshark.svg?color=yellow)](LICENSE)

<h3 align=center>Ferramenta para busca de sites vulneraveis a SQLI</h3>

SqliSearch é um script feito em `Python3`. criado com o objetivo de poupar seu tempo procurando alvos para fazer `BugBounty`.
quanto tempo você ja gastou procurando sites vulneraveis a SQLI e fazendo testes? esse script faz a busca de `dorks` no Google 
automaticamente usando `googlesearch` e faz o teste de erro para saber se o site é vulneravel.

<div align=center>
  <img src="img.png" width="70%"/>
</div>
<br/><br/>
<div align=center>  
  <img src="download.png" width="70%"/>
</div>

## Instalação:

<div style="display: flex;">  
    <img width="30px" src="https://www.debian.org/logos/openlogo-nd.svg"/>
</div>

```
git clone https://github.com/CarlosAllberto/SqliSearch
cd SqliSearch
sudo apt install python3 python3-pip -y
pip install -r requirements.txt
```

Em uma linha:

```
git clone https://github.com/CarlosAllberto/SqliSearch && cd SqliSearch && sudo apt install python3 python3-pip -y && pip install -r requirements.txt
```

<br/>

<div style="display: flex;">  
    <img width="30px" src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Archlinux-icon-crystal-64.svg"/>
</div>

```
git clone https://github.com/CarlosAllberto/SqliSearch
cd SqliSearch
sudo pacman -S python-pip -y
pip install -r requirements.txt
```

Em uma linha:

```
git clone https://github.com/CarlosAllberto/SqliSearch && cd SqliSearch && sudo pacman -S python-pip -y && pip install -r requirements.txt
```

<br/>

## Run:

```
usage: sqlisearch.py [-h] [-s SEARCH] [-u URL]

SqliSearch

options:
  -h, --help                     show this help message and exit
  -s SEARCH, --search SEARCH     pesquisa algo especifico
  -u URL, --url URL              passe uma url para testar sqli
```

## License

[![License: MIT](https://img.shields.io/github/license/gcla/termshark.svg?color=yellow)](LICENSE)
