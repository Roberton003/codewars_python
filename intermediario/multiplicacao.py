def verificar_multiplicar(n):
    """
    Função que verifica se um número é par ou ímpar e retorna o resultado da multiplicação.

    Parâmetros:
    n (int): O número a ser verificado.

    Retorna:
    int: O resultado da multiplicação. Se o número for par, retorna n * 8. Se o número for ímpar, retorna n * 9.
    """
    # Verifica se o número é par
    if n % 2 == 0:
        # Retorna o resultado da multiplicação por 8
        return n * 8
    else:
        # Retorna o resultado da multiplicação por 9
        return n * 9

    return n * 8 if n % 2 == 0 else n * 9

print(verificar_multiplicar(4))  # 16
print(verificar_multiplicar(5))  # 27