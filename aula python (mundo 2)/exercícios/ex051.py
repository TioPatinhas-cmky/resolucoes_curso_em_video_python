primeiro = int(input('Primeiro termo: '))
razao = int(input('Razâo: '))
decimo = primeiro + (10 - 1) * razao
for c in range (primeiro, decimo + razao, razao):
    print(c, end='>')
print('Acabou')