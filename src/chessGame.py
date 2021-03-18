import chess
import random
import os
import evaluation as ev
from colorama import init, Fore, Back, Style
from jogo import Jogo,Jogador
from minimax import melhor_jogada_agente_poda,melhor_jogada_agente

BACKGROUND = {
    (0, 0) : Back.LIGHTBLACK_EX,
    (1, 0) : Back.BLACK,
    (0, 1) : Back.BLACK,
    (1, 1) : Back.LIGHTBLACK_EX
}

ELEMENTS = {
    (chess.KING, 0): f'{Fore.CYAN} \u265A',
    (chess.QUEEN, 0): f'{Fore.CYAN} \u265B',
    (chess.ROOK, 0): f'{Fore.CYAN} \u265C',
    (chess.BISHOP, 0): f'{Fore.CYAN} \u265D',
    (chess.KNIGHT, 0): f'{Fore.CYAN} \u265E',
    (chess.PAWN, 0): f'{Fore.CYAN} \u265F',
    (chess.KING, 1): f'{Fore.WHITE} \u265A',
    (chess.QUEEN, 1): f'{Fore.WHITE} \u265B',
    (chess.ROOK, 1): f'{Fore.WHITE} \u265C',
    (chess.BISHOP, 1): f'{Fore.WHITE} \u265D',
    (chess.KNIGHT, 1): f'{Fore.WHITE} \u265E',
    (chess.PAWN, 1): f'{Fore.WHITE} \u265F'
}

def acharPeca(square):
    peca = jogo.board.piece_at(square)
    if peca != None:        
        return ELEMENTS[peca.piece_type, peca.color]
    else:
        return "  "

class ChessGame(Jogo):
    def __init__(self, board, playerColor, prim5jogadas = []):
        self.primeiras5Jogadas = prim5jogadas
        self.board = board
        self.playerColor = playerColor

    def turno(self):
        return self.board.turn

    def jogar(self, localizacao):
        aux = self.board.copy()
        aux.push(chess.Move.from_uci(localizacao))
        return ChessGame(chess.Board(aux.fen()), self.playerColor, self.primeiras5Jogadas)

    def jogos_validos(self):
        return list(self.board.legal_moves)

    def venceu(self):
        return self.board.is_checkmate()

    def empate(self):
        return self.board.is_stalemate() or self.board.is_insufficient_material() or self.board.is_fivefold_repetition() or self.board.is_seventyfive_moves()

    def avaliar(self):
        return ev.evaluate(self.board, not self.playerColor)
        #return ev.evaluate(self.board, not self.turno())

    def registrarAbertura(self, jogada):
        self.primeiras5Jogadas.append(jogada)

    def tipoEmpate(self):
        if(self.board.is_stalemate()):
            return "Stalemate - Afogamento"
        if(self.board.is_insufficient_material()):
            return "Insufficient Material - Material Insuficiente"
        if(self.board.is_fivefold_repetition()):
            return "Fivefold Repetition - 5 jogadas idênticas"
        if(self.board.is_seventyfive_moves()):
            return "Seventy Five moves - Muitas jogadas sem captura ou movimento de peão"
        return "Empate"

def sortPerPiece(legalMoves):
    pieces = []
    for _ in range(7):
        pieces.append([])

    for move in legalMoves:
        square = chess.parse_square(move[:2])
        p = jogo.board.piece_at(square)
        pieces[p.piece_type].append(move)

    for piece in range(1, 7):
        print(f"{ev.pieceName[piece]} = {pieces[piece]}")


def mostraTabuleiroBonitinho():
    colunas = ["a", "b",  "c",  "d",  "e",  "f",  "g",  "h"]

    print("""   a  b  c  d  e  f  g  h """)
    for linha in range(8,0,-1):
        print(f"{linha} ", end='', flush=True)
        for coluna in colunas:
            square = chess.parse_square(coluna + linha.__str__())
            print(f"{BACKGROUND[square % 2, linha % 2]}{acharPeca(square)}", Style.RESET_ALL, end='', flush=True)
        print()

