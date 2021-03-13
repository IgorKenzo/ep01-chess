import chess
from pieces import pieceValue
import random
import evaluation as ev




board = chess.Board(fen="4k3/p5pp/2p5/8/8/r7/5r2/3K4 b - - 11 35")
ev.evaluate(board)









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
# while not board.is_game_over():
#     moves.clear()
#     moves = list(board.legal_moves)

#     board.push(random.choice(moves))

# print(board)
# print(board.result())
# print(board.is_fivefold_repetition())
