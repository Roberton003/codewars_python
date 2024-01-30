def data_reverse(data):
    # Divide a lista em segmentos de 8 bits
    bytes = [data[i:i+8] for i in range(0, len(data), 8)]
    # Inverte a ordem dos segmentos
    bytes_invertidos = bytes[::-1]
    # Junta os segmentos de volta em uma única lista
    return [bit for byte in bytes_invertidos for bit in byte]

# Testa a função data_reverse com entradas de exemplo
data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
print("Antes da inversão:", data1)
data1_invertida = data_reverse(data1)
print("Depois da inversão:", data1_invertida)
assert data1_invertida == [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

data3 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
print("Antes da inversão:", data3)
data3_invertida = data_reverse(data3)
print("Depois da inversão:", data3_invertida)
assert data3_invertida == [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]