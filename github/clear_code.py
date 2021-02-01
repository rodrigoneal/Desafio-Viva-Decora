# mypy: ignore-errors
"""
Esse script é usado para refinar os dados do aplicativo.

Author: Rodrigo Castro
Date: 1/02/2021
"""
from typing import Tuple, Dict, Union


def normalize_file(
    url: str, data: Tuple[str, int, int] = None
) -> Dict[Union[str, int]]:
    """
    Trata os dados para facilitar na hora de salvar o arquivo.

    :param data:
    :param url:str
    :param dados: tuple
    :return: dict
    """
    if data:
        nome = url.split("/")[-1]
        path = url
        ext = data[0]
        linhas = data[1][0]
        byte = data[1][1]
    else:
        nome = url.split("/")[-1]
        path = url
        ext = ""
        linhas = ""
        byte = ""
    return {"nome": nome, "url": path, "ext": ext, "linhas": linhas, "byte": byte}
