# Desafio-Viva-Decora

### Bem Vindo a documentação do Web Scraping.

## Como Instalar:

    pip install git+https://github.com/rodrigoneal/Desafio-Viva-Decora.git#egg=web-scraping

## Como Usar:

    from github.web_scraping import GitHub

    git = GitHub("repositorios.txt")
    git.main(verbose=True)

Importe a classe GitHub que fica dentro do pacote github.web*scraping. A classe recebe
um parâmetro obrigatório que é o arquivo txt com a lista de repositórios do github que
serão \_crawlada*.

O método `main(verbose=False)` recebe um parâmetro booleano posicional opcional
_verbose_ por default=False. Coloque `True` para que o programa imprima no terminal as
URLs das pastas e arquivos que estão sendo _crawlado_.

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

Se for `False` ele apenas irá imprimir o repositório que está sendo _crawlado_ na hora.

    rodrigoneal/hoteis_api

#### Formatação do arquivo txt

Obrigatoriamente o arquivo precisa terminar com .txt e formatado da seguinte maneira:

    rodrigoneal/hoteis_api
    SambitAcharya/Mini-Projects
    frontpressorg/frontpress

Só utilize "/" entre o nome do usuário e o nome do repositório, evite colocar espaços
desnecessários.

# API

Arquivo: _web-scraping.py_

#### Classe GitHub:

#### `def __init__(file_txt):`

Método que inicializa a classe GitHub **Parametro**: file.txt; **Tipo**:FileIO- Arquivo
txt com a lista de repositórios que serão varridos

**Variável**: `self.url = "https://github.com/"`; **Tipo**:str - Variável de instância
da classe GitHub que armazena a url base do github.

**Variável**: `self.repositorio = ""`; **Tipo**: str - Variável de instância da classe
GitHub que armazena a url do  
repositorio do GitHub que é concatenado com a self.base_url Exemplo:
`https://github.com/frontpressorg/frontpress`

**Variável**: `self.file_txt = file_txt`; **Tipo**:FileIO - Variável de instância da
classe GitHub que armazena o nome do arquivo .txt que é usado pela classe GitHub.

**Variável**: `self.dados = []`; **Tipo**:list - Variável de instância da classe GitHub
que armazena uma lista com os dados dos arquivos já formatado.

Obs:

_Arquivo é o arquivo pego dentro do GitHub exemplo: "hoteis_api/hotel/app.py". O app.py
é um arquivo_

**Variável**: `self.filter = ["gitignore", "Dockerfile", "Makefile"]`; **Tipo**:list-
Variável de instância da classe GitHub que armazena uma lista com as extensões que não
serão  
listado e listado como outro

**Variável**: `self.diretorio=[]`; **Tipo**:list - Variável de instância da classe
GitHub que armazena uma lista de dicionários com os dados que serão gravados no arquivo
.txt

#### `request(path="")`

Método que faz uma requisição GET no site do github e retorna um objeto do tipo
_BeautifulSoup_ **Parâmetro**: path="" **Tipo**:str- string com a url da pasta ou
arquivo que forma o link absoluto da pagina

Exemplo: Link relativo ao arquivo app.py : `blob/master/hotel/app.py` Link absoluto do
arquivo app.py: `https://github.com/rodrigoneal/hoteis_api/blob/master/hotel/app.py`

#### `request_all_links()`

Método que navega por todas as pastas e arquivos de forma recursiva. Ele é o core da
aplicação pois pega todos os links e dentro dentro há chamadas de outras funções e
métodos que dão vida ao programa.

#### `main()`

Método inicia o programa **Parâmetro**: `verbose=True` **Tipo**:boolean-
**Default**=False Esse parâmetro indica se o programa deverá imprimir todos as URLs que
o programa está percorrendo em tempo real.

Arquivo parse_data.py

#### `sum_value_dict(list_to_parser, filter)`

Função que pega uma lista com dicionário e tupla. Soma os valores de dentro dessa lista
filtrando suas extensões Exemplo: Entrada >>> `[['py', (5, 5)], ['py', (5, 5)]]`
Saída >>>`[{'py':(10, 10)}]`

**Parâmetro**: `list_to_parser` **Tipo**:list- Lista com os arquivos que serão somados e
filtrados.

**Parâmetro**: `filter` **Tipo**:list- Lista com os arquivos que deverão ser ignorados e
armazenados como outros .

#### `get_data_file(soup)`

Função que pega os arquivos da URL e extrai o a extensão, numero de linhas e quantidade
de bytes do arquivo

    extensão:save.py, numero de linhas: 59, bytes: 2.24

Obs: Quando eu falo arquivo é a URL que contem o programa em si, exemplo .py, .js .php.
Obs: Ele salva converte esses dados de numero de linhas e quantidade de bytes para `int`
