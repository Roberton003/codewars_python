def soma_positivos(lista):
    return sum(n for n in lista if n > 0)

print(soma_positivos([1, -4, 7, 12]))  # 20