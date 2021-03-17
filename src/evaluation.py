import chess
import random

openings = ["e2e4 e7e5 g1f3 b8c6 f1c4", "d2d4 g8f6 c2c4 g7g6 f2f3", "c2c4 e7e6 b1c3 d7d5 d2d4", "e2e4 e7e6 d2d4 d7d5 b1d2", "c2c4 e7e5 b1c3 g8f6 g1f3", 
            "e2e4 g7g6 d2d4 f8g7 b1c3", "c2c4 c7c5 g2g3 b8c6 f1g2", "d2d4 g8f6 c2c4 e7e6 g1f3", "c2c4 e7e6 b1c3 g8f6 g1f3", "c2c4 e7e5 b1c3 g8f6 g1f3", 
            "d2d4 g8f6 c2c4 e7e6 g1f3", "e2e4 e7e5 g1f3 b8c6 b1c3", "d2d4 g8f6 c2c4 e7e6 g1f3", "d2d4 d7d5 c2c4 c7c6 g1f3", "d2d4 g8f6 g1f3 g7g6 c1g5",
            "e2e4 e7e6 d2d4 d7d5 b1c3", "e2e4 e7e6 d2d4 d7d5 e7e5", "e2e4 e7e5 f1c4 g8f6 d1d3", "d2d4 g8f6 c2c4 g7g6 b1c3", "g1f3 c7c5 c2c4 g8f6 g2g3",
            "c2c4 e7e6 g2g3 g8f6 f1g2", "d2d4 g8f6 c2c4 e7e6 g2g3", "d2d4 g8f6 c2c4 e7e6 g1f3", "d2d4 g8f6 c2c4 g7g6 g2g3", "d2d4 d7d5 c2c4 e7e6 g1f3",
            "e2e4 e7e6 d2d4 d7d5 b1c3", "c2c4 e7e5 b1c3 g8f6 g1f3", "c2c4 e7e6 g1f3 d7d5 e2e3", "d2d4 d7d5 c2c4 e7e6 g1f3", "g1f3 c7c5 c2c4 g8f6 b1c3",
            "g1f3 d7d5 g2g3 g8f6 f1g2", "e2e4 e7e5 g1f3 g8f6 d2d4", "d2d4 g8f6 c2c4 e7e6 g1f3", "d2d4 g8f6 c2c4 c7c5 d7d5", "e2e4 c7c5 g1f3 b8c6 d2d4",
            "g1f3 d7d5 d2d4 e7e6 g2g3", "e2e4 c7c5 g1f3 d7d6 d2d4", "e2e4 e7e5 g1f3 b8c6 f1b5", "c2c4 g8f6 b1c3 e7e6 e2e4", "e2e4 c7c6 d2d4 d7d5 e7e5"]

pieceValue = {
    chess.PAWN : 100,
    chess.KNIGHT : 320,
    chess.BISHOP : 330,
    chess.ROOK : 500,
    chess.QUEEN : 900,
    chess.KING : 20000
}

pieceValue2 = {
    chess.PAWN : 10,
    chess.KNIGHT : 30,
    chess.BISHOP : 30,
    chess.ROOK : 50,
    chess.QUEEN : 90,
    chess.KING : 900
}

pieceName = {
    chess.PAWN : "Pawn",
    chess.KNIGHT : "Knight",
    chess.BISHOP : "bishop",
    chess.ROOK : "Rook",
    chess.QUEEN : "Queen",
    chess.KING : "King"
}

# Aplicando o
#https://www.chessprogramming.org/Simplified_Evaluation_Function
# Pawn evaluation table
whitePawnTable = [
 0,  0,  0,  0,  0,  0,  0,  0,
 50, 50, 50, 50, 50, 50, 50, 50,
 10, 10, 20, 30, 30, 20, 10, 10,
 5,  5, 10, 25, 25, 10,  5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5, -5,-10,  0,  0,-10, -5,  5,
 5, 10, 10,-20,-20, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0 ]

blackPawnTable = [-x for x in whitePawnTable]

 # knight
whiteKnightTable = [
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  0,  0,  0,-20,-40,
-30,  0, 10, 15, 15, 10,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 10, 15, 15, 10,  5,-30,
-40,-20,  0,  5,  5,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50]

blackKnightTable = [-x for x in whiteKnightTable]

# bishop
whiteBishopTable = [
-20,-10,-10,-10,-10,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  5,  0,  0,  0,  0,  5,-10,
-20,-10,-10,-10,-10,-10,-10,-20]

blackBishopTable = [-x for x in whiteBishopTable]

#rook
whiteRookTable = [
0,  0,  0,  0,  0,  0,  0,  0,
5, 10, 10, 10, 10, 10, 10,  5,
-5,  0,  0,  0,  0,  0,  0, -5,
-5,  0,  0,  0,  0,  0,  0, -5,
-5,  0,  0,  0,  0,  0,  0, -5,
-5,  0,  0,  0,  0,  0,  0, -5,
-5,  0,  0,  0,  0,  0,  0, -5,
0,  0,  0,  5,  5,  0,  0,  0]

