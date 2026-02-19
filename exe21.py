

# --- Aplicativo de Média de Notas ---

print("Bem-vindo à Calculadora de Média de Notas!")

# 1. Criamos uma lista de notas. Estes poderiam ser os resultados de um aluno.
notas = [8.5, 9.0, 7.5, 10.0, 6.0]

print(f"\nAs notas do aluno são: {notas}")

# 2. Usamos a função sum() para somar todos os valores dentro da lista 'notas'.
soma_das_notas = sum(notas)

# 3. Usamos a função len() para contar quantos itens (notas) existem na lista.
quantidade_de_notas = len(notas)

# 4. Calculamos a média dividindo a soma pela quantidade.
media = soma_das_notas / quantidade_de_notas

print(f"\nSoma de todas as notas: {soma_das_notas}")
print(f"Quantidade de notas: {quantidade_de_notas}")

# Usamos :.2f para formatar o número e mostrar apenas 2 casas decimais.
print(f"\nA média final do aluno é: {media:.2f}")


#   
#Como armazenar números (do tipo float) em uma lista.

#Como usar a função sum() para obter a soma total dos elementos de uma lista.

#Como usar a função len() para descobrir o "tamanho" ou a quantidade de itens em uma lista.

#Como usar os valores obtidos da lista para realizar cálculos matemáticos.