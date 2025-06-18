'''Cores = {"azul": 150, 'vermelho': 200, 'verde': 250, 'amarelo': 300}

i = 0


def main():

    while True:
        cor = input('Qual é a cor da tatuagem\n1. azul\n2. vermelho\n3. verde\n4. amarelo\n>>> ')

        try:
            print(f'o valor da tatuagem {cor} é {Cores[cor]}')
            break
        except:
            print('Digite uma cor válida!!!')



def main():
    codigo = input('digite o codigo: ')
    horas_trabalhadas = int(input('digite as horas trabalhadas: '))

    vlr_hora = 22
    vlr_excedente = 33
    hora_max = 50

    if horas_trabalhadas > hora_max:
        excedente = horas_trabalhadas - hora_max
        saldo_normal = hora_max * vlr_hora
        saldo_excedente = excedente * vlr_excedente
        print(f'O valor excedente é {saldo_excedente}\n o valor final do salario é {saldo_excedente + saldo_normal}')
    else:
        saldo_normal = horas_trabalhadas * 22
        print(f'o valor do salário final é {saldo_normal}')



def main():
    lista = []
    for i in range(3):
        lista.append(input(int(f'digite o numero {i}: ')))
    novaLista = sorted(lista)
    print(f'o maior número da lista é {novaLista[-1]}')
'''

def main():
    par_ou_impar = int(input('digite um número para descobrir se é par ou ímpar: '))
    if(par_ou_impar % 2 == 0):
        print('o número é par')
    else:
        print('o numero é ímpar')



if __name__ == '__main__':
    main() 