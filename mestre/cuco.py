'''O pássaro cuco sai do relógio cuco e toca uma vez a cada quarto de hora, meia hora e três quartos de hora. No início de cada hora (1-12), a hora soa. Dado o tempo atual e um número n , determine o momento em que o pássaro cuco cantou n   vezes.

Parâmetros de entrada:
tempo_inicial - uma string no formato "HH:MM", onde 1 ≤ HH ≤ 12 e 0 ≤ MM ≤ 59, com 0's iniciais se necessário.
n - um número inteiro que representa o número alvo de sinos, com 1 <= n <= 200.

Valor de retorno: o momento em que o pássaro cuco tocou n   vezes - uma string no mesmo formato que inicial_time .

Se o pássaro cuco tocar em Initial_time , inclua esses toques na contagem. Se o enésimo toque for atingido na hora, informe a hora no início dessa hora (ou seja, suponha que o cuco termine de tocar antes do minuto acabar).

Exemplo: "03:38", 19   deve retornar "06:00" .
Explicação: Toca uma vez às "03:45" , 4 vezes às "04:00" , uma vez cada às "04:15", "04:30", "04:45" , 5 vezes às "05:00" , e uma vez em "05:15", "05:30", "05:45" . Neste ponto, ele tocou 16 vezes, então o 19º toque ocorre quando ele toca 6 vezes às "06:00" .'''

def momento_cuco(tempo_inicial, n):
    hora, minuto = map(int, tempo_inicial.split(':'))
    toques = 0

    while toques < n:
        if minuto == 0:
            toques += hora
        elif minuto % 15 == 0:
            toques += 1

        if toques >= n:
            break

        minuto += 1
        if minuto == 60:
            minuto = 0
            hora = 1 if hora == 12 else hora + 1

    return f"{hora:02d}:{minuto:02d}"

# Exemplo de uso
initial_times = ["07:22", "12:22", "01:30", "04:01", "03:38"]
n_values = [1, 2, 2, 10, 19]
momento_final = []

for tempo_inicial, n in zip(initial_times, n_values):
    momento_final.append(momento_cuco(tempo_inicial, n))

print(momento_final)  # ["07:30", "12:45", "01:45", "05:30", "06:00"]