# Define a função abrevia_nome que recebe um nome como parâmetro
def abrevia_nome(nome):
    # Divide o nome em partes separadas por espaços
    partes = nome.split()
    # Obtém as iniciais de cada parte do nome, convertendo-as para maiúsculas
    iniciais = [p[0].upper() for p in partes]
    # Retorna as iniciais separadas por pontos
    return '.'.join(iniciais)

print(abrevia_nome("Sam Harris"))  # S.H
print(abrevia_nome("patrick feeney"))  # P.F