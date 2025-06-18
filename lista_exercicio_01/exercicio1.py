def main():
    IDADE_MINIMA = 16
    nome = str(input('Digite o nome do aluno:\n>>> '))
    idade = int(input('Digite a idade do aluno\n>>> '))
    while True:
        autorizacao = str(input("Possui autorização? Digite o número da sua resposta\n1. SIM\n2. NÃO\n>>> "))
        try:
            if (autorizacao == '1') and (idade >= IDADE_MINIMA):
                print(f'O aluno {nome} está autorizado a participar do evento.')
                break
            elif (autorizacao == '1') or (idade <= IDADE_MINIMA):
                print(f'O aluno {nome} não está autorizado a participar do evento.')
                break
        except:
            print('A resposta para a autorização deve ser sim ou não.')

if __name__ == "__main__":
    main()