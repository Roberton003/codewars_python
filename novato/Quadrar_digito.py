def quadrar_digitos(n):
    """
    Função que recebe um número inteiro e retorna um novo número formado pelos dígitos do número original elevados ao quadrado.

    Parâmetros:
    n (int): O número inteiro a ser processado.

    Retorna:
    int: O novo número formado pelos dígitos do número original elevados ao quadrado.
    """
    return int(''.join(str(int(i)**2) for i in str(n)))

print(quadrar_digitos(9119))  # 811181
print(quadrar_digitos(765))  # 493625