# Inicia um laço infinito que só será interrompido quando o usuário decidir sair
while True:
    # Pergunta o nome do usuário
    nome = input("Olá! Por favor, digite seu nome: ")

    # Pede ao usuário para digitar um número, usando o nome dele na mensagem
    try:
        numero_str = input(f"\nOk, {nome}, digite o número para a tabuada que você deseja: ")
        # Se o usuário não digitar nada, oferece uma saída
        if numero_str == "":
            print("Nenhum número foi digitado. Saindo do programa.")
            break
        
        numero = int(numero_str)

        print(f"\n--- Tabuada do {numero} para {nome} ---")

        # O laço 'for' vai repetir o bloco de código 10 vezes (para i de 1 a 10)
        for i in range(1, 11):
            # Calcula o resultado da multiplicação
            resultado = numero * i
            # Imprime a linha da tabuada
            print(f"{numero} x {i} = {resultado}")

    except ValueError:
        print("\nErro: Você precisa digitar um número inteiro válido.")
    
    # Pergunta ao usuário se deseja continuar ou sair
    print("-" * 20) # Linha para separar visualmente
    continuar = input(f"\n{nome}, você quer ver outra tabuada? (digite 's' para sim ou qualquer outra tecla para sair): ")

    # Verifica a resposta. Se não for 's' (ou 'S'), o laço é interrompido.
    if continuar.lower() != 's':
        print(f"\nObrigado por usar a tabuada, {nome}. Até a próxima!")
        break # Encerra o programa
