itens_catalogo_infantil = ['carro', 'caminhão', 'barco']
itens_catalogo = ['BMW', 'Toyota', 'Honda', 'Hyundai']
print('Seja bem-vindo(a) à concessionária!')
while True:
    try:
        idade = int(input('Para oferecermos o produto adequado, comece digitando a sua idade.\n\n>>>'))
        break
    except:
        print('Você deve digitar um número!')


def catalogo_infantil():
    print('catalogo infantil\n')
    for i in itens_catalogo_infantil:
        print(f'{i}')

def catalogo():
    print('catalogo normal\n')
    for i in itens_catalogo:
        print(f'{i}')

if idade < 18:
    catalogo_infantil()
else:
    catalogo()

'''nome = input()

x = f'meu nome é {nome}'

print(x)'''