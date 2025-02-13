import random

while True:
    # O jogador escolhe uma opção 
    jogador = input("Escolha uma opção: 0 (Pedra), 1 (Papel), 2 (Tesoura)= ")

    if jogador not in ['0', '1', '2']:  # Verifica se a opção escolhida pelo usuário é válida e caso seja inválida pede para o usuário tentar novamente
        print("Opção inválida!")
        continue

    jogador = int(jogador) # Transforma a entrada em um número inteiro e o computador escolhe uma das três opções
    computador = random.randint(0, 2) 

    # Exibe as opções escolhidas pelo usuário e o computador
    escolhas = ["Pedra", "Papel", "Tesoura"]
    print(f"Você escolheu: {escolhas[jogador]}")
    print(f"Computador escolheu: {escolhas[computador]}")

    # Verifica o vencedor da rodada
    if jogador == computador:
        print("Empate!")
    elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
        print("Você venceu!")
    else:
        print("Computador venceu!")

    # Pergunta ao jogador se quer jogar novamente e caso a escolha seja "sim" o jogo continua, caso a escolha seja "não" o jogo é encerrado
    jogar_novamente = input("Gostaria de jogar novamente? (Sim/Não): ").strip().lower()
    if jogar_novamente != "sim":
        print("Jogo encerrado.")
        break
