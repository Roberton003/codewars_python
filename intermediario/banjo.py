# Esta função verifica se o nome de uma pessoa começa com a letra 'R'.
# Se sim, retorna o nome seguido de "toca banjo".
# Caso contrário, retorna o nome seguido de "não toca banjo".
def toca_banjo(nome):
    if nome[0].lower() == 'r':
        return nome + " plays banjo"
    else:
        return nome + " does not play banjo"

print(toca_banjo("Martin"))  # "Martin does not play banjo"
print(toca_banjo("Ricky"))  # "Ricky plays banjo"