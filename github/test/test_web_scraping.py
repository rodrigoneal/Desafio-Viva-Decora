"""Testa o programa."""
import os
import unittest
from github.clear_code import normalize_file
from github.parse_data import sum_value_dict, get_data_file  # type: ignore
from github.save import (
    save_tree_structure,
    save_as_column,
    calculate_percentage,
)
from github.web_scraping import GitHub


class TestGitHub(unittest.TestCase):
    """Classe que herda o TestCase."""

    def setUp(self):
        """Metodo que prepara um fixture."""
        self.git = GitHub("repositorios.txt")

    def tearDown(self):
        """Exclui tudo no final dos testes."""
        arquivo = "Project rodrigoneal_hoteis_api.txt"
        if os.path.exists(arquivo):
            os.remove(arquivo)

    def test_se_normalize_retorna_um_dict(self):
        """Testa se a função normalize_file retorna um dict."""
        url = "tree/master/hotel"
        data = ("py", (7, 104))
        self.assertIsInstance(normalize_file(url, data), dict)

    def test_se_normalize_retorna_so_url_sem_passar_os_dados(
        self,
    ):
        """Teste se a função normalize consegue filtrar sem passar o parametro dados."""
        url = "tree/master/hotel"
        self.assertEqual(
            normalize_file(url),
            {
                "byte": "",
                "ext": "",
                "linhas": "",
                "nome": "hotel",
                "url": url,
            },
        )

    def test_se_sum_value_dict_retorna_os_valores_somados(
        self,
    ):
        """Testa se a função sum_value_dict retorna os valores somados."""
        list_to_parser = ("py", (5, 10)), (
            "py",
            (5, 10),
        )
        filter = ["foo", "bar"]
        self.assertEqual(
            sum_value_dict(list_to_parser, filter),
            {"py": [10, 20]},
        )

    def test_se_sum_value_dict_retorna_os_valores_do_filter_em_outros(
        self,
    ):
        """Testa se a função sum_value_dict faz um filtro do valor passado no filtro e retorna uma extensão outros."""
        list_to_parser = ("py", (5, 10)), (
            "py",
            (5, 10),
        )
        filter = ["py"]
        self.assertEqual(
            sum_value_dict(list_to_parser, filter),
            {"outros": [10, 20]},
        )

    def test_se_get_data_file_retorna_um_tupla(
        self,
    ):
        """Testa se o get_data_file está retornando uma tupla."""
        self.git.repositorio = "rodrigoneal/Desafio-Viva-Decora"
        soup = self.git.request("blob/master/github/__init__.py")
        self.assertIsInstance(get_data_file(soup), tuple)

    def test_se_get_data_file_retorna_os_valores_da_pagina(
        self,
    ):
        """Teste se o get_data_file está pegando os valores certos da pagina."""
        self.git.repositorio = "rodrigoneal/hoteis_api"
        soup = self.git.request("blob/master/hotel/app.py")
        self.assertEqual(get_data_file(soup), ("py", (9, 192)))

    def test_se_save_tree_structure_cria_arquivo(
        self,
    ):
        """Testar se o função está gravando no arquivo."""
        repositorio = self.git.repositorio = "rodrigoneal/hoteis_api"
        path_data = [
            {
                "nome": "hotel",
                "url": "tree/master/hotel",
                "ext": "",
                "linhas": "",
                "byte": "",
            }
        ]
        save_tree_structure(repositorio, path_data)
        self.assertTrue(os.path.exists("Project rodrigoneal_hoteis_api.txt"))

    def test_se_calculate_percentage_calcula_certo(self):
        """Teste se a função está calculando certo."""
        total = 3283
        value = 2423

        self.assertEqual(round(calculate_percentage(total, value)), 74)

    def test_se_save_column_cria_um_arquivo(self):
        """Testa se a função save_column cria um arquivo."""
        path_dict = {
            "py": [435, 2423.86],
            "db": (0, 24.0),
            "toml": [37, 627.0],
            "outros": (1, 6.0),
            "txt": (11, 203.0),
        }
        repositorio = self.git.repositorio = "rodrigoneal/hoteis_api"
        save_as_column(repositorio, path_dict)
        self.assertTrue(os.path.exists("Project rodrigoneal_hoteis_api.txt"))


if __name__ == "__main__":
    unittest.main()
