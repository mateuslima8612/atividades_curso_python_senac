nota_1 = int(input('digite a primeira nota:\n>>>'))
nota_2 = int(input('digite a segunda nota:\n>>>'))
nota_3 = int(input('digite a terceira nota:\n>>>'))
nota_4 = int(input('digite a quarta nota:\n>>>'))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media >= 6:
    print(f'aluno aprovado, media {media}')
else:
    print(f'aluno reprovado, media {media}')
