from jogo import Jogo, Jogador
import chess
import evaluation as ev

def minimax(jogo, turno_max, jogador, profundidade_maxima = 8):
  # se o jogo acabou ou se a profundidade é máxima
  if jogo.venceu() or jogo.empate() or profundidade_maxima == 0:
    return jogo.avaliar()

  if turno_max: # turno do MAX
    melhor_valor = float("-inf") # Menos infinito é o menor valor
    for proximo_jogo in jogo.jogos_validos():
      utilidade = minimax(jogo.jogar(proximo_jogo.uci()), False, jogador, profundidade_maxima - 1)
      melhor_valor = max(utilidade, melhor_valor) # proximo_jogo com o maior valor
    return melhor_valor
  else: # turno no MIN
    pior_valor = float("inf") # Mais infinito é o maior valor
    for proximo_jogo in jogo.jogos_validos():
      utilidade = minimax(jogo.jogar(proximo_jogo.uci()), True, jogador, profundidade_maxima - 1)
      pior_valor = min(utilidade, pior_valor) # proximo_jogo com o menor valor
    return pior_valor

def minimax_alfabeta(jogo, turno_max, jogador, profundidade_maxima = 8, alfa = float("-inf"), beta = float("inf")):
  # se o jogo acabou ou se a profundidade é máxima
  if jogo.venceu() or jogo.empate() or profundidade_maxima == 0:
    return jogo.avaliar()

  if turno_max: # turno do MAX
    utilidade = float("-inf")
    for proximo_jogo in jogo.jogos_validos():
      utilidade = max(utilidade, minimax_alfabeta(jogo.jogar(proximo_jogo.uci()), False, jogador, profundidade_maxima - 1, alfa, beta))
      alfa = max(utilidade, alfa)
      if beta <= alfa:
        return utilidade
    return utilidade
  else: # turno no MIN
    utilidade = float("inf")
    for proximo_jogo in jogo.jogos_validos():
      utilidade = min(utilidade, minimax_alfabeta(jogo.jogar(proximo_jogo.uci()), True, jogador, profundidade_maxima - 1, alfa, beta))
      beta = min(utilidade, beta)
      if beta <= alfa:
        return utilidade
    return utilidade

# Encotrar o melhor movimento do computador
def melhor_jogada_agente(jogo, profundidade_maxima = 8):
  melhor_valor = float("-inf")
  melhor_jogada = -1
  for proximo_jogo in jogo.jogos_validos():
    utilidade = minimax(jogo.jogar(proximo_jogo.uci()), False, jogo.turno(), profundidade_maxima)
    #utilidade = minimax(jogo.board, profundidade_maxima, False)
    if utilidade > melhor_valor:
      melhor_valor = utilidade
      melhor_jogada = proximo_jogo
  return melhor_jogada

def melhor_jogada_agente_poda(jogo, profundidade_maxima = 8):

  if (len(jogo.primeiras5Jogadas) < 5):
    jogada = ev.buscarAbertura(jogo)
    if (jogada != -1):
      return chess.Move.from_uci(jogada)
  
  melhor_valor = float("-inf")
  melhor_jogada = -1
  # print(len(jogo.jogos_validos()))
  for proximo_jogo in jogo.jogos_validos():
    utilidade = minimax_alfabeta(jogo.jogar(proximo_jogo.uci()), False, jogo.turno(), profundidade_maxima)
    # print(utilidade)
    if utilidade > melhor_valor:
      melhor_valor = utilidade
      melhor_jogada = proximo_jogo
  return melhor_jogada

































# def minimax(board, depth, maximizing_player):
#   if depth == 0 or board.is_game_over():
#       return ev.evaluate(board, maximizing_player)#jogo.avaliar(board)
#   if maximizing_player:
#       value = -float('inf')
#       for move in board.legal_moves:
#           board.push(move)
#           value = max(value, minimax(board, depth - 1, False))
#           board.pop()
#       return value
#   else:
#       value = float('inf')
#       for move in board.legal_moves:
#           board.push(move)
#           value = min(value, minimax(board, depth - 1, True))
#           board.pop()
#       return value

# def minimax_alfabeta(jogo, turno_max, jogador, profundidade_maxima = 8, alfa = float("-inf"), beta = float("inf")):
#   # se o jogo acabou ou se a profundidade é máxima
#   if jogo.venceu() or jogo.empate() or profundidade_maxima == 0:
#     return jogo.avaliar2()

#   if turno_max: # turno do MAX
#     for proximo_jogo in jogo.jogos_validos():
#       utilidade = minimax_alfabeta(jogo.jogar(proximo_jogo.uci()), False, jogador, profundidade_maxima - 1, alfa, beta)
#       alfa = max(utilidade, alfa)
#       if beta <= alfa:
#         break
#     return alfa
#   else: # turno no MIN
#     for proximo_jogo in jogo.jogos_validos():
#       utilidade = minimax_alfabeta(jogo.jogar(proximo_jogo.uci()), True, jogador, profundidade_maxima - 1, alfa, beta)
#       beta = min(utilidade, beta)
#       if beta <= alfa:
#         break
#     return beta