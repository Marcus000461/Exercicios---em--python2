# Inicializa as variáveis
soma_notas = 0
contador = 1

# Loop para pedir as 4 notas
while contador <= 4:
  nota = float(input(f"Digite a {contador}ª nota: "))
  soma_notas += nota
  contador += 1
  

# Calcula a média
media = soma_notas / 4

# Exibe o resultado

print(f"\nA soma das notas é: {soma_notas} e média das notas é: {media}")

