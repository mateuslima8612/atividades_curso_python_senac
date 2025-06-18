def main():
    while True:
        try:
            numero = int(input('\n\nDe que número você deseja ver a tabuada?\n\n>>>'))
            tabuada = int(input('\n\nAté que número você gostaria de ver a tabuada?\n\n>>>'))
            for i in range(tabuada):
                print(f'{numero} x {(i + 1)} = {(numero * (i + 1))}')
            escolha_fim = int(input('\nDeseja gerar outra tabuada?\n1. Sim\n2. Não\n\n>>>'))
            if (escolha_fim == 1):
                pass
            else:
                break
            
        except:
            print('Valor inválido!')
            break
if __name__ == '__main__':
    main()


