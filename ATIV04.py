N1 = float(input('Informe a sua primeira nota: '))
N2 = float(input('Informe a sua segunda nota: '))

media = (N1+N2)/2
if (media==10):
    print('Aprovado com Distição, Sua média foi {}'.format(media))
elif (media>=7):
    print('Aprovado, Sua média foi {}'.format(media))
else:
    print('Reprovado, Sua média foi {}'.format(media)) 
