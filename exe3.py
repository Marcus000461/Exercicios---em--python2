# --- Calculadora de Média Simples ---

print("--- Calculadora de Média de 4 Notas ---")
print("Por favor, insira as quatro notas abaixo.")
print("")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
# 2. Cálculo da Média
    # Somamos todas as notas e dividimos pela quantidade de notas (que é 4)
media = (nota1 + nota2 + nota3 + nota4) / 4
# 3. Saída do Resultado
    # Usamos uma f-string para formatar a saída de forma amigável.
    # :.1f formata o número para ter apenas uma casa decimal.
print(f"\n--- Resultado ---")
print(f"As notas digitadas foram: {nota1}, {nota2}, {nota3}, {nota4}")
print(f"A média das notas é: {media:.1f}")
