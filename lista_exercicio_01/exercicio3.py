

def main():
    USUARIO = 'admin'
    SENHA = '1234'
    while True:
        userlogin = input(str('Digite o nome de usuário:\n>>> '))
        userpassword = input(str('Digite a senha:\n>>> '))

        if (userlogin == USUARIO and userpassword == SENHA):
            print('Usuário logado com sucesso.')
            break
        else:
            print('\n\nDados incorretos.\n\n')
            pass

if __name__ == '__main__':
    main()