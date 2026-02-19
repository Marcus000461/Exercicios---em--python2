import random
import time

def jogar_novamente():
    """Função que encapsula a lógica principal do jogo."""
    
    # O computador "pensa" em um número de 1 a 10
    numero_secreto = random.randint(1, 10)
    tentativas = 3
    acertou = False

    print("\n---------------------------------")
    print("Ótimo! Pensei em um número entre 1 e 10.")
    print(f"Você tem {tentativas} chances para adivinhar qual é.")
    print("---------------------------------")
    
    # Loop para as tentativas do jogador
    while tentativas > 0:
        try:
            # Pede ao usuário para adivinhar
            palpite = int(input(f"Tentativa {4 - tentativas}/3 - Qual seu palpite? "))

            # Verifica se o palpite está no intervalo válido
            if palpite < 1 or palpite > 10:
                print("Opa! O número deve ser entre 1 e 10. Tente de novo.")
                continue # Pula para a próxima iteração do loop

        except ValueError:
            # Caso o usuário não digite um número
            print("Isso não parece ser um número. Por favor, digite um número de 1 a 10.")
            continue

        # Compara o palpite com o número secreto
        if palpite == numero_secreto:
            print(f"\nSENSACIONAL, {nome}! Você acertou!")
            acertou = True
            break # Encerra o loop de tentativas pois o jogador acertou
        else:
            tentativas -= 1 # Decrementa o número de tentativas
            print("Você errou!")
            if tentativas > 0:
                print(f"Você ainda tem {tentativas} chance(s).")
            
    # Se o loop terminar e o jogador não tiver acertado
    if not acertou:
        print("\nQue pena, suas chances acabaram.")
        print(f"O número que eu pensei era o {numero_secreto}.")

# --- Início do Programa Principal ---

print("Bem-vindo ao Jogo de Adivinhar o Número!")
nome = input("Para começar, qual é o seu nome? ")

while True:
    resposta = input(f"\nE aí, {nome}, quer jogar? (sim/não): ").lower()

    if resposta == 'sim':
        jogar_novamente()
    elif resposta == 'não' or resposta == 'sair':
        print(f"\nTudo bem, {nome}. Tchauu!")
        break
    else:
        print("Opção inválida. Por favor, responda com 'sim' ou 'não'.")