# *Jogo da Velha — Agente Inteligente com Minimax + Poda Alfa-Beta*
Trabalho prático da disciplina Inteligência Artificial e Aprendizado de Máquina — Eng de Software, 5 semestre

Implementação de um agente inteligente para o Jogo da Velha utilizando o algoritmo Minimax com Poda Alfa-Beta.
O agente avalia todas as jogadas possíveis e sempre toma a melhor decisão possível.

# Integrantes:
    Felipe Nonato Leoneli		  RA: 24021973 
    Guilherme Braz Lourenço	      RA: 24000000 
    Rafael Roveri Pires			  RA: 24007131
# Como rodar:
  **Pré-requisito: Python 3 instalado.**
  
  Clone o repositório:
    -> git clone https://github.com/Gu1br4/AtividadeAvIA.git
    -> Cd AtividadeAvIA
  
    - Execute o jogo
      python jogo_da_velha.py


Como o algoritmo funciona:
  O Minimax simula recursivamente todas as jogadas possíveis, alternando entre dois papéis:
  
    - Maximizador (IA): busca o maior score possível
    - Minimizador (Humano): assume que o adversário também joga de forma ótima
  
  Cada estado terminal recebe um score:
  
    +10 − profundidade → vitória da IA (prefere vencer mais rápido)
    profundidade − 10 → vitória do humano (prefere adiar a derrota)
    0 → empate
  
  A Poda Alfa-Beta otimiza a busca descartando ramos que não influenciam o resultado, reduzindo a complexidade de O(b^d) para O(b^(d/2)) no melhor caso.
