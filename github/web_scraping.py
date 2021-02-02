"""
Esse arquivo é o principal que faz todo o programa funcionar.

Author: Rodrigo Castro
Date: 1/02/2021
"""

import httpx
from bs4 import BeautifulSoup

from github.save import (
    save_as_column,
    save_tree_structure,
)
from github.parse_data import (  # type: ignore
    sum_value_dict,
    get_data_file,
)
from github.clear_code import normalize_file


class GitHub:
    """Classe que faz a requisição, pega os links e salva."""

    def __init__(self, file_txt):
        """Inicializador da classe."""
        self.base_url = "https://github.com/"
        self.repositorio = ""
        self.file_txt = file_txt
        self.path = ""
        self.dados = []
        self.filter = [
            "gitignore",
            "Dockerfile",
            "Makefile",
        ]
        self.diretorio = []
        self.verbose = False

    def request(self, path: str = ""):
        """
        Faz uma requisição GET pegando todo o conteudo html.

        :param path: str
        """
        url = f"{self.base_url}{self.repositorio}/{path}"
        get = httpx.get(url)
        if self.verbose:
            print(get.url)
        soup = BeautifulSoup(
            get.text, "html.parser"
        )
        return soup

    def request_all_links(self):
        """Navega por toda a pagina de forma recursiva pegando todos os urls."""
        soup = self.request(self.path)
        if self.path.startswith("blob"):
            result = get_data_file(soup)
            self.dados.append(result)
            normalize = normalize_file(
                self.path, result
            )
            self.diretorio.append(normalize)
        else:
            if self.path != "":
                normalize = normalize_file(
                    self.path
                )
                self.diretorio.append(normalize)
        spans = soup.find_all(
            "span", {"class": "css-truncate"}
        )
        for span in spans:
            links = span.find_all(
                "a",
                {"class": "js-navigation-open"},
            )
            for link in links:
                _split = link["href"].split("/")[
                    3:
                ]
                self.path = "/".join(_split)
                self.request_all_links()

    def main(self, verbose=False):
        """Metodo que inicializa a programa."""
        with open(self.file_txt, "r") as files:
            for file in files.readlines():
                self.verbose = verbose
                self.repositorio = file.strip()
                self.request_all_links()
                sum_dict = sum_value_dict(
                    self.dados, self.filter
                )
                save_as_column(
                    self.repositorio, sum_dict
                )
                save_tree_structure(
                    self.repositorio,
                    self.diretorio,
                )
                self.diretorio.clear()
                self.dados.clear()
                self.path = ""


if __name__ == "__main__":
    git = GitHub("repositorios.txt")
    git.main(True)
