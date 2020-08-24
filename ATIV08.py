N1 = float(input('Informe o primeiro número: '))
N2 = float(input('Informe o segundo número: '))
N3 = float(input('Informe o terceiro número: '))

if (N1<N2) and (N1<N3) and (N2<N3):
    print (N1,N2,N3)
elif (N2<N1) and (N2<N3) and (N1<N3):
    print(N2,N1,N3)
else:
    print(N3,N1,N2)
