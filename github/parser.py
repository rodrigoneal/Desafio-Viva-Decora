from operator import itemgetter


def sum_value_dict(list_to_parser:list[dict], filter:list[str]) -> list[dict[str,tuple[int,int]]]:
    """
    Soma os valores  e salva num dicionario
    :param list_to_parser: list
    :param filter:list
    :return list
    """
    temp_dict = {}
    for key, value in list_to_parser:
        if key in filter:
            key = 'outros'
        if key in temp_dict:
            temp_dict[key] = [x + y for x, y in zip(temp_dict[key], value)]
        else:
            temp_dict[key] = value
    return temp_dict


def get_data_file(soup:object) -> tuple[str, tuple[int, int]]:
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
    return result

# dados = [('py', (0, 0)), ('py', (13, 481)), ('py', (12, 259)), ('py', (10, 185)), ('py', (15, 417)), ('py', (7, 104)), ('py', (0, 0)), ('py', (39, 1)), ('py', (55, 1)), ('py', (0, 0)), ('py', (97, 3)), ('py', (83, 2)), ('py', (0, 0)), ('py', (25, 758)), ('py', (0, 0)), ('py', (9, 192)), ('db', (24, 24)), ('py', (1, 18)), ('py', (0, 0)), ('py', (69, 1)), ('toml', (16, 173)), ('gitignore', (1, 6)), ('txt', (11, 203)), ('toml', (21, 454))]
# a = sum_value_dict(dados, 'filter')
# print(a)