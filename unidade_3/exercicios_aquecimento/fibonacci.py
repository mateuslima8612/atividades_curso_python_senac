numero_1 = 0
numero_2 = 1

resultado = 0

while (resultado < 2000):
    resultado = (numero_1 + numero_2)
    print(resultado)
    numero_1 = numero_2
    numero_2 = resultado
