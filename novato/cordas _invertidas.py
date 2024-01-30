def inverter_string(s):
    """
    Inverte a string passada como parâmetro.

    Parâmetros:
    - s (str): A string a ser invertida.

    Retorna:
    A string invertida.
    """
    return s[::-1]

def test_inverter_string():
    """
    Testa a função inverter_string com alguns casos de teste.

    Imprime 'Pass' se o teste passar e 'Fail' se falhar.
    """
    test_cases = [
        ("Olá, mundo!", "!odnum ,álO"),
        ("abcdef", "fedcba"),
        ("12345", "54321"),
        ("", ""),  # Testando com uma string vazia
    ]

    for original, expected_output in test_cases:
        result = inverter_string(original)
        try:
            assert result == expected_output
            print(f"Pass: inverter_string('{original}') == '{expected_output}'")
        except AssertionError:
            print(f"Fail: inverter_string('{original}') != '{expected_output}'")

# Executando os testes
test_inverter_string()
