"""
Esse script é usado para criar e gravar os dados do web scraping.

Author: Rodrigo Castro
Date: 1/02/2021
"""


def save_tree_structure(
    repository: str, path_dict: dict
) -> None:
    """Grava dentro do txt com o nome do repositorio uma lista em arvore com subdiretorios e seus arquivos."""
    with open(
        f'Project {repository.replace("/", "_")}.txt',
        "a",
    ) as file:
        file.write("\n\n\n\n")
        for diretorio in path_dict:
            tamanho = diretorio["url"].split("/")

            if tamanho[0] == "tree":

                file.write(
                    f'{"|   " * (len(tamanho) - 3)}|__ [{diretorio["nome"].strip()}]'
                    + "\n"
                )
            else:

                file.write(
                    f'{"|   " * (len(tamanho) - 3)}|__ {diretorio["nome"].strip()} ({diretorio["linhas"]} linhas)'
                    + "\n"
                )


def save_as_column(
    repository: str, path_dict: dict
) -> None:
    """Cria um arquivo txt se não existir, com nome do repositorio e grava as extensões."""
    print(path_dict)
    with open(
        f'Project {repository.replace("/", "_")}.txt',
        "a",
    ) as file:
        file.write(repository + "\n\n\n\n")
        file.write(
            f" {'Extensão':<13}|{'Linhas':^15}|{'Bytes':>14}"
            + "\n"
        )
        sum_lines = 0
        sum_bytes = 0
        lista_ordenada = [
            item for item in path_dict.items()
        ]
        lista_ordenada.sort(
            key=lambda x: x[1][0], reverse=True
        )
        for _, v in lista_ordenada:
            sum_lines += v[0]
            sum_bytes += v[1]
        for k, v in lista_ordenada:
            tipo = k
            linha = v[0]
            byte = v[1]
            if linha > 0 and byte > 0:
                file.write(
                    f"{tipo:<15}|{linha:^10}({round(linha / sum_lines * 100)} %)|{byte}({round(byte / sum_bytes * 100)} %) "
                    + "\n"
                )
            elif linha > 0 and byte == 0:
                file.write(
                    f"{tipo:<15}|{linha:^10}({round(linha / sum_lines * 100)} %)|{byte}(0 %) "
                    + "\n"
                )
            elif linha == 0 and byte > 0:
                file.write(
                    f"{tipo:<15}|{linha:^10} (0 %)|{byte}(0 %) "
                    + "\n"
                )
            else:
                file.write(
                    f"{tipo:<10}|{linha:^15}(0 %)|{byte:>10}(0 %)"
                    + "\n"
                )
