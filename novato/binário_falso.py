from __future__ import absolute_import

def substituir_digitos(seq):
    """
    Substitui dígitos abaixo de 5 por '0' e dígitos 5 e superiores por '1'.

    Parâmetros:
    - seq (str): Sequência de dígitos.

    Retorna:
    Uma string resultante da substituição de dígitos.
    """
    resultado = ''.join('0' if int(digito) < 5 else '1' for digito in seq)
    return resultado

# Exemplo de uso:
sequencia_original = "374892"
resultado_substituido = substituir_digitos(sequencia_original)
print(f"A sequência original: {sequencia_original}")
print(f"A sequência substituída: {resultado_substituido}")

import random

def testar_substituir_digitos():
    """
    Testa a função substituir_digitos com 5 casos de teste aleatórios.

    Imprime 'Pass' se o teste passar e 'Fail' se falhar.
    """
    for _ in range(5):
        sequencia_original = ''.join(str(random.randint(0, 9)) for _ in range(random.randint(1, 10)))
        resultado_esperado = ''.join('0' if int(digito) < 5 else '1' for digito in sequencia_original)
        resultado_obtido = substituir_digitos(sequencia_original)
        
        try:
            assert resultado_obtido == resultado_esperado
            print(f"Pass: substituir_digitos('{sequencia_original}') == '{resultado_esperado}'")
        except AssertionError:
            print(f"Fail: substituir_digitos('{sequencia_original}') != '{resultado_esperado}'")

# Executando os testes
testar_substituir_digitos()

