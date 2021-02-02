"""Testa o programa."""
import unittest
from github.clear_code import normalize_file
from github.parse_data import sum_value_dict  # type: ignore


class TestGitHub(unittest.TestCase):
    """Classe que herda o TestCase."""

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
        filter = [".venv"]
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


if __name__ == "__main__":
    unittest.main()
