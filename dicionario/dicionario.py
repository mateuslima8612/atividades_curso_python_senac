usuarios = []

def adicionar_usuario():
    while True:
        #usuario realiza o cadastro
        nome = input('digite o nome: ')
        idade = input('idade: ')
        cidade = input('cidade: ')

        #inclui o usuario em um dicionário dentro da lista 'usuarios'
        usuarios.append({'nome': nome, 'idade': idade, 'cidade': cidade})
        escolha_final = input('deseja continuar? 1. sim | 2. sair\n\n>>>')
        if escolha_final == '1':
            pass
        else:
            break
    
adicionar_usuario()
for i in range(len(usuarios)):
    for j in [i]:
        print(f'O usuario {usuarios[i]['nome']} tem {usuarios[i]['idade']} e mora em {usuarios[i]['cidade']}')

for item in usuarios:
    print(item['nome'])

print(f'\n\n\n{usuarios[0].keys()}\n{usuarios[0].values()}')