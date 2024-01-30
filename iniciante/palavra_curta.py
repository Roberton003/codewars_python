# Esta função recebe uma string 's' como entrada e retorna o comprimento da palavra mais curta na string.
def comprimento_palavra_curta(s):
    return min(len(palavra) for palavra in s.split())

print(comprimento_palavra_curta("Eu amo Python"))  # 1
print(comprimento_palavra_curta("Python é ótimo"))  # 2