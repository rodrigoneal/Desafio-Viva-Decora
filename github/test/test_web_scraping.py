"""Testa o programa."""
import unittest
from github.clear_code import normalize_file
from github.parse_data import sum_value_dict, get_data_file  # type: ignore
from github.web_scraping import GitHub


class TestGitHub(unittest.TestCase):

    """Classe que herda o TestCase."""

    def setUp(self):
        """Metodo que prepara um fixture."""
        self.git = GitHub("repositorios.txt")

    def test_se_normalize_retorna_um_dict(self):
        """Testa se a função normalize_file retorna um dict."""
        url = "tree/master/hotel"
        data = ("py", (7, 104))
        self.assertIsInstance(
            normalize_file(url, data), dict
        )

    def test_se_sum_value_dict_retorna_os_valores_somados(
        self,
    ):
        """Testa se a função sum_value_dict retorna os valores somados."""
        list_to_parser = ("py", (5, 10)), (
            "py",
            (5, 10),
        )
        filter = ["foo","bar"]
        self.assertEqual(
            sum_value_dict(
                list_to_parser, filter
            ),
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
            sum_value_dict(
                list_to_parser, filter
            ),
            {"outros": [10, 20]},
        )

    def test_se_get_data_file_retorna_um_tupla(
        self,
    ):
        """Testa se o get_data_file está retornando uma tupla."""
        self.git.repositorio = (
            "rodrigoneal/Desafio-Viva-Decora"
        )
        soup = self.git.request(
            "blob/master/github/__init__.py"
        )
        self.assertIsInstance(
            get_data_file(soup), tuple
        )

    def test_se_get_data_file_retorna_os_valores_da_pagina(
        self,
    ):
        """Teste se o get_data_file está pegando os valores certos da pagina."""
        self.git.repositorio = (
            "rodrigoneal/Desafio-Viva-Decora"
        )
        soup = self.git.request(
            "blob/master/github/__init__.py"
        )
        self.assertEqual(
            get_data_file(soup), ("py", (5, 116))
        )


if __name__ == "__main__":
    unittest.main()