blackRookTable = [-x for x in whiteRookTable]

#queen
whiteQueenTable = [
-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5,  5,  5,  5,  0,-10,
-5,  0,  5,  5,  5,  5,  0, -5,
0,  0,  5,  5,  5,  5,  0, -5,
-10,  5,  5,  5,  5,  5,  0,-10,
-10,  0,  5,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20]

blackQueenTable = [-x for x in whiteQueenTable]

#king middle game
whiteKingMidGameTable= [
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-20,-30,-30,-40,-40,-30,-30,-20,
-10,-20,-20,-20,-20,-20,-20,-10,
 20, 20,  0,  0,  0,  0, 20, 20,
 20, 30, 10,  0,  0, 10, 30, 20]

blackKingMidGameTable = [-x for x in whiteKingMidGameTable]

#king end game
whiteKingEndGameTable = [
-50,-40,-30,-20,-20,-30,-40,-50,
-30,-20,-10,  0,  0,-10,-20,-30,
-30,-10, 20, 30, 30, 20,-10,-30,
-30,-10, 30, 40, 40, 30,-10,-30,
-30,-10, 30, 40, 40, 30,-10,-30,
-30,-10, 20, 30, 30, 20,-10,-30,
-30,-30,  0,  0,  0,  0,-30,-30,
-50,-30,-30,-30,-30,-30,-30,-50]

blackKingEndGameTable = [-x for x in whiteKingEndGameTable]

def applyOnTable(piece, color, index):
    if piece == chess.PAWN:
        return whitePawnTable[index] if color == chess.WHITE else blackPawnTable[index]
    if piece == chess.KNIGHT:
        return whiteKnightTable[index] if color == chess.WHITE else blackKnightTable[index]
    if piece == chess.BISHOP:
        return whiteBishopTable[index] if color == chess.WHITE else blackBishopTable[index]
    if piece == chess.ROOK:
        return whiteRookTable[index] if color == chess.WHITE else blackRookTable[index]
    if piece == chess.QUEEN:
        return whiteQueenTable[index] if color == chess.WHITE else blackQueenTable[index]
    if piece == chess.KING:
        return whiteKingMidGameTable[index] if color == chess.WHITE else blackKingMidGameTable[index]
        
def evaluate(board, colorAI):
    pieceSumAI = 0
    pieceSumPlayer = 0

    if (board.is_checkmate()):
        txt = board.result().split("-")
        if (txt[0] == colorAI):
            return 1000000#float("inf")
        else:
            return -1000000#float("-inf")

    for piece in pieceValue:
        aiPieces = board.pieces(piece, colorAI)
        testeA = 0
        for p in aiPieces:
            testeA += pieceValue[piece] + applyOnTable(piece, colorAI, chess.square_mirror(p))
            #print(testeA)
        pieceSumAI += testeA


        #print(f'Peça: {pieceName[piece]}. AI: {testeA} SOMA: {pieceSumAI}')
        
        playerPieces = board.pieces(piece, not colorAI)
        testeB = 0
        for p in playerPieces:
            #print(-pieceValue[piece], applyOnTable(piece, not colorAI, p))
            testeB += -pieceValue[piece] + applyOnTable(piece, not colorAI, p)
        pieceSumPlayer += testeB
        
        #print(f'Peça: {pieceName[piece]}. Player: {testeB}')

    #print(pieceSumAI , pieceSumPlayer)
    return pieceSumAI + pieceSumPlayer



def buscarAbertura(board):
    if (len(board.primeiras5Jogadas) <= 0):
        r = random.choice(openings)
        plays = r.split(" ")        
        return plays[0]
    else:
        size = len(board.primeiras5Jogadas)
        for op in openings:           
            control = True
            plays = op.split(" ")
            # print(plays)
            for i in range(size):
                # print(i)
                # print(board.primeiras5Jogadas[i], plays[i])            
                if (board.primeiras5Jogadas[i] != plays[i]):
                    control = False
            if control:
                return plays[size]
    return -1




# def evaluate2(board, colorAI):
#     total = 0
#     for piece in pieceValue:
#         aiPieces = board.pieces(piece, colorAI)
#         for p in aiPieces:
#             valor = pieceValue2[piece]
#             total += valor
#         playerPieces = board.pieces(piece, not colorAI)
#         for p in playerPieces:
#             valor = pieceValue2[piece]
#             total -= valor
#     return total

#And of course "These values are for white, for black I use mirrored values."
'''
Additionally we should define where the ending begins. For me it might be either if:

Both sides have no queens or
Every side which has a queen has additionally no other pieces or one minorpiece maximum.
'''