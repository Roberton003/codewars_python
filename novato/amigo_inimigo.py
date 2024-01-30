# Este código define uma função chamada "amigos" que recebe uma lista de nomes como entrada.
# Ele retorna uma nova lista contendo apenas os nomes que possuem um comprimento de 4 caracteres.
def amigos(lista):
    return [nome for nome in lista if len(nome) == 4]

print(amigos(["Ryan", "Kieran", "Jason", "Você"]))  # ["Ryan", "Você"]
print(amigos(["Ryan", "Kieran", "Mark"]))  # ["Ryan", "Mark"]