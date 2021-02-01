# Desafio-Viva-Decora

<h2 style="text-align: center" xmlns="http://www.w3.org/1999/html">  Bem Vindo a documentação do Web Scraping. <h2/>
<p style="margin: 0; padding: 0">Para instalar basta clonar ou baixar o repositorio </p>
<br /> <em>  https://github.com/rodrigoneal/Desafio-Viva-Decora </em><br/>
Crie um arquivo com o nome <b>repositorios.txt</b> e coloque os repositorios um embaixo do outro 
<br/>  
<div style="align-content: center"> Ex: <ul style="list-style-type: none;"> <li>frontpressorg/frontpress</li> <br/>
           <li>SambitAcharya/Mini-Projects</li></ul>
<p> Obs: Sem espaço ou acentos e só coloque barra entre o nome do usuario do autor e o nome do projeto</p>

</div>

<h2 style="text-align: center"> API </h2>

<div>
<h2>
Web Scraping.py
</h2>

<h3>  <p>Classe GitHub: </p></h3>

<h4>  <code>def __init__(file_txt): </code> <br /></h4>
<p>Metodo que inicializa a classe GitHub</p>
<p>Parametro: <em>file.txt</em> TIPO:FileIO- Arquivo txt com a lista de repositorios que serão varridos</p>

<p>Variaveis: <code>self.url = "https://github.com/"</code><b>TIPO:</b>str - Variveis de instancia da classe GitHub que armazena a url base do github.</p>

<p>Variaveis: <code>self.repositorio = ""</code><b>TIPO:</b>str - Variveis de instancia da classe GitHub que armazena a url do 
repositorio do GitHub que é concatenado com a <code>self.base_url</code>.
Exemplo: https://github.com/<b><em>frontpressorg/frontpress</em></b>
</p>
<p>Variaveis: <code>self.file_txt = file_txt</code> <b>TIPO:</b>FileIO - Variveis de instancia da classe GitHub que armazena o nome do arquivo txt
que será usado pelo programa.
</p>

<p>Variaveis: <code>self.dados = []</code> <b>TIPO:</b>list - Variveis de instancia da classe GitHub que armazena uma lista com os dados dos <em>arquivos</em>
 já formatado. <br>
 <br>A formataçã é feita pela função get_data_file</p>
 <br>Obs: Arquivo é o arquivo pego dentro do GitHub exemplo: hoteis_api/hotel/app.py O app.py é um arquivo </p>

<p>Variaveis: <code>self.filter = ["gitignore", "Dockerfile", "Makefile"]</code> - Variveis de instancia da classe GitHub que armazena uma lista com as extensões que não serão
listado e listado como outro
</p>
<p>Variaveis: <code>self.diretorio</code> - Variveis de instancia da classe GitHub que armazena uma lista dicionario dentro com dados que serão gravados no arquivo txt</p>


<h3>  <p><code>request(path="")</code></p></h3>
<p>Metodo que faz uma requisição GET no site do github e retorna um objeto do tipo BeautifulSoup </p>
<p>Parametro: <em>path</em> TIPO:str - string com a url da pasta/arquivo que forma o link absoluto da pagina <br>
Exemplo: https://github.com/rodrigoneal/hoteis_api<b>/blob/master/hotel/app.py</b>
</p>

<h3>  <p><code>request_all_links()</code></p></h3>
<p>Metodo que navega por todas as pastas e arquivos de forma recursiva <br />

<h3>  <p><code>main()</code></p></h3>
<p>Metodo principal que inicia o programa <br />


</p>
</div>

<div>
<h2>parse_data</h2>


<h3> <code>sum_value_dict(list_to_parser, filter) </code> <br /></h3>
<p>Função que pega uma lista com dicionario e soma os valores de dentro dessa lista filtrando suas extensões <br>
Exemplo: Entrada: <code>[['py', (5, 5)], ['py', (5, 5)]]</code> Saida: <code>[{'py':(10, 10)}]</code>
</p>
<p>Parametro: <em>list_to_parser</em> TIPO:List- L</p>




</div>