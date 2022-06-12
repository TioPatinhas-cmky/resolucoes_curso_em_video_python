frase = str(input('Digite uma frase: ')).upper() .strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira posição que encontrei o A foi {}'.format(frase.find('A')+1))
print('a última letra A que encontrei foi na posição {}'.format(frase.rfind('A')+1))