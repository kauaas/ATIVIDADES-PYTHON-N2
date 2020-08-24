 
N1 = float (input('Informe um número: '))
N2 = float (input('Informe um número: '))
N3 = float (input('Informe um número: '))

if (N1>N2) and (N1>N3):
    print('O maior número é {} '.format(N1))
elif (N2>N1) and (N2>N3):
    print('O maior número é {} '.format(N2))
else:
    print('O maior número é {} '.format(N3))

if (N1<N2) and (N1<N3):
    print('O menor número é {}'.format(N1))
elif (N2<N1) and (N2<N3):
    print('O menor número é {}'.format(N2))
else:
    print('O menor número é {}'.format(N3))
