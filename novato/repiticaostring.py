import random

def repeat_string(s, n):
    """
    Repete a string s exatamente n vezes.

    Parâmetros:
    - s (str): A string a ser repetida.
    - n (int): O número de repetições.

    Retorna:
    Uma string resultante da repetição de s n vezes.
    """
    return s * n

def random_test_repeat_string():
    """
    Testa a função repeat_string com 5 casos de teste aleatórios.

    Imprime 'Pass' se o teste passar e 'Fail' se falhar.
    """
    for _ in range(5):
        s = ''.join(random.choice(['a', 'b', 'c']) for _ in range(random.randint(1, 10)))
        n = random.randint(1, 5)
        expected_output = s * n
        result = repeat_string(s, n)
        
        try:
            assert result == expected_output
            print(f"Pass: repeat_string('{s}', {n}) == '{expected_output}'")
        except AssertionError:
            print(f"Fail: repeat_string('{s}', {n}) != '{expected_output}'")

# Executando os testes aleatórios
random_test_repeat_string()

'''Claro, vou explicar cada parte do código:

1. **`repeat_string(s, n)` Function:**
   - Esta função aceita dois parâmetros: uma string `s` e um número inteiro `n`.
   - Utiliza o operador de multiplicação (`*`) para repetir a string `s` exatamente `n` vezes.
   - Retorna a string resultante da repetição.

2. **`test_repeat_string()` Function:**
   - Esta função de teste verifica se a função `repeat_string` está funcionando corretamente.
   - Define uma lista de casos de teste (`test_cases`), onde cada caso é uma tupla contendo uma string `s`, um número `n`, e o resultado esperado após a repetição.
   - Utiliza um loop `for` para iterar sobre os casos de teste.
   - Chama a função `repeat_string` com os parâmetros dados no caso de teste.
   - Usa uma estrutura `try` e `except` para verificar se o resultado obtido é igual ao resultado esperado. Se sim, imprime "Pass"; caso contrário, imprime "Fail".

3. **Execução dos Testes (`test_repeat_string()`):**
   - No final do código, a função de teste é chamada (`test_repeat_string()`).
   - Os testes incluem casos com strings diferentes, números de repetição variados, uma string vazia e um caso com `n` igual a 1.
   - Cada teste é impresso como "Pass" se for bem-sucedido ou "Fail" se houver uma discrepância entre o resultado obtido e o esperado.

Este código é uma boa prática para garantir que a função principal (`repeat_string`) esteja produzindo os resultados esperados em uma variedade de situações. Se precisar de mais esclarecimentos ou tiver alguma dúvida específica, estou à disposição!'''

'''A função random_test_repeat_string gera 5 casos de teste aleatórios. 
Para cada teste, cria uma string s com caracteres aleatórios entre 'a', 'b' e 'c' 
com um comprimento aleatório entre 1 e 10. Além disso, gera um número aleatório n entre 1 e 5. 
A função então compara o resultado da função repeat_string com o resultado esperado e imprime "Pass" 
se estiver correto e "Fail" se não estiver.'''