# Esta função `printer_error` conta o número de caracteres na string `s` que são maiores que 'm'.
# Ela retorna uma string no formato "{erros}/{len(s)}", onde `erros` é a contagem de caracteres maiores que 'm'
# e `len(s)` é o comprimento total da string `s`.
def printer_error(s):
    erros = sum(1 for c in s if c > 'm')
    return f"{erros}/{len(s)}"

print(printer_error("aaabbbbhaijjjm"))  # "0/14"
print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))  # "8/22"