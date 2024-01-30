def dna_complementar(dna):
    """
    Retorna o complemento de uma sequência de DNA.

    Parâmetros:
    dna (str): A sequência de DNA a ser complementada.

    Retorna:
    str: A sequência de DNA complementar.

    Exemplo:
    >>> dna_complementar('ATCG')
    'TAGC'
    """
    complementos = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complementos[base] for base in dna)

print(dna_complementar("ATTGC"))  # "TAACG"
print(dna_complementar("GTAT"))  # "CATA"