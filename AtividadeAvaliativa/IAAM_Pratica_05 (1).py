# # Jogo da Velha - Humano vs Agente Inteligente (Minimax)

# ### Passo 1: Criar uma função que escreve na tela o tabuleiro

def mostra_tabuleiro(tabuleiro):

    print("-------------") # Marca uma divisão entre telas para controle visual

    for linha in tabuleiro:

        print("|", linha[0], "|", linha[1], "|", linha[2], "|")

        print("-------------") # Marca uma divisão entre telas para controle visual


# ### Passo 2: Criar as regras para que o jogo seja finalizado

def verifica_vitoria(tabuleiro, jogador):

    # Vamos verificar possibilidade de vitória por sequência horizontal
    for i in range(0,3):

        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:

            return True

    # Vamos verificar possibilidade de vitória por sequência vertical
    for i in range(0,3):

        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:

            return True

    # Vamos verificar possibilidade de vitória na diagonal
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:

        return True

    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:

        return True

    return False


# ### Passo 3: Verificar se o tabuleiro está cheio (empate)

def tabuleiro_cheio(tabuleiro):

    for linha in tabuleiro:

        if " " in linha:

            return False

    return True


# ### Passo 4: Algoritmo Minimax - Agente Inteligente

def minimax(tabuleiro, profundidade, e_maximizando):

    # Casos terminais: verificar se alguém venceu ou se empatou
    if verifica_vitoria(tabuleiro, "O"):  # IA venceu
        return 1

    if verifica_vitoria(tabuleiro, "X"):  # Humano venceu
        return -1

    if tabuleiro_cheio(tabuleiro):  # Empate
        return 0

    if e_maximizando:
        # Turno da IA (O) - busca maximizar o score
        melhor_score = -float('inf')

        for i in range(3):
            for j in range(3):

                if tabuleiro[i][j] == " ":

                    tabuleiro[i][j] = "O"  # Simula a jogada da IA
                    score = minimax(tabuleiro, profundidade + 1, False)
                    tabuleiro[i][j] = " "  # Desfaz a jogada

                    melhor_score = max(score, melhor_score)

        return melhor_score

    else:
        # Turno do Humano (X) - busca minimizar o score
        melhor_score = float('inf')

        for i in range(3):
            for j in range(3):

                if tabuleiro[i][j] == " ":

                    tabuleiro[i][j] = "X"  # Simula a jogada do humano
                    score = minimax(tabuleiro, profundidade + 1, True)
                    tabuleiro[i][j] = " "  # Desfaz a jogada

                    melhor_score = min(score, melhor_score)

        return melhor_score


# ### Passo 5: Função que encontra a melhor jogada para a IA

def melhor_jogada(tabuleiro):

    melhor_score = -float('inf')
    jogada = None

    for i in range(3):
        for j in range(3):

            if tabuleiro[i][j] == " ":

                tabuleiro[i][j] = "O"  # Simula a jogada
                score = minimax(tabuleiro, 0, False)
                tabuleiro[i][j] = " "  # Desfaz a jogada

                if score > melhor_score:
                    melhor_score = score
                    jogada = (i, j)

    return jogada


# ### Passo 6: Criar a função que inicializa o jogo (Humano vs IA)

def start_jogo():

    # Criação da lista que gera o tabuleiro
    tabuleiro = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]

    # Humano joga com "X", IA joga com "O"
    humano = "X"
    ia = "O"

    print("Bem-vindo ao Jogo da Velha!")
    print("Você é o jogador X e a IA é o jogador O.")
    print("Escolha posições de 1 a 3 para linha e coluna.\n")

    # Printa o tabuleiro na tela
    mostra_tabuleiro(tabuleiro)

    # Loop principal do jogo
    while True:

        # --- Turno do Humano (X) ---
        while True:

            linha = int(input("Escolha uma linha (1 - 3): ")) - 1
            coluna = int(input("Escolha uma coluna (1 - 3): ")) - 1

            # Verificando se a posição está dentro dos limites
            if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                print("Posição inválida. Escolha valores entre 1 e 3.")
                continue

            # Verificando se a posição escolhida é válida
            if tabuleiro[linha][coluna] != " ":
                print("Posição ocupada. Escolha outra opção.")
                continue

            break

        tabuleiro[linha][coluna] = humano
        mostra_tabuleiro(tabuleiro)

        # Verifica se o humano venceu
        if verifica_vitoria(tabuleiro, humano):
            print("Parabéns! Você venceu!!!")
            return

        # Verifica empate
        if tabuleiro_cheio(tabuleiro):
            print("O jogo terminou empatado.")
            return

        # --- Turno da IA (O) - Algoritmo Minimax ---
        print("\nA IA está pensando...")
        jogada_ia = melhor_jogada(tabuleiro)
        tabuleiro[jogada_ia[0]][jogada_ia[1]] = ia
        print(f"A IA jogou na linha {jogada_ia[0] + 1}, coluna {jogada_ia[1] + 1}.\n")
        mostra_tabuleiro(tabuleiro)

        # Verifica se a IA venceu
        if verifica_vitoria(tabuleiro, ia):
            print("A IA venceu! Tente novamente.")
            return

        # Verifica empate
        if tabuleiro_cheio(tabuleiro):
            print("O jogo terminou empatado.")
            return


start_jogo()
