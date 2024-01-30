def soma_numeros(lista):
    """
    Função que recebe uma lista de números e retorna a soma de todos os elementos.

    Parâmetros:
    - lista: uma lista de números inteiros ou de ponto flutuante.

    Retorno:
    - A soma de todos os elementos da lista.
    """
    return sum(lista)

print(soma_numeros([1, 5.2, 4, 0, -1]))  # 9.2
print(soma_numeros([]))  # 0
print(soma_numeros([-2.398]))  # -2.398