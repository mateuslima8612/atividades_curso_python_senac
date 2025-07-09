perfil_usuario = {
    'nome': 'Mateus',
    'idade': 20,
    'cidade': 'Nova Friburgo'
    }

perfil_usuario['cidade'] = input(f'Sua cidade é {perfil_usuario['cidade']}\ndigite a nova cidade\n>>>')
print(f'Perfil Atualizado\nNome: {perfil_usuario["nome"]}\nIdade: {perfil_usuario['idade']}\nCidade: {perfil_usuario["cidade"]}')