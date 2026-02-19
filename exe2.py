# --- Início do Programa ---
print("--- Calculadora de Índice de Massa Corporal (IMC) ---\n")
print("\n Por favor, forneça seu peso e altura.")


    # Solicita o peso do usuário e converte para float (número com decimal)
peso_usuario = float(input("Digite seu peso em quilogramas (ex: 70.5): "))

    # Solicita a altura do usuário e converte para float
altura_usuario = float(input("Digite sua altura em metros (ex: 1.75): "))
 # Calcula o IMC: peso / (altura * altura)
imc = peso_usuario / (altura_usuario ** 2)  # altura ** 2 é o mesmo que altura * altura
print(f"Seu IMC é: {imc:.2f}")  # :.2f formata para 2 casas decimais
