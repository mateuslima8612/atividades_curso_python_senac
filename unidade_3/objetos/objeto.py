import os

def limpar():
    os.system('cls')

class BancoDeDados:
    def __init__(self):
        self.users = []
    
    def adicionar_usuario(self, novo_usuario):
        usuario_cadastrado = False

        for usuario in self.users:
            if novo_usuario.cpf == usuario.cpf:
                usuario_cadastrado = True
        
        if usuario_cadastrado:
            print('Usuário já existe no sistema')
            pass
        else:
            self.users.append(novo_usuario)
    
    def mostrar_usuarios(self):
        limpar()
        if self.users == []:
            print('Não há usuários cadastrados')
        else:
            for i in self.users:
                print(f'Nome: {i.nome} | Idade: {i.idade} | Endereço: {i.endereco} | CPF: {i.cpf}')

    def alterar_usuario(self):
        limpar()
        self.mostrar_usuarios()
        try:
            cpf_selecionado = input('Digite o CPF do usuário que deseja alterar\n>>>')
            encontrado = False
            for usuario in self.users:
                if cpf_selecionado == usuario.cpf:
                    encontrado = True
                    try:
                        escolha_alteracao = int(input('Digite o número da opção que deseja alterar:\n1. Nome\n2. Idade\n3. Endereço\n4. CPF\n>>>'))
                        if escolha_alteracao == 1:
                            usuario.nome = input('Digite o novo nome:')
                            print(f'Nome de usuário alterado para {usuario.nome}')
                        elif escolha_alteracao == 2:
                            usuario.idade = int(input('Digite a nova idade:'))
                            print(f'Idade de {usuario.nome} alterada para {usuario.idade}')
                        elif escolha_alteracao == 3:
                            usuario.endereco = input('Digite o novo endereço do usuário:')
                            print(f'Endereço alterado para {usuario.endereco}')
                        elif escolha_alteracao == 4:
                            usuario.cpf = input('Digite o novo CPF')
                            print(f'CPF alterado para {usuario.cpf}')

                    except:
                        limpar()
                        print('Escolha Inválida')
                        return()
            if encontrado == False:
                limpar()
                print('CPF não encontrado:')
        except:
            print('Parâmetros inválidos')

class Usuario:
    def __init__(self, nome, idade, endereco, cpf):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf

funcionarios_toyota = BancoDeDados()

def main():
    while True:
        try:
            escolha_menu = int(input('digite uma opção:\n1. Cadastrar um novo usuários\n2. Alterar dados\n3. Mostrar usuários cadastrados\n4. Sair\n>>>'))
            if escolha_menu == 1:
                nome = input('Digite o nome do usuário\n>>>')
                idade = int(input('Digite a idade do usuário\n>>>'))
                endereco = input('Digite o endereço\n>>>')
                cpf = input('Digite o CPF do usuário\n>>>')
                novo_usuario = Usuario(nome, idade, endereco, cpf)
                funcionarios_toyota.adicionar_usuario(novo_usuario)
                limpar()
                funcionarios_toyota.mostrar_usuarios()
            elif escolha_menu == 2:
                funcionarios_toyota.alterar_usuario()
            elif escolha_menu == 3:
                funcionarios_toyota.mostrar_usuarios()
            elif escolha_menu == 4:
                break    

        except:
            print('Escolha inválida')
        pass
    

if __name__ == '__main__':
    main()

