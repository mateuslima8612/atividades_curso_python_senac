import calculadora

while True:
    try:
        escolha = int(input('escolha a opcao da operacao desejada: \n1. soma\n2. subtracao\n3. multiplicacao\n4. divisao\n5. raiz quadrada\n6. potenciacao\n7. converter para fahrenheit\nQualquer outro número para sair\n>>>'))
        break
    except:
        print('A escolha deve ser um número')
        continue

if escolha == 1:
    num1 = input('Digite o primeiro número da soma:\n>>>')
    num2 = input('Digite o segundo número da soma:\n>>>')
    calculadora.soma(int(num1), int(num2))
if escolha == 2:
    num1 = input('Digite o primeiro número da subtracao:\n>>>')
    num2 = input('Digite o segundo número da subtracao:\n>>>')
    calculadora.subtracao(int(num1), int(num2))
if escolha == 3:
    num1 = input('Digite o primeiro número da multiplicacao:\n>>>')
    num2 = input('Digite o segundo número da multiplicacao:\n>>>')
    calculadora.multiplicacao(int(num1), int(num2))
if escolha == 4:
    num1 = input('Digite o primeiro número da divisao:\n>>>')
    num2 = input('Digite o segundo número da divisao:\n>>>')
    calculadora.divisao(int(num1), int(num2))
if escolha == 5:
    num1 = input('Digite o número que deseja encontrar a raiz quadrada\n>>>')
    calculadora.raiz(int(num1))

if escolha == 6:
    num1 = input('Qual é o número da operacao?\n>>>')
    num2 = input('Elevado a que potencia?')
    calculadora.potenciacao(int(num1), int(num2))

if escolha == 7:
    num1 = input('Que numero deseja converter para fahrenheit?\n>>>')
    calculadora.conversao_fahrenheit(int(num1))