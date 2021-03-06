"""Esse script é usado para refinar os dados do aplicativo."""
from typing import Dict, Union, Optional


def normalize_file(
    url: str,
    data: Optional[tuple] = None,
) -> Dict[str, Union[str, int]]:
    """Trata os dados para facilitar na hora de salvar o arquivo.

    :param data: tuple
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

    return {
        "nome": nome,
        "url": path,
        "ext": ext,
        "linhas": linhas,
        "byte": byte,
    }
