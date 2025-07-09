import random

inicios = ['Era uma vez', 'Numa terra distante', 'Numa galáxia distante']
sujeitos = ['Roberto', 'Robocop', 'Romário', 'Neymar', 'Nicole']
objetos = ['bola de futebol', 'panela de polenta', 'masserati', 'garfo', 'palito de dente', 'bugatti']
locais = ['SENAC', 'maracana', 'projac', 'polo sul', 'maldivas', 'logo ali em olaria']
encerramentos = ['e viveu feliz pra sempre', 'e não viveu tão feliz assim', 'continua...']

inicio = random.choice(inicios)
sujeito = random.choice(sujeitos)
objeto = random.choice(objetos)
local = random.choice(locais)
encerramento = random.choice(encerramentos)

print(f'{inicio} {sujeito}, que encontrou {objeto} em {local}, {encerramento}')