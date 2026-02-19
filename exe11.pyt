numero = int(input("Digite o número da tabuada que você deseja: "))

print(f"\n--- Tabuada do {numero} ---")

    # O laço 'for' vai repetir o bloco de código 10 vezes (para i de 1 a 10)
for i in range(1, 11):
        # Calcula o resultado da multiplicação
        resultado = numero * i
        # Imprime a linha da tabuada
        print(f"{numero} x {i} = {resultado}")