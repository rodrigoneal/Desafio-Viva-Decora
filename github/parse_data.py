# mypy: ignore-errors
"""
Esse script é usado para fazer o parser dos arquivos do projeto.

Author: Rodrigo Castro
Date: 1/02/2021
"""
from typing import List, Dict, Tuple, Any


def sum_value_dict(
    list_to_parser: List[dict], filter: List[str]
) -> Dict[str, Tuple[Any]]:
    """
    Soma os valores  e salva num dicionario.

    :param list_to_parser: list
    :param filter:list
    :return list
    """
    temp_dict: Dict[str, Tuple] = {}
    for key, value in list_to_parser:
        if key in filter:
            key = "outros"
        if key in temp_dict:
            temp_dict[key] = [x + y for x, y in zip(temp_dict[key], value)]
        else:
            temp_dict[key] = value
    return temp_dict


def get_data_file(soup: object) -> Tuple[str, tuple[int, int]]:
    """
    Extrai as informações da pagina com a extensão, a quantidade de linhas e a quantidade de byte do arquivo.

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
    return result
