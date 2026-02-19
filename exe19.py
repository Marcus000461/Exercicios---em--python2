# --- Aplicativo de Lista de Tarefas ---

# 1. Criamos uma lista vazia para armazenar nossas tarefas.
tarefas = []

print("Bem-vindo ao seu Gerenciador de Tarefas!")

# Adicionando algumas tarefas iniciais com o método append()
tarefas.append("Estudar Python")
tarefas.append("Fazer o dever de casa")
tarefas.append("Lavar a louça")

print("\nSuas tarefas de hoje são:")
# 2. Usamos um loop 'for' para mostrar cada item da lista.
# A função enumerate() nos dá o índice (a posição) e o valor de cada item.
for i, tarefa in enumerate(tarefas):
    print(f"{i + 1}. {tarefa}")

# Removendo uma tarefa da lista
print("\nVocê completou 'Fazer o dever de casa'. Removendo da lista...")

# 3. Para remover um item, precisamos saber sua posição (índice).
# 'Fazer o dever de casa' está na posição 1 (listas começam a contar do 0).
# Usamos 'del' para deletar o item nessa posição.
del tarefas[1]

print("\nSua lista de tarefas atualizada é:")
for i, tarefa in enumerate(tarefas):
    print(f"{i + 1}. {tarefa}")
    
    
   # Como criar uma lista vazia: tarefas = [].

#Como adicionar itens ao final da lista com .append().

#Como acessar e exibir itens de uma lista usando um loop for.

#Como remover um item da lista usando del e seu índice (posição).

