inventario = []

def adicionar_item(nome, preco, quantidade):
    inventario.append({'nome': nome, 'preço': preco, "quantidade": quantidade})

def main():
    while True:
        escolha_menu = int(input('escolha uma opção:\n1. adicionar ao inventario\n>>>'))
        if escolha_menu == 1:
            nome = input('nome do produto: ')
            preco = input('preço do produto: ')
            quantidade = input('quantidade do produto')
            adicionar_item(nome, preco, quantidade)
            print(f'produto {nome} adicionado ao inventario')
            print('nome | preço | quantidade')
            for i in range(len(inventario)):
                print(f'{inventario[i]["nome"]} | {inventario[i]["preço"]} | {inventario[i]["quantidade"]}')

main()