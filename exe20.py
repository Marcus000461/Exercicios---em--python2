# --- Aplicativo de Sorteio de Nomes ---

# 1. Primeiro, precisamos importar a biblioteca 'random', que sabe como gerar coisas aleatórias.
import random

print("Bem-vindo ao Sorteador de Nomes!")

# 2. Criamos nossa lista de participantes.
participantes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduarda", "Felipe"]

print("\nParticipantes do sorteio:")
# Mostramos todos os nomes que estão na lista.
for nome in participantes:
    print(f"- {nome}")

# 3. Usamos a função random.choice() para escolher um item aleatório da lista.
# Nós passamos nossa lista 'participantes' como argumento para a função.
ganhador = random.choice(participantes)

print("\nSorteando...")
print("E o(a) grande ganhador(a) é...")
print(f"🎉 {ganhador}! 🎉")

#Como criar uma lista já com itens definidos.

#Como usar uma lista em conjunto com outras bibliotecas do Python (neste caso, random).

#O conceito de que cada item em uma lista pode ser acessado individualmente.