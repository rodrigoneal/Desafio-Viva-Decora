# type: ignore
"""Esse script é usado para fazer o parser dos arquivos do projeto."""
from typing import List, Dict, Tuple, Any


def sum_value_dict(
    list_to_parser: Tuple[Tuple[str, Tuple[int]]],
    filter_value: List[str],
) -> Dict[str, List[Any]]:
    """
    Soma os valores  e salva num dicionario.

    :param list_to_parser: list
    :param filter_value:list
    :return list
    """
    temp_dict: Dict[str, Tuple] = {}
    for key, value in list_to_parser:
        if key in filter_value:
            key = "outros"
        if key not in temp_dict:
            temp_dict[key] = value
        else:
            temp_dict[key] = [x + y for x, y in zip(temp_dict[key], value)]
    return temp_dict


def get_data_file(
    soup: Any,
) -> Tuple[str, Tuple[int, int]]:
    """
    Extrai as informações da pagina com a extensão, a quantidade de linhas e a quantidade de byte do arquivo.

    :param soup: object BeautifulSoup
    """
    div = soup.find("div", {"class": "text-mono"}).text.strip()
    extensao = soup.find("strong", {"class": "final-path"}).text.split(".")[-1]
    lines = div.split(" ")
    if lines[0] != "executable" and "lines" in lines:
        linha_byte = (int(float(lines[0])), float(lines[-2]))
    elif lines[0] == "executable" and "lines" in lines:
        linha_byte = (int(float(lines[7])), float(lines[-2]))
    else:
        linha_byte = (0, float(lines[-2]))
    extensao = extensao.replace("~", "")
    result = extensao, linha_byte
    return result
