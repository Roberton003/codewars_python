import random

def juntar_palavras_em_frase(palavras):
    """
    Junta um conjunto de palavras em uma frase, adicionando espaços entre elas.

    Parâmetros:
    - palavras (list): Lista de palavras a serem unidas.

    Retorna:
    Uma string representando a frase formada pelas palavras.
    """
    return ' '.join(palavras)

def teste_juntar_palavras_em_frase():
    """
    Testa a função juntar_palavras_em_frase com 5 casos de teste aleatórios.

    Imprime 'Pass' se o teste passar e 'Fail' se falhar.
    """
    for _ in range(5):
        lista_palavras = [random.choice(['word', 'python', 'hello', 'test']) for _ in range(random.randint(2, 6))]
        expected_output = ' '.join(lista_palavras)
        result = juntar_palavras_em_frase(lista_palavras)
        
        try:
            assert result == expected_output
            print(f"Pass: juntar_palavras_em_frase({lista_palavras}) == '{expected_output}'")
        except AssertionError:
            print(f"Fail: juntar_palavras_em_frase({lista_palavras}) != '{expected_output}'")

# Executando os testes aleatórios
teste_juntar_palavras_em_frase()
'''A função juntar_palavras_em_frase usa o método join para unir as palavras da lista em uma única string, separadas por espaços. A função de teste aleatório gera 5 conjuntos de palavras aleatórias
 e compara o resultado da função principal com o resultado esperado.'''