# Define uma função chamada findNeedle que recebe uma lista chamada haystack como entrada.
def findNeedle(haystack):
    # Retorna uma string que indica a posição da palavra 'needle' na lista haystack.
    return f"encontrou a agulha na posição {haystack.index('needle')}"

print(findNeedle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))  # "found the needle at position 5"