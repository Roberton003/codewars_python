# Importamos o módulo unittest, que fornece uma estrutura para escrever e executar testes de unidade em Python.
import unittest

# Definimos a função mormons, que calcula o número de missões necessárias para atingir um número alvo de seguidores.
def mormons(starting_number, reach, target):
    # Se o número atual de mórmons é maior ou igual ao alvo, retornamos 0, pois não precisamos de mais missões.
    if starting_number >= target:
        return 0
    # Se o número atual de mórmons é menor que o alvo, fazemos uma chamada recursiva à função, adicionando o número de mórmons que cada missão alcança ao número atual de mórmons.
    else:
        return 1 + mormons(starting_number + starting_number * reach, reach, target)

# Definimos uma classe de teste para a função mormons.
class TestMormons(unittest.TestCase):
    # Definimos um método de teste que verifica se a função mormons retorna os resultados esperados para vários conjuntos de argumentos.
    def test_mormons(self):
        self.assertEqual(mormons(10, 3, 9), 0)  # O número de seguidores já excede o alvo, então o resultado deve ser 0.
        self.assertEqual(mormons(40, 2, 120), 1)  # Após 1 missão, o número de mórmons é igual ao alvo, então o resultado deve ser 1.
        self.assertEqual(mormons(20000, 2, 7000000000), 12)  # Leva 12 missões para atingir o alvo, então o resultado deve ser 12.

# Se este script for o arquivo principal que está sendo executado, executamos os testes.
if __name__ == '__main__':
    unittest.main()
 