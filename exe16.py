import random

# 1. Pergunta o nome da pessoa
nome = input("Olá! Qual é o seu nome? ")


# 2. Pergunta se quer jogar pela primeira vez
resposta = input(f"Olá {nome}, você quer jogar o jogo de adivinhação? (sim/não): ").lower()

# 3. O jogo continua enquanto a resposta for "sim"
while resposta == 'sim':
    
    # Configurações do jogo
    numero_secreto = random.randint(1, 10)
    tentativas = 3
    acertou = False # Variável para verificar se o jogador ganhou

    print("\n------------------------------------")
    print(f"Ok! Pensei em um número de 1 a 10. Você tem {tentativas} chances.")
    print("------------------------------------")

    # Loop para as 3 tentativas
    while tentativas > 0:
        # Pede o palpite e já converte para número
        palpite = int(input(f"Você tem {tentativas} chance(s). Qual seu palpite? "))

        # Verifica se acertou
        if palpite == numero_secreto:
            print(f"SENSACIONAL, {nome}! Você acertou!")
            acertou = True
            break # Se acertou, para o loop de tentativas na hora
        else:
            print("Você errou!")
            tentativas = tentativas - 1 # Diminui uma tentativa

    # 4. Se o loop de tentativas acabou e o jogador não acertou
    if not acertou:
        print(f"Que pena, suas chances acabaram. O número era {numero_secreto}.")

    # 5. Pergunta se quer jogar de novo e atualiza a resposta
    print("\n------------------------------------")
    resposta = input("Quer jogar de novo? (sim/não): ").lower()


# 6. Se a resposta não for mais "sim", o jogo acaba
print(f"\nTudo bem. Tchauu, {nome}!")
