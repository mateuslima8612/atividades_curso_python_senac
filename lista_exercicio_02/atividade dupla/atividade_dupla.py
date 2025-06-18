frase_secreta = []

nova_palavra = ['python']

frase_secreta.append('em')
frase_secreta.extend(nova_palavra)

frase_secreta.append('aprendi')

frase_secreta.insert(0, 'abacaxi')

frase_secreta.insert(0, 'eu')

print(frase_secreta)

frase_secreta.pop(1)
frase_secreta.pop(-1)
frase_secreta.insert(1, 'aprendi')
frase_secreta.insert(2, 'listas')
print(frase_secreta)

frase_secreta.clear()
print(frase_secreta)
