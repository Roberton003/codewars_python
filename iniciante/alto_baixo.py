def alto_baixo(s):
    """
    Retorna o maior e o menor número em uma string de números separados por espaço.

    Args:
        s (str): A string contendo os números separados por espaço.

    Returns:
        str: Uma string contendo o maior e o menor número separados por espaço.
    """
    numeros = list(map(int, s.split()))
    return f"{max(numeros)} {min(numeros)}"

print(alto_baixo("1 2 3 4 5"))  # "5 1"
print(alto_baixo("1 2 -3 4 5"))  # "5 -3"
print(alto_baixo("1 9 3 4 -5"))  # "9 -5"