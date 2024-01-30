import random

def litros_ciclismo(tempo_horas):
    """
    Calcula a quantidade de litros que Nathan deve beber durante o ciclismo.

    Parâmetros:
    - tempo_horas (float): O tempo em horas de ciclismo.

    Retorna:
    A quantidade de litros de água arredondada para baixo.
    """
    litros_por_hora = 0.5
    quantidade_litros = tempo_horas * litros_por_hora
    return int(quantidade_litros)  # Arredonda para baixo

def random_test_quantidade_litros_ciclismo():
    """
    Testa a função quantidade_litros_ciclismo com 5 casos de teste aleatórios.

    Imprime 'Pass' se o teste passar e 'Fail' se falhar.
    """
    for _ in range(5):
        tempo_horas = round(random.uniform(1, 10), 2)  # Tempo aleatório entre 1 e 10 horas
        expected_output = int(tempo_horas * 0.5)  # Cálculo esperado da quantidade de litros
        result = litros_ciclismo(tempo_horas)
        
        try:
            assert result == expected_output
            print(f"Pass: litros_ciclismo({tempo_horas}) == {expected_output} litros")
        except AssertionError:
            print(f"Fail: litros_ciclismo({tempo_horas}) != {expected_output} litros")

# Executando os testes aleatórios
random_test_quantidade_litros_ciclismo()
