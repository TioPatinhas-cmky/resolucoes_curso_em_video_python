n = vezes = somar = 0
n = int(input('Digite um número [999 pra parar]: '))
while n != 999:
    somar += n
    n = int(input('Digite um número [999 pra parar]: '))
    if n + 1:
        vezes += 1 
print(f'Você digitou {vezes} números, e a soma entre eles foi {somar}')