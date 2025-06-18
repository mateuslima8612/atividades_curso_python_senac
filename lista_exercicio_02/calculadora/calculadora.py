
def soma(num1, num2):
    print(num1 + num2)

def subtracao(num1, num2):
    print(num1 - num2)

def multiplicacao(num1, num2):
    print(num1 * num2)

def divisao(num1, num2):
    print(num1 / num2)

def raiz(num1):
    for i in range(num1):
        if (i * i) == num1:
            print(f'A raiz quadrada de {num1} é {i}')

def potenciacao(num1, num2):
    potencia = num1
    for i in range(num2 - 1):
        num1 = num1 * potencia
    print(f'O resultado da potenciacao de {potencia} elevado a {num2} é {num1}')

def conversao_fahrenheit(num1):
    fahrenheit = 9 / 5 * num1 + 35
    print(f'{num1} convertido para fahrenheit é {fahrenheit}')