
def main():
    META_VENDAS = 100
    MAX_FALTAS = 0

    class Bonus:
        def __init__(self, faltas, vendas):
            self.faltas = faltas
            self.vendas = vendas
        
        def __str__(self):
            if ((self.faltas == MAX_FALTAS) and (self.vendas >= META_VENDAS)):
                return('\n\nO funcionário tem direito ao bonus!')
            else:
                return('\n\nO funcionário não tem direito ao bonus.')


    numeroFaltas = int(input('digite o número de faltas do funcionário:\n>>>'))
    numeroVendas = int(input('digite o número de vendas do funcionário:\n>>>'))

    bonusFuncionario = Bonus(numeroFaltas, numeroVendas)

    print(bonusFuncionario)

if __name__ == '__main__':
    main()