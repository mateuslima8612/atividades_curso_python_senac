
def main():
    saldo = 0
    while True:
        print("\n\n=====Caixa Eletrônico Simples=====\n\nAtualmente só temos notas de R$ 50,00\n1. Consultar saldo\n2. Depositar valor\n3. Sacar valor\n4. Sair\nDigite uma opção de 1 a 4.")
        try:            
            escolha = int(input('\n>>>'))
        except:
            print("Você deve digitar um número de 1 a 4.")
        try:
            if escolha == 1:
                print(f'\n\n>>>O saldo do usuário é {saldo}')
            elif escolha == 2:
                try:
                    deposito = int(input('Quanto deseja depositar?\n\n>>>'))
                    saldo = (deposito + saldo)
                    print(f'Depósito efetuado com sucesso. Seu novo saldo é {saldo}')
                except:
                    print('O valor a ser depositado deve ser um número.')
            elif escolha == 3:
                if saldo <= 0:
                    print(f'O saldo do usuário é {saldo}. Não é possível realizar saques.')
                else:
                    try:
                        saque = int(input(f'Seu saldo disponível é {saldo}. Quanto deseja sacar?\n\n>>>'))
                        if saque > saldo:
                            print('O valor do saque não pode ser maior que o saldo disponível.')
                        else:
                            if ((saque % 50) != 0):
                                print('Só temos notas de R$50,00!') 
                            else:
                                saldo = (saldo - saque)
                                print(f'Saque efetuado com sucesso. Seu novo saldo é {saldo}.\n\n')
                    except:
                        print('O valor a ser sacado deve ser um número.')
            elif escolha == 4: 
                break
        except UnboundLocalError:
            'Digite um valor válido.'

if __name__ == "__main__":

    main()