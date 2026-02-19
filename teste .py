print("#######progrma de tarefas######")
print()
# --- Aplicativo de Lista de Tarefas ---

# 1. Criamos uma lista vazia para armazenar nossas tarefas.
dados = input("Quer criar sua lista de tarefas? Sim ou Não(s/n):")
if dados =="s":
    tarefas = []
    print()
    print()
    print("==============Bem-vindo ao seu Gerenciador de Tarefas!==============")
    tarefas.append(input("Digite a primeira tarefa:"))
    if input("Quer adicionar mais uma tarefa? (s/n):")=="s":
        tarefas.append(input("Digite a segunda tarefa:"))
        if input("Quer adicionar mais uma tarefa? (s/n):")=="s":
            tarefas.append(input("Digite a terceira tarefa:"))
            if input("Quer adicionar mais uma tarefa? (s/n):")=="s":
                tarefas.append(input("Digite a quarta tarefa:"))
                if input("Quer adicionar mais uma tarefa? (s/n):")=="s":
                    tarefas.append(input("Digite a quinta tarefa:"))
                    
else:
    print("Ok, até mais!")
print(tarefas)