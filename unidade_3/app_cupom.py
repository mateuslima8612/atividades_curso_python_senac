idade = int(input('digite a idade\n>>>'))
clube = int(input('participa do clube? digite 1 para sim e 2 para não\n>>>'))

if idade > 60 and clube == 1:
    print('desconto vip')

elif idade > 60 or clube == 1:
    print('desconto básico')

else:
    print('usuario não tem desconto')
