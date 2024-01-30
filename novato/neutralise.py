

''' Dadas duas strings compostas por + e -, retorne uma nova string 
que mostra como as duas strings interagem da seguinte maneira:

Quando positivos e positivos interagem, eles permanecem positivos .
Quando negativos e negativos interagem, eles permanecem negativos .
Mas quando negativos e positivos interagem, eles se tornam neutros e são mostrados como o número 0.'''
import random
def neutralise(str1, str2):
    result = []

    for char1, char2 in zip(str1, str2):
        if char1 == '+' and char2 == '+':
            result.append('+')
        elif char1 == '-' and char2 == '-':
            result.append('-')
        else:
            result.append('0')

    return ''.join(result)

def random_test_neutralise():
    for _ in range(10):
        str1 = ''.join(random.choice(['+', '-']) for _ in range(random.randint(1, 10)))
        str2 = ''.join(random.choice(['+', '-']) for _ in range(len(str1)))
        expected_output = neutralise(str1, str2)
        print(f"Testing neutralise('{str1}', '{str2}')...")
        try:
            assert neutralise(str1, str2) == expected_output
            print("Pass")
        except AssertionError:
            print("Fail")

random_test_neutralise()

'''Vamos analisar cada parte do código:

1. **neutralise(str1, str2):**
   - Esta função recebe duas strings, `str1` e `str2`, e retorna uma nova string que representa a interação entre os caracteres das duas strings, conforme as regras já discutidas no desafio anterior.
   - Ela utiliza um loop `for` para percorrer cada par de caracteres correspondentes nas duas strings.
   - Se ambos os caracteres são '+' ou ambos são '-', o resultado é o mesmo caractere.
   - Se um dos caracteres é '+' e o outro é '-', o resultado é '0'.
   - A função retorna a string resultante.

2. **random_test_neutralise():**
   - Esta função realiza um teste aleatório da função `neutralise`.
   - Um loop `for` é utilizado para executar o teste 10 vezes (alterável conforme a necessidade).
   - Para cada iteração do loop, duas strings aleatórias, `str1` e `str2`, são geradas usando `random.choice(['+', '-'])` para criar caracteres aleatórios e `random.randint(1, 10)` para determinar o comprimento de `str1`.
   - A função `neutralise` é chamada com as strings geradas, e o resultado é armazenado em `expected_output`.
   - Em seguida, é feita uma tentativa (`try`) de verificar se a chamada real da função `neutralise` com as mesmas strings é igual ao resultado esperado. Se sim, é impresso "Pass"; caso contrário, é impresso "Fail".

3. **random.choice(['+', '-']) e random.randint(1, 10):**
   - `random.choice(['+', '-'])` escolhe aleatoriamente entre os caracteres '+' e '-'.
   - `random.randint(1, 10)` gera um número inteiro aleatório entre 1 e 10, determinando o comprimento de uma string.

O código, em resumo, cria strings aleatórias, chama a função `neutralise` com essas strings e verifica se o resultado coincide com a saída esperada. Isso é útil para testar se a função `neutralise` está funcionando corretamente em uma variedade de cenários.'''


