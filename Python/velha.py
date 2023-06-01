import pygame

# Gobals
pygame.font.init()
branco = " "
token = ["X", "O"]
nome = [" "," "]
score = {
    "Empate" : 0,
    "X" : 1,
    "O" : -1
}

# Função para definir se joga contra maquina ou contra outro jogador
def escolhe_nome():
    jogadores = int(input("Digite 1 para jogar conta a maquina ou 2 para jogar contra outra pessoa: "))
    if(jogadores == 2):
        jogador_01 = input("Digite o nome do primeiro jogador: ")
        jogador_02 = input("Digite o nome do segundo jogador: ")
    else:
        jogador_01 = input("Digite o nome do primeiro jogador: ")
        jogador_02 = "Bot"

    return [jogador_01,jogador_02]

# Função que cria a matriz do jogo
def criarBoard():
    board = [
        [branco,branco,branco],
        [branco,branco,branco],
        [branco,branco,branco],
        [branco,branco,branco]
    ]
    return board

# Função que exibe a matriz
def printBoard(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("----------")

# Função para validar a jogada
def getInputValido(mensagem):
    try:
        n = int(input(mensagem))
        if(n >= 1 and n <= 3):
            return n -1
        else:
            return print("O numero deve estar entre 1 e 3.")
    except:
        print("Numero nao valido")
        return getInputValido(mensagem)

# Função para verificar se a posição esta dispinivel
def verificaMovimento(board, linha, coluna):
    if (board[linha][coluna] == branco):
        return True
    else:
        return False

# Função que preenche o espaço
def fazMovimento(board, linha, coluna, jogador):
    board[linha][coluna] = token[jogador]

# Função que verifica uma condição de fim de jogo
def verificaGanhador(board):
    #Linha
    for i in range(3):
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != branco):
            return board[i][0]
        
    #Coluna
    for i in range(3):
        if(board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != branco):
            return board[0][i]
        
    #Diagonal_01
    if(board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != branco):
        return board[0][0]
    
    #Diagonal_02
    if(board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != branco):
        return board[0][2]
    
    #Verifica se continua
    for i in range(3):
        for j in range(3):
            if board[i][j] == branco:
                return False
    #Empate
    return "Empate"

# Função que reliza o movimento do bot
def moviment_IA(board, jogador):
    possibilidade = getPosicoes(board)
    melhor_valor = None
    melhor_movimento = None
    for possibilidade in possibilidade:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = branco

        if(melhor_valor is None):
            melhor_valor = valor
            melhor_movimento = possibilidade
        elif (jogador == 0):
            if(valor > melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade
        elif (jogador == 1):
            if(valor < melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade

    return melhor_movimento[0], melhor_movimento[1]

# Função para verificar possiveis jogadas
def getPosicoes(board):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] == branco):
                posicoes.append([i,j])

    return posicoes

# Função para definir melhor movimento
def minimax(board, jogador):
    ganhador = verificaGanhador(board)
    if(ganhador):
        return score[ganhador]
    jogador = (jogador +1)%2

    possibilidade = getPosicoes(board)
    melhor_valor = None
    for possibilidade in possibilidade:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = branco

        if(melhor_valor is None):
            melhor_valor = valor
        elif (jogador == 0):
            if(valor > melhor_valor):
                melhor_valor = valor
        elif (jogador == 1):
            if(valor < melhor_valor):
                melhor_valor = valor

    return melhor_valor

# Definições da tela de jogo
def draw_board(board, jogador):
    height = 600
    width = 600
    tamanho = 600/3
    win = pygame.display.set_mode(size=(600, 600))    
    win.fill(color= (255, 255, 255))

    for i in range(1, 3):
        pygame.draw.line(win, (0, 0, 0), (0, i* tamanho), (width, i* tamanho), 3)
        pygame.draw.line(win, (0, 0, 0), (i* tamanho, 0), (i* tamanho, height), 3)

    for i in range(3):
        for j in range(3):
            font = pygame.font.SysFont("comicsans", 100)

            x = j* tamanho
            y = i* tamanho

            text = font.render(board[i][j], 1, (128, 128, 128))
            win.blit(text, ((x+ 75),(y+ 75)))

def main():
    pygame.display.set_caption("Jogo da Velha")

    board = criarBoard()

    draw_board(board, 0)
    pygame.display.update()
 
    ganhador = verificaGanhador(board)
    nome = escolhe_nome()
    jogador = 0
        
    while(not ganhador):
        printBoard(board)
        jogou = False
        if(jogador == 1 and nome[1] == "Bot"):
            linha, coluna = moviment_IA(board, jogador)
        else:
            while(not jogou):
                for evento in pygame.event.get():
                    if(evento.type == pygame.QUIT):
                        return
                    elif(evento.type == pygame.MOUSEBUTTONUP):
                        pos = pygame. mouse.get_pos()
                        linha = int(pos[1]/200)
                        coluna = int(pos[0]/200)
                        jogou = True
                        
        if(verificaMovimento(board, linha, coluna)):
            fazMovimento(board, linha, coluna, jogador)
            jogador = (jogador +1)%2
        else:
            print("A posição ja foi escolhida!")

        ganhador = verificaGanhador(board)

        draw_board(board, jogador)
        pygame.display.update()
        
    if(ganhador == "Empate"):
        mensagem = "Empate"
    else:
        mensagem = (f"O jogador {nome[jogador -1]} venceu!")
    print("######################")
    printBoard(board)
    print(mensagem)
    print("######################")    

    while(True):
        for evento in pygame.event.get():
            if(evento.type == pygame.QUIT):
                return    

main()
