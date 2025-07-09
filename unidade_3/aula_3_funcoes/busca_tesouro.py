import random

locais = ['caverna', 'praia', 'floresta', 'deserto', 'castelo']

# def local_tesouro():


#     while True:
#         escolha = int(input('Escolha onde deseja buscar:\n1. caverna\n2. praia\n3. floresta\n4. deserto\n5. castelo\n>>>'))
#         if locais[(escolha) - 1] == local_do_tesouro:
#             print('Parabéns, você encontrou o tesouro!')
#             break
#         else:
#             print('Você errou, tente novamente.')
#             pass

def menu_opcoes():
    escolha = int(input('Escolha onde deseja buscar:\n1. caverna\n2. praia\n3. floresta\n4. deserto\n5. castelo\n>>>'))
    return escolha

def validar(escolha_jogador, local_correto):
    if locais[(escolha_jogador) - 1] == local_correto:
        print('Você encontrou!!!')
        exit()
    else:
        print('Você errou, tente novamente.')
        pass

def jogo():
    print('Bem-vindo à caça ao tesouro!')
    local_do_tesouro = random.choice(locais)
    while True:
        validar(menu_opcoes(), local_do_tesouro)
        print(f'a escolha correta era {local_do_tesouro}')

jogo()


