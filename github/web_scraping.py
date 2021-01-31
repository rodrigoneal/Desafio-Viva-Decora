import os
from collections import OrderedDict
import httpx
from bs4 import BeautifulSoup

# TODO: Consertar o problema do self.dados que tem indices a menos


def normalize_file(url: str, dados: tuple = None) -> dict:
    """
    Trata os dados para facilitar na hora de salvar o arquivo
    :param url:str
    :param dados: tuple
    :return: um dicionario com o nome, a url, a extensão, as linhas e o tamanho do arquivo
    tratado
    """
    if dados:
        nome = url.split('/')[-1]
        path = url
        ext = dados[0]
        linhas = dados[1][0]
        byte = dados[1][1]
    else:
        nome = url.split('/')[-1]
        path = url
        ext = ''
        linhas = ''
        byte = ''
    return {'nome': nome, "url": path, 'ext': ext, 'linhas': linhas, 'byte': byte}


class GitHub:
    def __init__(self, file_txt):
        self.base_url = "https://github.com/"
        self.repositorio = ''
        self.links = []  # Salva todas as urls da
        self.file_txt = file_txt
        self.total_percentage = OrderedDict()
        self.path = ''
        self.dados = []
        self.outros = ['gitignore', 'Dockerfile', 'Makefile']
        self.diretorio = []
        self.cont = 0

    def add_dict(self, key: str, value: tuple):

        """
        Soma os valores do dicionario com a chave especifica
        :param key: str
        :param value: tuple
        """

        if key in self.outros:
            key = 'outros'
        if key in self.total_percentage:
            self.total_percentage[key] = [x + y for x, y in zip(self.total_percentage[key], value)]
        else:
            self.total_percentage[key] = value

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

    def get_links(self):

        """
        Navega por toda a pagina de forma recursiva pegando todos os urls
        verificando se é uma pasta ou um arquivo
        :-Se for um arquivo chama o metodo "get_data_file"
        que faz um crawler salvando as informações do arquivo
        :-Se for uma pasta salva dentro da lista com todos os links das pastas
        """
        soup = self.request(self.path)
        if self.path.startswith('blob'):
            self.get_data_file(soup)
        spans = soup.find_all("span", {"class": "css-truncate"})
        for span in spans:
            links = span.find_all("a", {"class": "js-navigation-open"})
            for link in links:
                _split = link["href"].split('/')[3:]
                self.path = '/'.join(_split)
                self.links.append(self.path)
                self.get_links()

    def save_type(self):
        """
        Cria um arquivo txt se não existir, com nome do repositorio e grava as extensões
        das linguagens de programação utilizada no projeto com as informações da quantidade
        de linhas e a porcentagem de linhas utilizada para cada linguagem
        """
        with open(f'Project {self.repositorio.replace("/", "_")}.txt', 'a') as file:
            if not os.path.getsize(f'Project {self.repositorio.replace("/", "_")}.txt') > 0:
                file.write(self.repositorio + '\n\n\n\n')
                file.write(f" {'Extensão':<13}|{'Linhas':^15}|{'Bytes':>14}" + '\n')
            sum_lines = 0
            sum_bytes = 0
            lista_ordenada = sorted(self.total_percentage.items(), key=lambda v: v[1][0])[:]
            lista_ordenada.sort(key=lambda x: x[1][0], reverse=True)
            for _, v in lista_ordenada:
                sum_lines += v[0]
                sum_bytes += v[1]
            for k, v in lista_ordenada:
                tipo = k
                linha = v[0]
                byte = v[1]
                if linha > 0 and byte > 0:
                    file.write(
                        f'{tipo:<15}|{linha:^10}({round(linha / sum_lines * 100)} %)|{byte}({round(byte / sum_bytes * 100)} %) ' + '\n')
                elif linha > 0 and byte == 0:
                    file.write(
                        f'{tipo:<15}|{linha:^10}({round(linha / sum_lines * 100)} %)|{byte}(0 %) ' + '\n')
                elif linha == 0 and byte > 0:
                    file.write(
                        f'{tipo:<15}|{linha:^10} (0 %)|{byte}(0 %) ' + '\n')
                else:
                    file.write(f'{tipo:<10}|{linha:^15}(0 %)|{byte:>10}(0 %)' + '\n')

    def save_structure_txt(self):
        """
        Grava dentro do txt com o nome do repositorio uma lista em arvore com subdiretorios e seus arquivos.
        Os arquivos tem a informação da quantidade de linhas e o tamanho que ocupa em bytes
        """

        with open(f'Project {self.repositorio.replace("/", "_")}.txt', 'a') as file:
            if not os.path.getsize(f'Project {self.repositorio.replace("/", "_")}.txt') > 0:
                file.write('\n')
            for diretorio in self.diretorio:
                tamanho = diretorio['url'].split('/')

                if tamanho[0] == 'tree':

                    file.write(f'{"|   " * (len(tamanho) - 3)}|__ [{diretorio["nome"].strip()}]' + '\n')
                else:

                    file.write(
                        f'{"|   " * (len(tamanho) - 3)}|__ {diretorio["nome"].strip()} ({diretorio["linhas"]} linhas)' + '\n')

    def get_data_file(self, soup):
        """
        Extrai as informações da pagina com a extensão, a quantidade de linhas e a quantidade de byte do arquivo
        passa essas informações pra serem salvas dentro de um dicionario e salva dentro de uma lista
        :param soup: object BeautifulSoup
        """
        div = soup.find("div", {"class": "text-mono"}).text.strip()
        extensao = soup.find("strong", {"class": "final-path"}).text.split(".")[-1]
        lines = div.split(" ")
        try:
            linha_byte = int(float(lines[0])), int(float(lines[-2]))
        except ValueError:
            try:
                linha_byte = int(float(lines[7])), int(float(lines[-2]))
            except:
                linha_byte = 0, 0
        result = extensao, linha_byte
        self.dados.append(result)
        self.add_dict(*result)

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
                self.get_links()
                self.path = ''
                for link in range(len(self.links)):
                    if self.links[link].startswith('blob'):
                        normalize = normalize_file(self.links[link], self.dados[link])
                        self.diretorio.append(normalize)
                    else:
                        normalize = normalize_file(self.links[link])
                        self.diretorio.append(normalize)

                self.path = ''
                self.save_type()
                self.save_structure_txt()
                self.diretorio.clear()
                self.links.clear()
                self.total_percentage.clear()


if __name__ == "__main__":
    from time import time

    git = GitHub('teste.txt')
    inicio = time()
    a = git.main()

    fim = time()
    print(fim - inicio)


