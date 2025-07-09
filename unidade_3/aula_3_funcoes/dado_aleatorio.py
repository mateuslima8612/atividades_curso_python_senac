import random

def lancar_dados(faces):
    return random.randint(1, faces)

nr_faces = int(input('quantas faces tem o dado\n>>>'))

print(f'O resultado foi... {lancar_dados(nr_faces)}')