tarefas = []

tarefa1 = input("Escolha a primeira tarefa\n>>>")
tarefa2 = input("Escolha a segunda tarefa\n>>>")
tarefa3 = input("Escolha a terceira tarefa\n>>>")

tarefas.append(tarefa1)
tarefas.append(tarefa2)
tarefas.append(tarefa3)

tarefas.pop(0)

print(tarefas)