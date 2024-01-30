# Esta função remove todas as vogais de uma string fornecida.
def remover_vogais(s):
    """
    Remove todas as vogais de uma string fornecida.

    Parâmetros:
    s (str): A string de entrada.

    Retorna:
    str: A string resultante após a remoção das vogais.
    """

def remover_vogais(s):
    return ''.join(c for c in s if c.lower() not in 'aeiou')

print(remover_vogais("Este site é para perdedores LOL!"))  # "st st é pr prdrsrs LL!"