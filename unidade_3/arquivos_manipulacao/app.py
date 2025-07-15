from limpar import limpar_tela
import os

# caminho = 'tarefas.txt'
# lista_tarefas = []

# def ler_arquivo(caminho):
#     try:    
#         limpar_tela()
#         with open(caminho, 'r', encoding='utf-8') as arquivo:
#             print('Lista de tarefas:')
#             print(arquivo.read())
#     except:
#         print('Sem tarefas.')

# def atualizar_arquivo(caminho):
#     with open(caminho, 'a', encoding='utf-8') as arquivo:   
#         texto = input('digite uma nova tarefa:\n>>>')
#         arquivo.write(texto)

# while True:
#     ler_arquivo(caminho)
    
#     try:
#         escolha = int(input('Escolha uma opção:\n1. adicionar nova tarefa\n2. apagar lista de tarefas\n>>>'))
#         if escolha == 1:
#             limpar_tela()
#             atualizar_arquivo(caminho)
#             ler_arquivo(caminho)
#         elif escolha == 2:
#             limpar_tela()
#             try:
#                 os.remove(caminho)
#             except:
#                 print('Não há tarefas para remover')
#                 input('Pressione enter para continuar:')
#     except ValueError:
#         print('Escolha inválida')
#         input('Pressione enter para continuar:')

lista = 'lista.txt'

# garante que o arquivo existe e tem uma lista válida
if not os.path.exists(lista):
    with open(lista, 'w', encoding='utf-8') as f:
        f.write('[]')

def listar():
    global nova_lista_eval
    limpar_tela()
    with open(lista, 'r', encoding='utf-8') as arquivo:
        nova_lista = arquivo.read().strip()
        try:
            nova_lista_eval = eval(nova_lista) if nova_lista else []
        except:
            nova_lista_eval = []
    for i in range(len(nova_lista_eval)):
        print(f'{i + 1}. {nova_lista_eval[i]}')

def deletar(item):
    nova_lista_eval.pop(item - 1)
    with open(lista, 'w', encoding='utf-8') as arquivo:
        arquivo.write(str(nova_lista_eval))
    listar()

def criar(item):
    nova_lista_eval.append(item)
    with open(lista, 'w', encoding='utf-8') as arquivo:
        arquivo.write(str(nova_lista_eval))
    listar()

while True:
    listar()
    try:
        escolha = int(input('\nDigite uma opção:\n1. Criar nova tarefa\n2. Deletar tarefa\n\n>>>'))
        if escolha == 1:
            item = input('Escreva uma tarefa para adicioná-la à lista de tarefas:\n\n>>>')
            criar(item)
        elif escolha == 2:
            try:
                item = int(input('\nDigite o número da tarefa que deseja deletar\n\n>>>'))
                deletar(item)
            except:
                print('Escolha inválida.')
                input('Aperte enter para continuar:\n>>>')
    except:
        print('Escolha inválida.')
        input('Aperte enter para continuar:\n>>>')
