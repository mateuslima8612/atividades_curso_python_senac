numero = int(input('digite um número:\n>>>'))

if (numero < 100):
    while numero < 101:
        print(numero)
        numero += 1
else:
    print('o numero deve ser menor que 100')