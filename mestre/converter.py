def string_para_array(s):
    """
    Converte uma string em uma lista de palavras.

    Args:
        s (str): A string a ser convertida.

    Returns:
        list: Uma lista contendo as palavras da string.
    """
    return s.split()

print(string_para_array("Robin Singh"))  # ["Robin", "Singh"]
print(string_para_array("I love arrays they are my favorite"))  # ["I", "love", "arrays", "they", "are", "my", "favorite"]