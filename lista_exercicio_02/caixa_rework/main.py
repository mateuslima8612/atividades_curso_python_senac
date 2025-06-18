import db

def main():
    while True:
        escolha = input('escolha uma opção:\n1. cadastro\n2. sair\n>>>')
        if escolha == '1':
            user = input('Para iniciarmos o cadastro, digite o seu nome:\n\n>>>')
            password = input('Agora digite uma senha para realizar o seu cadastro:\n\n>>>')
            db.CaixaOnline.user_registration(user, password, 0)
        elif escolha == '2':
            db.con.close()
            break

main()
