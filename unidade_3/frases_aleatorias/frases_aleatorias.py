import random

pessoas = ["Magaly", "Neymar", "Elvis Presley", "Beyonce", "Jarbas, meu pai?", "Não, o Jô Soares"]
locais = ["Senac", "Estácio", "Casa da Mãe Joana", "Igreja", "Planalto Central", "Terreiro", "Monastério"]
recipiente = ["Um saco", "Um buraco no chão", "tapaué", "bolso", "canteiro de obras"]
objetos = ["Caneta", "Celular", "Estetoscópio", "Feijoada", "Privada", "Um quadro do Michael Jackson", "Tamagochi"]

pessoa_escolhida = random.choice(pessoas)
local_escolhido = random.choice(locais)
recipiente_escolhido = random.choice(recipiente)
objeto_escolhido = random.choice(objetos)

frase = f'Era uma vez {pessoa_escolhida} que estava em {local_escolhido} olhando para {objeto_escolhido} dentro de {recipiente_escolhido}'

print(frase)