# Esta função calcula o próximo quadrado perfeito dado um número 'n'.
def proximo_quadrado_perfeito(n):
    raiz = n ** 0.5
    if raiz.is_integer():
        return (raiz + 1) ** 2
    else:
        return -1

print(proximo_quadrado_perfeito(121))  # 144
print(proximo_quadrado_perfeito(625))  # 676
print(proximo_quadrado_perfeito(114))  # -1