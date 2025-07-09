import random

numero = random.randint(0, 10)
escolha = int(input('tente adivinhar o número\ndigite um número: >>>'))
if escolha == numero:
    print(f'Parabéns!\nvocê escolheu {escolha}, o numero aleatorio era {numero}')
else:
    print(f'Você errou\nvocê escolheu {escolha}, o numero aleatorio era {numero}')