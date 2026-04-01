# Exibe o tabuleiro
def mostra_tabuleiro(tabuleiro):
    print("-------------")
    for linha in tabuleiro:
        print("|", linha[0], "|", linha[1], "|", linha[2], "|")
        print("-------------")

# Verifica se algum jogador venceu, conferindo as linhas, colunas e diagonais
def verifica_vitoria(tabuleiro, jogador):
    # Verifica as linhas
    for i in range(0, 3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
    # Verifica as colunas
    for i in range(0, 3):
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True
    # Verifica a diagonal principal
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    # Verifica a segunda diagonal
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False

# Verifica se o tabuleiro está cheio, se estiver cheio e não houve vitoria, 
# o jogo resultou em empate
def tabuleiro_cheio(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:        # " " significa vazio, não está cheio
            return False

    return True

# Algoritmo Minimax com poda Alfa-Beta

def minimax(tabuleiro, profundidade, e_maximizando, alfa, beta, simbolo_ia, simbolo_humano):
    # IA vence  = +10 score
    if verifica_vitoria(tabuleiro, simbolo_ia):
        return 10 - profundidade
    # Humano vence  = -10 score
    if verifica_vitoria(tabuleiro, simbolo_humano):
        return profundidade - 10
    # Empate = 0
    if tabuleiro_cheio(tabuleiro):
        return 0

    if e_maximizando:
        # Turno da IA - busca alcançar o maior "score" possivel
        melhor_score = -float('inf')

        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == " ":          # testa posições vazias
                    tabuleiro[i][j] = simbolo_ia    # Simula a jogada
                    score = minimax(tabuleiro, profundidade + 1, False, alfa, beta, simbolo_ia, simbolo_humano)
                    tabuleiro[i][j] = " "           # Desfaz a jogada
                    melhor_score = max(score, melhor_score)
                    alfa = max(alfa, melhor_score)
                    # Poda Alfa: ignoramos o caminho pois o humano nunca deixaria chegar até aqui
                    if beta <= alfa:
                        break
            
            if beta <= alfa:
                break

        return melhor_score

    else:
        # Turno do Humano - busca alcançar o menor "score" possivel (pior para a IA)
        melhor_score = float('inf')

        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == " ":
                    tabuleiro[i][j] = simbolo_humano        # Simula a jogada
                    score = minimax(tabuleiro, profundidade + 1, True, alfa, beta, simbolo_ia, simbolo_humano)
                    tabuleiro[i][j] = " "                   # Desfaz a jogada
                    melhor_score = min(score, melhor_score)
                    beta = min(beta, melhor_score)
                    # Poda Beta: ignoramos o caminho pois a IA nunca escolheria
                    if beta <= alfa:
                        break

            if beta <= alfa:
                break

        return melhor_score
# Testa todas as posições vazias e retorna a coordenada (i, j) com melhor score
def melhor_jogada(tabuleiro, simbolo_ia, simbolo_humano):
    melhor_score = -float('inf')
    jogada = None

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ": 
                tabuleiro[i][j] = simbolo_ia    # Testa a jogada
                score = minimax(tabuleiro, 0, False, -float('inf'), float('inf'), simbolo_ia, simbolo_humano)
                # Chama o minimax considerando que agora é turno do humano (false)
                tabuleiro[i][j] = " "           # Desfaz a jogada

                if score > melhor_score:        # Melhor posição encontrada
                    melhor_score = score
                    jogada = (i, j)             # Guarda a posição

    return jogada

# Inicializa o tabuleiro 3x3 vazio
def start_jogo():
    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    print("Bem-vindo ao Jogo da Velha!")
    print("Lembre-se: X sempre começa o jogo.\n")

    # Loop para o jogador escolher X ou O
    while True:
        escolha = input("Você quer jogar com X ou O?\n>>> ").strip().upper()

        if escolha in ["X", "O"]:
            break

        print("Opção inválida. Digite X ou O.")

    humano = escolha

    ia = "O" if humano == "X" else "X"      # Simbolo restante é o da IA

    print(f"\nVocê jogará com '{humano}' e a IA jogará com '{ia}'.")

    turno_humano = (humano == "X")      # Define quem começa

    print("Escolha posições de 1 a 3 para linha e coluna.\n")

    mostra_tabuleiro(tabuleiro)

    while True:
        if turno_humano:
            while True:            # Loop até uma jogada valida ser efetuada
                try:
                    linha  = int(input("Escolha uma linha (1 - 3): ")) - 1
                    coluna = int(input("Escolha uma coluna (1 - 3): ")) - 1

                except ValueError:
                    print("Entrada inválida. Digite apenas números inteiros.")
                    continue

                if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                    print("Posição inválida. Escolha valores entre 1 e 3.")
                    continue

                if tabuleiro[linha][coluna] != " ":
                    print("Posição ocupada. Escolha outra opção.")
                    continue

                break

            tabuleiro[linha][coluna] = humano
            mostra_tabuleiro(tabuleiro)

            if verifica_vitoria(tabuleiro, humano):
                print("Parabéns! Você venceu!!!")
                return

            if tabuleiro_cheio(tabuleiro):
                print("O jogo terminou empatado.")
                return

            turno_humano = False     # Passa o turno para a IA

        else:
            print("\nA IA está pensando...")
            jogada_ia = melhor_jogada(tabuleiro, ia, humano)        # IA calcula a melhor jogada
            tabuleiro[jogada_ia[0]][jogada_ia[1]] = ia
            print(f"A IA jogou na linha {jogada_ia[0] + 1}, coluna {jogada_ia[1] + 1}.\n")
            mostra_tabuleiro(tabuleiro)

            if verifica_vitoria(tabuleiro, ia):
                print("A IA venceu! Tente novamente.")
                return

            if tabuleiro_cheio(tabuleiro):
                print("O jogo terminou empatado.")
                return

            turno_humano = True      # Passa o turno para o humano

# Loop do ponto de partida do jogo
while True:
    start_jogo()
    jogar_novamente = input("\nDeseja jogar novamente? (S/N): ").strip().upper()
    if jogar_novamente != "S":
        print("Obrigado por jogar!")
        break