def lerJogada(legalMovesList):
    while True:
        legalMoves = []
        for move in legalMovesList:
            legalMoves.append(move.uci())
        #print(legalMoves)
        sortPerPiece(legalMoves)
        mov = input("\nDigite uma jogada: ")
        if mov in legalMoves:
            return mov

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#JOGO NORMAL
if __name__ == "__main__":
    player = int(input("0 pra preto, 1 pra branco: "))
    jogo = ChessGame(chess.Board(),player)
    computador = ""

    while not jogo.board.is_game_over():
        if jogo.board.turn == player:

            mostraTabuleiroBonitinho()

            if computador != "":                
                print(f"\nJogada do Computador é {computador}\n") 

            humano = lerJogada(list(jogo.board.legal_moves))            
            jogo = jogo.jogar(humano)

            cls()
            mostraTabuleiroBonitinho()

            if (len(jogo.primeiras5Jogadas) < 5):
                jogo.registrarAbertura(humano)

            if jogo.venceu():
                cls()
                print("Humano Venceu!")
                break
            elif jogo.empate():
                cls()
                print("Empate!")
                print(jogo.tipoEmpate())
                break
        else:            
            computador = melhor_jogada_agente_poda(jogo,2)
            print(f"Jogada do Computador é {computador}")
            jogo = jogo.jogar(computador.uci())

            if (len(jogo.primeiras5Jogadas) < 5):
                jogo.registrarAbertura(computador.uci())
            
            if jogo.venceu():
                cls()
                print("Computador venceu!")
                break
            elif jogo.empate():
                cls()
                print("Empate!")
                print(jogo.tipoEmpate())
                break
    mostraTabuleiroBonitinho()

##BOT X BOT
# if __name__ == "__main__":
#     player = int(input("0 pra preto, 1 pra branco: "))
#     jogo = ChessGame(chess.Board(),player)

#     while not jogo.board.is_game_over():
#         if jogo.board.turn == player:
#             print(jogo.board)
#             IA = melhor_jogada_agente_poda(jogo, 0)
#             print(f"Jogada da IA é {IA.uci()}")
#             jogo = jogo.jogar(IA.uci())
#             if jogo.venceu():
#                 print("IA Venceu!")
#                 break
#             elif jogo.empate():
#                 print("Empate!")
#                 print(jogo.tipoEmpate())
#                 break
#         else:    
#             print(jogo.board)
#             AI = melhor_jogada_agente_poda(jogo, 0)
#             print(f"Jogada do AI é {AI.uci()}")
#             jogo = jogo.jogar(AI.uci())
#             if jogo.venceu():
#                 print("AI venceu!")
#                 break
#             elif jogo.empate():
#                 print("Empate!")
#                 print(jogo.tipoEmpate())
#                 break



















































# if __name__ == "__main__":
#     jogo = ChessGame(chess.Board(fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/1NB1KBN1 w kq - 0 1"), True)
#     print(ev.isEndGame(jogo.board))

#     x = melhor_jogada_agente_poda(jogo, 0)
#     print(x)
#     jogo = jogo.jogar(x)
#     jogo.registrarAbertura(x)

#     humano = lerJogada(list(jogo.board.legal_moves))
#     jogo = jogo.jogar(humano)
#     jogo.registrarAbertura(humano)

#     print(jogo.primeiras5Jogadas)

#     x = melhor_jogada_agente_poda(jogo, 0)
#     print(x)
#     jogo = jogo.jogar(x)
#     jogo.registrarAbertura(x)

#     print(jogo.primeiras5Jogadas)

# board = chess.Board(fen="4k3/p5pp/2p5/8/8/r7/5r2/3K4 b - - 11 35")
# ev.evaluate(board)



#an adjacency list
# positions = {}

# # depth-first search from a FEN string
# def generate_tree(fen, depth):
#     board = chess.Board(fen)
#     legal_moves = list(board.legal_moves)
#     if fen in positions:
#         positions[fen] += legal_moves
#     else:
#         positions[fen] = legal_moves

#     for move in legal_moves:
#         board.push(move)
#         next_fen = board.fen()
#         board.pop()
        
#         if not (depth == 0):
#             generate_tree(next_fen, depth-1)
#         else:
#             return

# try:
#     generate_tree(chess.STARTING_FEN, 3)
    
#     soma = 0

#     for p in positions:
#         soma += len(positions[p])
        
#     print(soma)
# except RecursionError: 
#     print("a")
#     print(len(positions) + sum(len(p) for p in positions))


# board = chess.Board()
# legalMovesList = board.legal_moves
# moves = []
# print(board.result())
# while not board.is_game_over():
#     moves.clear()
#     moves = list(board.legal_moves)

#     board.push(random.choice(moves))

# print(board)
# print(board.result())
# print(board.is_fivefold_repetition())
