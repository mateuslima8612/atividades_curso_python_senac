def cumprimentar(nome):
    return(f"olá {nome}, tenha uma boa noite")

nome1 = cumprimentar('mateus')
nome2 = cumprimentar('fulano')
nome3 = cumprimentar('ciclano')

print('testes')
print(nome1)
print(nome2)
print(nome3)
print('--------------------\n\n')

nome_usuario = input('digite o seu nome\n>>>')

print(cumprimentar(nome_usuario))

