def remover_priultimo(s):
    """
    Remove o primeiro e o último caractere de uma string e retorna o resultado.

    Args:
        s (str): A string de entrada.

    Returns:
        str: A string resultante após a remoção do primeiro e último caractere.
    """
    return s[1:-1]

print(remover_priultimo("Python"))  # "ytho"
print(remover_priultimo("JavaScript"))  # "avaScrip"