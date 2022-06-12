peso = float(input('Qual é o seu peso?(KG)'))
altura = float(input('Qual é a sua altura?(M)'))
imc = peso / (altura ** peso)

print(f'O imc dessa pessoa é de {imc :.1f}')

if imc <= 18.5:
    print('Abaixo do peso.')

elif imc <= 25:
    print('Peso ideal.')

elif imc <= 30:
    print('Sobrepeso.')

elif imc <= 40:
    print('Obesidade.')

else:
    print('Obesidade Mórbida.')