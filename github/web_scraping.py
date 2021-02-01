import httpx
from bs4 import BeautifulSoup

from github.save import save_as_column, save_tree_structure
from github.parser import sum_value_dict, get_data_file
from github.clear_code import normalize_file

class GitHub:
    def __init__(self, file_txt):
        self.base_url = "https://github.com/"
        self.repositorio = ''
        self.links = []  # Salva todas as urls da
        self.file_txt = file_txt
        self.path = ''
        self.dados = []
        self.filter = ['gitignore', 'Dockerfile', 'Makefile']
        self.diretorio = []

    def request(self, path: str = ''):
        """
        Faz uma requisição GET pegando todo o conteudo html
        e faz um parser do html para manipulação
        do objeto atraves do BeautifulSoup
        :param path: str
        """
        url = f"{self.base_url}{self.repositorio}/{path}"
        get = httpx.get(url)
        print(get.url)
        soup = BeautifulSoup(get.text, "html.parser")
        return soup

    def request_all_links(self, path=''):

        """
        Navega por toda a pagina de forma recursiva pegando todos os urls
        verificando se é uma pasta ou um arquivo
        :-Se for um arquivo chama o metodo "get_data_file"
        que faz um crawler salvando as informações do arquivo
        :-Se for uma pasta salva dentro da lista com todos os links das pastas
        """
        soup = self.request(self.path)
        if self.path.startswith('blob'):
            result = get_data_file(soup)
            self.dados.append(result)
            normalize = normalize_file(self.path, result)
            self.diretorio.append(normalize)
        else:
            if self.path != '':
                normalize = normalize_file(self.path)
                self.diretorio.append(normalize)
        spans = soup.find_all("span", {"class": "css-truncate"})
        for span in spans:
            links = span.find_all("a", {"class": "js-navigation-open"})
            for link in links:
                _split = link["href"].split('/')[3:]
                self.path = '/'.join(_split)
                self.request_all_links()

    def main(self):
        """
        Metodo que inicializa a programa pegando o arquivo txt
        primeiro faz a leitura do arquivo txt passando ele para a variavel da instancia
        chama o metodo get_links que percorre o site pegando todos os arquivos e pastas
        itera sobre todos os links chamando a função normalize_files passando o link e os dados do link
        salva na variavel da instancia da classe o metodo normalize
        salva todos os dados no txt com o nome do repositorio
        limpa todas as variaveis da instancia da classe para começa com um novo repositorio
        """
        with open(self.file_txt, 'r') as files:
            for file in files.readlines():
                self.repositorio = file.strip()
                self.request_all_links()
                sum_dict = sum_value_dict(self.dados, self.filter)
                save_as_column(self.repositorio, sum_dict)
                save_tree_structure(self.repositorio, self.diretorio)
                self.diretorio.clear()
                self.links.clear()
                self.dados.clear()
                self.path = ''


if __name__ == "__main__":
    from time import time

    git = GitHub('teste.txt')
    inicio = time()
    a = git.main()

    fim = time()
    print(fim - inicio)
