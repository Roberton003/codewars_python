'''Você é o “especialista em informática” de uma Associação Atlética local (CAA). Muitas equipes de corredores vêm competir. Cada vez que você obtém uma sequência de todos os resultados das corridas de cada equipe que correu. Por exemplo, aqui está uma string mostrando os resultados individuais de uma equipe de 5 corredores:

"01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"

Cada parte da string tem o formato: h|m|s onde h, m, s (h para hora, m para minutos, s para segundos) são números inteiros positivos ou nulos (representados como strings) com um ou dois dígitos. As substrings na string de entrada são separadas por , ou ,.

Para comparar os resultados das equipes é solicitado que você forneça três estatísticas; intervalo, média e mediana .

Range: diferença entre os valores mais baixos e mais altos. Em {4, 6, 9, 3, 7} o valor mais baixo é 3 e o mais alto é 9, então o intervalo é 9 − 3 = 6.

Mean or Average: Para calcular a média, some todos os números e divida a soma pela contagem total de números.

Median: Nas estatísticas, a mediana é o número que separa a metade superior de uma amostra de dados da metade inferior. A mediana de uma lista finita de números pode ser encontrada organizando todas as observações do valor mais baixo para o valor mais alto e escolhendo o do meio (por exemplo, a mediana de {3, 3, 5, 9, 11} é 5) quando há um número ímpar de observações. Se houver um número par de observações, então não existe um único valor médio; a mediana é então definida como a média dos dois valores intermediários (a mediana de {3, 5, 6, 9} é (5 + 6) / 2 = 5,5).

Sua tarefa é retornar uma string fornecendo esses 3 valores. Para o exemplo dado acima, o resultado da string será

"Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"

no formato: "Intervalo: hh|mm|ss Média: hh|mm|ss Mediana: hh|mm|ss"`

onde hh, mm, ss são inteiros (representados por strings) com 2 dígitos cada .

Observações :
se o resultado em segundos for ab.xy... ele será truncado como ab.
se a string fornecida for "" você retornará '''

'''Para resolver essa tarefa, você pode seguir os seguintes passos:

Divida a string de entrada em uma lista de tempos.
Converta cada tempo para segundos.
Calcule o intervalo, a média e a mediana dos tempos em segundos.
Converta o intervalo, a média e a mediana de volta para o formato hh|mm|ss.
Retorne uma string com o intervalo, a média e a mediana.'''

def estatisticas_corrida(s):
    """
    Calcula estatísticas de uma corrida com base nos tempos fornecidos.

    Args:
        s (str): String contendo os tempos separados por vírgula e espaço.

    Returns:
        str: String contendo as estatísticas calculadas, incluindo o intervalo, a média e a mediana dos tempos.

    Example:
        >>> estatisticas_corrida("01|30|00, 02|15|30, 01|45|45")
        'Range: 00|45|30 Average: 01|50|05 Median: 01|45|45'
    """

    if not s:
        return ''

    def para_segundos(tempo):
        h, m, s = map(int, tempo.split('|'))
        return h * 3600 + m * 60 + s

    def para_tempo(segundos):
        h = segundos // 3600
        m = (segundos % 3600) // 60
        s = segundos % 60
        return f"{h:02d}|{m:02d}|{s:02d}"

    tempos = sorted(para_segundos(tempo) for tempo in s.split(', '))
    intervalo = tempos[-1] - tempos[0]
    media = sum(tempos) // len(tempos)
    mediana = tempos[len(tempos) // 2] if len(tempos) % 2 == 1 else (tempos[len(tempos) // 2 - 1] + tempos[len(tempos) // 2]) // 2

    return f"Range: {para_tempo(intervalo)} Average: {para_tempo(media)} Median: {para_tempo(mediana)}"
