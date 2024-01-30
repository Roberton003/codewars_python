def soma_array(array):
    """
    Soma todos os elementos de um array.

    Args:
        array (list): Uma lista de números.

    Returns:
        int: A soma de todos os elementos do array.
    """
    return sum(int(i) for i in array)

# Comentário explicando a função
# A função soma_array recebe um array de números e retorna a soma de todos os elementos do array.

print(soma_array(["1", 2, "3", 4, "5"]))  # 15