def normalize_file(url: str, data: tuple[str, int, int] = None) -> dict:
    """
    Trata os dados para facilitar na hora de salvar o arquivo
    :param data:
    :param url:str
    :param dados: tuple
    :return: dict
    """
    if data:
        nome = url.split('/')[-1]
        path = url
        ext = data[0]
        linhas = data[1][0]
        byte = data[1][1]
    else:
        nome = url.split('/')[-1]
        path = url
        ext = ''
        linhas = ''
        byte = ''
    return {'nome': nome, "url": path, 'ext': ext, 'linhas': linhas, 'byte': byte}

