'''DESCRIÇÃO:
História
Sua empresa migrou os últimos 20 anos de dados muito importantes para uma nova plataforma, em múltiplas fases. No entanto, algo deu errado: alguns dos carimbos de data/hora essenciais estavam confusos! Parece que alguns servidores foram configurados para usar o dd/mm/yyyyformato de data, enquanto outros usaram o mm/dd/yyyyformato durante a migração. Infelizmente, o banco de dados original foi corrompido no processo e não há backups disponíveis... Agora cabe a você avaliar os danos.

Tarefa
Você receberá uma lista de registros como strings na forma [start_date, end_date]fornecida no yyyy-mm-ddformato ISO, e sua tarefa é contar quantos desses registros são:

correto : não pode haver nada de errado com as datas, o mês/dia não pode ser confundido ou não seria um carimbo de data/hora válido de qualquer outra forma; por exemplo["2015-04-04", "2015-05-13"]
recuperável : inválido em sua forma atual, mas o timestamp original pode ser recuperado, pois só existe uma combinação válida possível; por exemplo["2011-10-08", "2011-08-14"]
incerto : o carimbo de data/hora original não pode ser recuperado porque uma ou ambas as datas são ambíguas e podem gerar vários resultados válidos ou podem gerar apenas resultados inválidos; por exemplo["2002-02-07", "2002-12-10"]
Nota: os registros originais sempre definiram uma duração não negativastart_date ≤ end_date (ou seja )

Retorne suas descobertas em um array:[ correct_count, recoverable_count, uncertain_count ]

Exemplos
["2015-04-04", "2015-05-13"]  -->  correct     # nothing (could be) wrong here
["2013-06-18", "2013-08-05"]  -->  correct     # end date is ambiguous, but this is
                                               # the only possible valid version
["2001-02-07", "2001-03-01"]  -->  correct     # both dates are ambiguous, but this is
                                               # the only possible valid version
["2011-10-08", "2011-08-14"]  -->  recoverable # start date is wrong, but can be corrected
                                               # because there is only one valid version possible
["2009-08-21", "2009-04-12"]  -->  recoverable # end date is wrong, but can be corrected
                                               # because there is only one valid version possible
["1996-01-24", "1996-03-09"]  -->  uncertain   # end date is ambiguous (could also be 1996-09-03)
["2000-10-09", "2000-11-20"]  -->  uncertain   # start date is ambiguous (could also be 2000-09-10)
["2002-02-07", "2002-12-10"]  -->  uncertain   # both dates are ambiguous, and there are
                                               # multiple possible valid versions
                                               
                                               '''
# SOLUÇÃO:
def is_valid_date(date):
    year, month, day = date
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return day <= 29
        else:
            return day <= 28
    elif month in [4, 6, 9, 11]:
        return day <= 30
    else:
        return day <= 31

def check_dates(records):
    correct = recoverable = uncertain = 0
    for record in records:
        start_date = list(map(int, record[0].split('-')))
        end_date = list(map(int, record[1].split('-')))
        start_valid = is_valid_date(start_date)
        end_valid = is_valid_date(end_date)
        start_recoverable = start_date[1] <= 31 and start_date[2] <= 12 and not start_valid
        end_recoverable = end_date[1] <= 31 and end_date[2] <= 12 and not end_valid

        if start_valid and end_valid:
            if start_date <= end_date:
                correct += 1
            else:
                uncertain += 1
        elif start_valid and end_recoverable:
            if start_date <= [end_date[0], end_date[2], end_date[1]]:
                recoverable += 1
            else:
                uncertain += 1
        elif end_valid and start_recoverable:
            if [start_date[0], start_date[2], start_date[1]] <= end_date:
                recoverable += 1
            else:
                uncertain += 1
        else:
            uncertain += 1

    return [correct, recoverable, uncertain]

def main():
    records = [
        ["2015-04-04", "2015-05-13"],  # correct
        ["2013-06-18", "2013-08-05"],  # correct
        ["2001-02-07", "2001-03-01"],  # correct
        ["2011-10-08", "2011-08-14"],  # recoverable
        ["2009-08-21", "2009-04-12"],  # recoverable
        ["1996-01-24", "1996-03-09"],  # uncertain
        ["2000-10-09", "2000-11-20"],  # uncertain
        ["2002-02-07", "2002-12-10"]]  # uncertain

    result = check_dates(records)

    print(result)  # [3, 2, 3]

if __name__ == "__main__":
    main()