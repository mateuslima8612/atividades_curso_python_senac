def main():
    APROVADO = 7
    RECUPERACAO = 5
    while True:
        try:
            media = int(input('Digite a media do aluno:\n>>> '))
            if (media > 10):
                print('Valor inválido')
            else:
                break
        except:
            print('Valor inválido.')



    if (media > APROVADO):
        print('O aluno foi aprovado.')
    elif (media < RECUPERACAO):
        print('O aluno foi reprovado.')
    else:
        print('O aluno foi reprovado.')

if __name__ == '__main__':
    main()