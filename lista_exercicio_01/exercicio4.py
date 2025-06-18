

def main():
    while True:
        try:
            a = int(input('Digite o valor do primeiro lado do triângulo:\n>>> '))
            b = int(input('Digite o valor do segundo lado do triângulo:\n>>> '))
            c = int(input('Digite o valor do terceiro lado do triângulo:\n>>> '))

            if (a + b > c and b + c > a and c + a > b):
                print('é possível formar um triângulo\n\n')
                break
            else:
                print('não é possível formar um triângulo\n\n')
                break
        except:
            print('\n\nOs valores devem ser números\n\n')

if __name__ == '__name__':
    main()


