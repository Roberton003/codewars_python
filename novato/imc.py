def calcular_imc(peso, altura):
    """
    Calcula o índice de massa corporal (IMC) e fornece uma descrição com base nas faixas.

    Parâmetros:
    - peso (float): Peso em quilogramas.
    - altura (float): Altura em metros.

    Retorna:
    Uma string representando a descrição do IMC.
    """
    imc = peso / altura ** 2

    if imc <= 18.5:
        return "Abaixo do peso"
    elif imc <= 25.0:
        return "Normal"
    elif imc <= 30.0:
        return "Excesso de peso"
    else:
        return "Obeso"

def testar_calculo_imc():
    """
    Testa a função calcular_imc com diversos casos.

    Imprime 'Pass' se o teste passar e 'Fail' se falhar.
    """
    test_cases = [
        (60, 1.70, "Normal"),     # Peso normal
        (70, 1.75, "Excesso de peso"),  # Excesso de peso
        (50, 1.65, "Abaixo do peso"),   # Abaixo do peso
        (90, 1.80, "Obeso"),      # Obeso
    ]

    for peso, altura, expected_output in test_cases:
        result = calcular_imc(peso, altura)
        try:
            assert result == expected_output
            print(f"Pass: calcular_imc({peso}, {altura}) == '{expected_output}'")
        except AssertionError:
            print(f"Fail: calcular_imc({peso}, {altura}) != '{expected_output}'")

# Executando os testes
testar_calculo_imc()
