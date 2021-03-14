import chess

pieceValue = {
    chess.PAWN : 100,
    chess.KNIGHT : 320,
    chess.BISHOP : 330,
    chess.ROOK : 500,
    chess.QUEEN : 900,
    chess.KING : 20000
}

pieceName = {
    chess.PAWN : "peao",
    chess.KNIGHT : "cav",
    chess.BISHOP : "bispo",
    chess.ROOK : "torre",
    chess.QUEEN : "rain",
    chess.KING : "rei"
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
whiteBishopTable = [-20,-10,-10,-10,-10,-10,-10,-20,
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
        
    

# def evaluate(board, colorAI):
#     pieceSumAI = 0
#     pieceSumPlayer = 0

#     for piece in pieceValue:
#         aiPieces = board.pieces(piece, colorAI)
#         for p in aiPieces:
#             pieceSumAI += pieceValue[piece] + applyOnTable(piece, colorAI, chess.square_mirror(p))
        
#         playerPieces = board.pieces(piece, not colorAI)
#         for p in playerPieces:
#             pieceSumPlayer += -pieceValue[piece] + applyOnTable(piece, not colorAI, p)

#     print(pieceSumAI , pieceSumPlayer)
#     return pieceSumAI + pieceSumPlayer
contadorGlobal = 0
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


#And of course "These values are for white, for black I use mirrored values."
'''
Additionally we should define where the ending begins. For me it might be either if:

Both sides have no queens or
Every side which has a queen has additionally no other pieces or one minorpiece maximum.
'''