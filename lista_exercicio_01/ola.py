import exercicio1, exercicio2, exercicio3, exercicio4, exercicio5, sair


def main():
    exercicios = ['', exercicio1, exercicio2, exercicio3, exercicio4, exercicio5, sair]
    escolha = int(input('escolha qual exercício deseja executar:\n1. Verificador de idade e autorização\n2. Verificador de media do aluno\n3. Tela de Login\n4. Verificador de triângulo\n5. Verificador de bônus\n6. Sair\n\n>>> '))
    try:
        exercicios[escolha].main()
        print('\n\n\n\n\n\n\n')
    except AttributeError:
        print('valor inválido\n')

while True:
    if __name__ == '__main__':
        main()
        