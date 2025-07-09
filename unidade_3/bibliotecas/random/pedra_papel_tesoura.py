import random
def main():
    while True:    
        menu_escolha = input('escolha o número de uma opção:\n1. jogar\n2. sair')
        if menu_escolha == '1':
            escolha_numero = int(input("Escolha um número: \n1. Pedra\n2. Papel\n3. Tesoura\n>>>"))
            escolhas = ['pedra', 'papel', 'tesoura']
            escolha_jogador = escolhas[(escolha_numero - 1)]

            escolha_computador = random.choice(escolhas)

            if escolha_computador == escolha_jogador:
                print(f'Jogador escolheu {escolha_jogador}\nComputador escolheu {escolha_computador}\nEmpate')

            elif (escolha_computador == 'pedra' and escolha_jogador == 'tesoura') or (escolha_computador == 'tesoura' and escolha_jogador == 'papel') or (escolha_computador == 'papel' and escolha_jogador == 'pedra'):
                print(f'Jogador escolheu {escolha_jogador}\nComputador escolheu {escolha_computador}\nDerrota')

            else:
                print(f'Jogador escolheu {escolha_jogador}\nComputador escolheu {escolha_computador}\nVitoria')
        else:
            break
    
main()