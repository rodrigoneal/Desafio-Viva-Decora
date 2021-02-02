
# <center>Desafio-Viva-Decora  </center>
  
### Bem Vindo a documentação do Web Scraping. 

## <center>Como Instalar:</center>

    pip install git+https://github.com/rodrigoneal/Desafio-Viva-Decora.git#egg=web-scraping

## <center>Como Usar:</center>

    from github.web_scraping import GitHub
    
    git = GitHub("repositorios.txt")
    git.main(verbose=True)
Importe a classe GitHub que fica dentro do pacote github.web_scraping. 
A classe recebe um parâmetro obrigatório que é o arquivo txt com a lista de repositórios do github que serão 
*crawlada*.

O método  `main(verbose=False)` recebe um parâmetro booleano posicional opcional *verbose* por default=False. Coloque `True` para que o programa imprima no terminal as URLs das pastas e arquivos que estão sendo *crawlado*.

    https://github.com/frontpressorg/frontpress/blob/master/.editorconfig
    https://github.com/frontpressorg/frontpress/blob/master/.gitignore
    https://github.com/frontpressorg/frontpress/blob/master/.jshintignore
    https://github.com/frontpressorg/frontpress/blob/master/.jshintrc
    https://github.com/frontpressorg/frontpress/blob/master/.nvmrc
    https://github.com/frontpressorg/frontpress/blob/master/.travis.yml
    https://github.com/frontpressorg/frontpress/blob/master/LICENSE.md
    https://github.com/frontpressorg/frontpress/blob/master/README.md
    https://github.com/frontpressorg/frontpress/blob/master/bower.json
    https://github.com/frontpressorg/frontpress/blob/master/contributing.md
    https://github.com/frontpressorg/frontpress/blob/master/deploy_key.enc
    https://github.com/frontpressorg/frontpress/blob/master/frontpress.json.v1.sample
    https://github.com/frontpressorg/frontpress/blob/master/frontpress.json.v2.sample
    https://github.com/frontpressorg/frontpress/blob/master/gulpfile.js
    https://github.com/frontpressorg/frontpress/blob/master/karma.conf.js
    https://github.com/frontpressorg/frontpress/blob/master/package.json

Se for `False` ele apenas irá imprimir o repositório que está sendo *crawlado* na hora.

    rodrigoneal/hoteis_api


#### Formatação do arquivo txt
Obrigatoriamente o arquivo precisa terminar com  .txt e formatado da seguinte maneira:

    rodrigoneal/hoteis_api  
    SambitAcharya/Mini-Projects  
    frontpressorg/frontpress

Só utilize "/" entre o nome do usuário e o nome do repositório, evite colocar espaços desnecessários.


# <center>API </center>
  

## Arquivo: `web-scraping.py`

  
### Classe GitHub: 
  

   #### `def __init__(file_txt):`

Método que inicializa a classe GitHub
**Parametro**: file.txt;  **Tipo**:FileIO- Arquivo txt com a lista de repositórios que serão varridos 
  
**Variável**: `self.url = "https://github.com/"`; **Tipo**:str - Variável de instância da classe GitHub que armazena a url base do github.
  
**Variável**: `self.repositorio = ""`; **Tipo**: str - Variável de instância da classe GitHub que armazena a url do   
repositorio do GitHub que é concatenado com a self.base_url
Exemplo: `https://github.com/frontpressorg/frontpress`  

**Variável**: `self.file_txt = file_txt`; **Tipo**:FileIO - Variável de instância da classe GitHub que armazena o nome do arquivo .txt  que é usado pela classe GitHub.  

  
**Variável**: `self.dados = []`; **Tipo**:list - Variável de instância da classe GitHub que armazena uma lista com os dados dos arquivos já formatado.  

Obs: 

*Arquivo é o arquivo pego dentro do GitHub exemplo: "hoteis_api/hotel/app.py". O app.py é um arquivo*
 
  
**Variável**: `self.filter = ["gitignore", "Dockerfile", "Makefile"]`;  **Tipo**:list- Variável de instância da classe GitHub que armazena uma lista com as extensões que não serão  
listado e listado como outro  

**Variável**: `self.diretorio=[]`; **Tipo**:list - Variável de instância da classe GitHub que armazena uma lista de dicionários com os dados que serão gravados no arquivo .txt
  
  

   #### `request(path="")`

Método que faz uma requisição GET no site do github e retorna um objeto do tipo *BeautifulSoup* 
**Parâmetro**: path="" **Tipo**:str- string com a url da pasta ou arquivo que forma o link absoluto da pagina 

Exemplo: 
Link relativo ao arquivo app.py : `blob/master/hotel/app.py`
Link absoluto do arquivo app.py: `https://github.com/rodrigoneal/hoteis_api/blob/master/hotel/app.py`


#### `request_all_links()`
Método que navega por todas as pastas e arquivos de forma recursiva.
Ele é o core da aplicação pois pega todos os links e dentro dentro há chamadas de outras funções e métodos que dão vida ao programa.
  
#### `main()`
Método inicia o programa
**Parâmetro**: `verbose=True` **Tipo**:boolean- **Default**=False Esse parâmetro indica se o programa deverá imprimir todos 
as URLs que o programa está percorrendo em tempo real.

## Arquivo: `parse_data.py`
  
  
#### `sum_value_dict(list_to_parser, filter)` 
Função que pega uma lista com dicionário e tupla. Soma os valores de dentro dessa lista filtrando suas extensões 
Exemplo: 
Entrada >>> `[['py', (5, 5)], ['py', (5, 5)]]` Saída >>>`[{'py':(10, 10)}]`  
**Parâmetro**: `list_to_parser` **Tipo**:list- Lista com os arquivos que serão somados e filtrados. 
**Parâmetro**: `filter` **Tipo**:list- Lista com os arquivos que deverão ser ignorados e armazenados como outros . 

