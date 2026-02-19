


        # Solicita ao usuário o número para a tabuada
numero = int(input("Digite o número para a tabuada: "))

        # Solicita ao usuário o início do intervalo
inicio = int(input("Digite o início do intervalo da tabuada: "))

        # Solicita ao usuário o fim do intervalo
fim = int(input("Digite o fim do intervalo da tabuada: "))

print(f"\nTabuada de {numero}, de {inicio} a {fim}:\n")

        # Garante que o intervalo seja percorrido corretamente, mesmo que o fim seja menor que o início
if fim < inicio:
            inicio, fim = fim, inicio

        # Itera sobre o intervalo fornecido e imprime a tabuada
for i in range(inicio, fim + 1):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")

