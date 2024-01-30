# Define a função conta_ovelhas que recebe uma lista de ovelhas como parâmetro
def conta_ovelhas(ovelhas):
    # Retorna a contagem de ovelhas verdadeiras na lista
    return ovelhas.count(True)

# Define a lista de ovelhas
ovelhas = [True, True, True, False, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True, True, False, False, True, True]
print(conta_ovelhas(ovelhas))  # 17