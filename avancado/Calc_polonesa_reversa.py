# Importamos o módulo unittest, que fornece uma estrutura para escrever e executar testes de unidade em Python.
import unittest

# Definimos a função calc, que avalia expressões em notação polonesa reversa.
def calc(expr):
    # Se a expressão estiver vazia, retornamos 0.
    if not expr:
        return 0

    # Dividimos a expressão em tokens.
    tokens = expr.split()

    # Inicializamos a pilha.
    stack = []

    # Para cada token na expressão.
    for token in tokens:
        # Se o token for um operador.
        if token in "+-*/":
            # Pegamos os dois últimos números da pilha.
            num2 = stack.pop()
            num1 = stack.pop()

            # Realizamos a operação e colocamos o resultado de volta na pilha.
            if token == "+":
                stack.append(num1 + num2)
            elif token == "-":
                stack.append(num1 - num2)
            elif token == "*":
                stack.append(num1 * num2)
            elif token == "/":
                stack.append(num1 / num2)
        # Se o token for um número, colocamos na pilha.
        else:
            stack.append(float(token))

    # O resultado da expressão é o único número restante na pilha.
    return stack[0]

# Definimos uma classe de teste para a função calc.
class TestCalc(unittest.TestCase):
    # Definimos um método de teste que verifica se a função calc retorna os resultados esperados para vários conjuntos de argumentos.
    def test_calc(self):
        self.assertEqual(calc(""), 0)  # A expressão vazia deve ser avaliada como 0.
        self.assertEqual(calc("3 4 +"), 7)  # 3 + 4 = 7
        self.assertEqual(calc("3 4 -"), -1)  # 3 - 4 = -1
        self.assertEqual(calc("3 4 *"), 12)  # 3 * 4 = 12
        self.assertEqual(calc("12 4 /"), 3)  # 12 / 4 = 3
        self.assertEqual(calc("5 1 2 + 4 * + 3 -"), 14)  # 5 + ((1 + 2) * 4) - 3 = 14

# Se este script for o arquivo principal que está sendo executado, executamos os testes.
if __name__ == '__main__':
    unittest.main()