#### `get_data_file(soup)`
Função que pega os arquivos da URL e extrai o a extensão, numero de linhas e quantidade de bytes do arquivo

    extensão:save.py, numero de linhas: 59, bytes: 2.24

Obs: Quando eu falo arquivo é a URL que contem o programa em si, exemplo .py, .js .php. 
Obs: Ele converte  numero de linhas e quantidade de bytes para `int` isso pode fazer com que a porcentagem descrita no arquivo .txt tenha menos de 100% por causa desse arredondamento 

## Arquivo: `save.py`

#### `save_tree_structure(repository, path_dict)` 
Função que abre o arquivo e  grava um arquivo txt com a estrutura em arvore.
*Por padrão ela gravar o arquivo no modo "a".*

    |__ [hotel]  
    |   |__ [ext]  
    |   |   |__ __init__.py (0 linhas)  
    |   |   |__ api.py (13 linhas)  
    |   |   |__ configuration.py (12 linhas)  
    |   |   |__ database.py (10 linhas)  
    |   |   |__ jwt.py (15 linhas)  
    |   |   |__ serializer.py (7 linhas)  
    |   |__ [models]  
    |   |   |__ __init__.py (0 linhas)  
    |   |   |__ hotel.py (39 linhas)  
    |   |   |__ usuario.py (55 linhas)  
    |   |__ [resources]  
    |   |   |__ __init__.py (0 linhas)  
    |   |   |__ hotel.py (97 linhas)  
    |   |   |__ usuario.py (83 linhas)  
    |   |__ [schema]  
    |   |   |__ __init__.py (0 linhas)  
    |   |   |__ serializer.py (25 linhas)  
    |   |__ __init__.py (0 linhas)  
    |   |__ app.py (9 linhas)  
    |   |__ banco.db (24 linhas)  
    |   |__ blacklist.py (1 linhas)  
    |   |__ config.py (0 linhas)  
    |   |__ filter.py (69 linhas)  
    |__ .pyproject.toml (16 linhas)  
    |__ .gitignore (1 linhas)  
    |__ requirements.txt (11 linhas)  
    |__ settings.toml (21 linhas)  
    rodrigoneal/hoteis_api


**Parâmetro**: `repository` **Tipo**:str- O repositório que foi *crawlado(sic)*que será usado para abrir o arquivo .txt
**Parâmetro**: `path_dict` **Tipo**:list- Recebe uma lista com dicionários, é usado pra criar a arvore de estrutura o dicionario precisa ter as chaves nome, url, ext, linhas e byte.

    {'nome': '__init__.py', 'url': 'blob/master/hotel/ext/__init__.py', 'ext': 'py', 'linhas': 0, 'byte': 0}
nome: o nome do arquivo que será salvo `'nome': '__init__.py'`
url: o caminho final da url do arquivo   `'url': 'blob/master/hotel/ext/__init__.py'`
ext: É a extensão do arquivo `__init__.py` a extensão é `'ext': 'py'` sem o ponto. 
linhas: a quantidade de linhas de código do arquivo passado.  `'linhas': 0`
byte: é o tamanho em bytes que o arquivo ocupa `'byte': 0`

- nome:str
 - url:str
 - ext:str
- linhas:int
 - byte:int

#### `save_as_column(repository, path_dict)` 
Função que cria o arquivo e grava um analise sobre as linguagens de programação mais utilizadas no projeto analisado, faz o calculo de porcentagem a linguagem representa do total do projeto no formato .txt.

      Extensão     |    Linhas     |    Bytes  
    py             |   435   (86 %)|  2422(74 %)   
    toml           |    37    (7 %)|  627(19 %)   
    db             |    24    (5 %)|  24(1 %)   
    txt            |    11    (2 %)|  203(6 %)   
    outros         |    1     (0 %)|  6(0 %)
**Parâmetro**: `repository` **Tipo**:str- O repositório que foi *crawlado(sic)*que será usado para abrir o arquivo .txt
**Parâmetro**: `path_dict` **Tipo**:dict- Recebe um dicionário com as linguagens de programação mais usadas.

    {'py': [435, 2422], 'db': [24, 24], 'toml': [37, 627], 'outros': [1, 6], 'txt': [11, 203]}


## Arquivo: `clear_code.py`


#### `normalize_file(url, data)` 
Função que recebe a url e a data para facilitar na hora de gravar no .txt,  retornando um dict com os dados normalizados   .
**Entrada**
url >>> `blob/master/hotel/ext/__init__.py`
data >>> `('py', (10, 185))`
**SAÍDA** 

  dict>>>  `{'nome': '__init.__.py' 'url': 'blob/master/hotel/ext/__init__.py, 'ext': 'py', 'linhas': 10, 'byte': 185}`

**Parâmetro**: `url` **Tipo**:str- Url relativo a pasta ou o arquivo que será filtrado. 

**Parâmetro**: `data` **Tipo**:dict- Recebe uma tupla com str e um tupla dentro e inserindo esses valores dentro de um dicionário.

    ('py', (7, 104))
O primeiro valor é a extensão do arquivo.
O segundo é uma tupla, no índice [0] ~~zero~~ é o numero de linhas escrita no arquivo e no índice [1] é o numero de bytes ocupado pelo arquivo. 
