def time_since_midnight():
    h = int(input("Digite as horas: "))
    m = int(input("Digite os minutos: "))
    s = int(input("Digite os segundos: "))
    milliseconds = (h * 3600 + m * 60 + s) * 1000
    return milliseconds

if __name__ == "__main__":
    print(time_since_midnight())



