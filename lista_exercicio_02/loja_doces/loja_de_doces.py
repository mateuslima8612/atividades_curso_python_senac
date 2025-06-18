
lista_doces = [
    {'nome': 'Bala', 'valor': 0.50},
    {'nome': 'Chocolate', 'valor': 3.00},
    {'nome': 'Biscoito', 'valor': 3.50},
    {'nome': 'Pirulito', 'valor': 2.00}
]

carrinho = []
subtotal = []

def main():
    print('Boas vindas à Loja de Doces.')
    while True:
        escolha_menu = input('Escolha uma opção:\n1. Catálogo\n2. Sair\n>>> ')
        try:
            if (int(escolha_menu) == 1):
                print('Menu:')
                for i in range(len(lista_doces)):
                    print(f'{i + 1}. {lista_doces[i]['nome']} R${lista_doces[i]['valor']:.2f}')
                escolha_compra = int(input('Selecione a opção desejada para comprar | Digite 5 para sair\n>>> '))
                escolha_correcao = (escolha_compra - 1)
                if escolha_compra == 5:
                    break
                else:
                    quantidade = int(input(f'Você escolheu {lista_doces[escolha_correcao]['nome']}. Digite a quantidade que deseja comprar\n>>> '))
                    print(f'{lista_doces[escolha_correcao]['nome']} | {quantidade} X {lista_doces[escolha_correcao]['valor']} | Total: R${(quantidade * lista_doces[escolha_correcao]['valor'])}\n\nCarrinho:')
                    carrinho.append(lista_doces[escolha_correcao]['nome'])
                    subtotal.append((quantidade) * (lista_doces[escolha_correcao]['valor']))
                    for i in range(len(carrinho)):
                        print(f'{carrinho[i]} | {quantidade}x - R$ {subtotal[i]}')
                    finalizar = (int(input(f'Subtotal: R$ {sum(subtotal)}\nDeseja finalizar a compra?\n1. Sim\n2. Não\n>>> ')))
                    if (finalizar == 1):
                        print('Compra finalizada com sucesso!\n\n')
                        carrinho.clear()
                        subtotal.clear()
                    elif (finalizar == 2):
                        pass
                    else:
                        print('\n\nEscolha inválida!\n\n')
            elif (int(escolha_menu) == 2):
                break
            else:
                print('\n\nEscolha inválida!\n\n')
        except:
            print('\n\nEscolha inválida\n\n')

if __name__ == '__main__':
    main()