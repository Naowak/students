# -*- coding: utf-8 -*-

import time
import Tictactoe 
from random import randint,choice

def RandomMove(b):
    '''Renvoie un mouvement au hasard sur la liste des mouvements possibles'''
    return choice(b.legal_moves())

def deroulementRandom(b):
    '''Effectue un déroulement aléatoire du jeu de morpion.'''
    print("----------")
    print(b)
    if b.is_game_over():
        res = getresult(b)
        if res == 1:
            print("Victoire de X")
        elif res == -1:
            print("Victoire de O")
        else:
            print("Egalité")
        return
    b.push(RandomMove(b))
    deroulementRandom(b)
    b.pop()


def getresult(b):
    '''Fonction qui évalue la victoire (ou non) en tant que X. Renvoie 1 pour victoire, 0 pour 
       égalité et -1 pour défaite. '''
    if b.result() == b._X:
        return 1
    elif b.result() == b._O:
        return -1
    else:
        return 0
    
# def explore(board):
#     # Check condition arret
#     if board.is_game_over():
#         result = getresult(board)
#         if result == 1:
#             # J'ai gagné
#             return 1, 0, 0
#         elif result == -1:
#             # j'ai perdu
#             return 0, 0, 1
#         else:
#             # égalité
#             return 0, 1, 0
    
#     legal_moves = board.legal_moves()
#     results = [0, 0, 0]
#     for move in legal_moves:
#         # Pour chaque coup possible
#         board.push(move)
#         res = explore(board) # On descend d'un niveau dans l'arbre
#         for i in range(3): # On somme toutes les victoires, égalités et défaites que l'on obtiens sur l'ensemble des feuilles explorées
#             results[i] += res[i]
#         board.pop()
    
#     return results



# board = Tictactoe.Board()
# begin = time.time()
# results = explore(board)
# end = time.time() - begin
# print('Victoire: ', results[0])
# print('Egalité: ', results[1])
# print('Défaite: ', results[2])
# print('Nombre de parties:', sum(results))
# print('Temps requis :', end)
    

### ------------------------------------

# def exploreAllMoves(b):
#     '''Fonction qui explore tous les coups possibles à partir de la position actuelle'''
#     if board.is_game_over():
#         result = getresult(board)
#         if result == 1:
#             global win_count
#             win_count += 1
#         elif result == -1:
#             global lose_count
#             lose_count += 1
#         else:
#             global draw_count
#             draw_count += 1
#         global total_games
#         total_games += 1
#         return

#     legal_moves = board.legal_moves()
#     for move in legal_moves:
#         board.push(move)
#         exploreAllMoves(board)
#         board.pop()

# def explore(board):

#     if board.is_game_over():
#         print(board)
#         return

#     legal_moves = board.legal_moves()
#     for move in legal_moves:
#         board.push(move)
#         explore(board)
#         board.pop()

# def exploreAllMoves(b):
#     '''Fonction qui explore tous les coups possibles à partir de la position actuelle'''
#     # Check if game over, if yes return result
#     if board.is_game_over():
#         result = getresult(board)
#         if result == 1:
#             return 1, 0, 0
#         elif result == -1:
#             return 0, 0, 1
#         else:
#             return 0, 1, 0

#     # Otherwise, explore all legal moves and return the sum of the results
#     legal_moves = board.legal_moves()
#     results = [0, 0, 0]
#     for move in legal_moves:
#         board.push(move)
#         result = exploreAllMoves(board)
#         for i in range(3):
#             results[i] += result[i]
#         board.pop()
#     return results

# # Initialisation des compteurs
# # win_count = 0
# # lose_count = 0
# # draw_count = 0
# # total_games = 0

# # Création du plateau de jeu
# board = Tictactoe.Board()
# begin = time.time()
# results = exploreAllMoves(board) 
# end = time.time()
# # print("Victoires: ", win_count)
# # print("Egalités: ", draw_count)
# # print("Défaites: ", lose_count)
# # print("Total de parties: ", total_games)
# print("Victoires: ", results[0])
# print("Egalités: ", results[1])
# print("Défaites: ", results[2])
# print("Total de parties: ", sum(results))
# print("Temps d'exécution: ", end - begin, " secondes")

# # print(board)

# ### Deroulement d'une partie aléatoire
# #deroulementRandom(board)

# # print("Apres le match, chaque coup est défait (grâce aux pop()): on retrouve le plateau de départ :")
# # print(board)

# ### ------------------------------------



# def minimax(board, is_maximizing):
#     # Check game over
#     if board.is_game_over():
#         result = getresult(board)
#         return result

#     # My turn
#     if is_maximizing:
#         best_score = -float('inf')
#         for move in board.legal_moves():
#             board.push(move)
#             score = minimax(board, False)
#             board.pop()
#             best_score = max(score, best_score)
#         return best_score
#     # Ennemy Response
#     else:
#         best_score = float('inf')
#         for move in board.legal_moves():
#             board.push(move)
#             score = minimax(board, True)
#             board.pop()
#             best_score = min(score, best_score)
#         return best_score

# # Création du plateau de jeu
# board = Tictactoe.Board()

# # Recherche de la stratégie gagnante
# result = minimax(board, True)

# # Affichage du résultat
# if result == 1:
#     print("Il existe une stratégie gagnante pour X.")
# elif result == 0:
#     print("Il n'existe pas de stratégie gagnante pour X, mais il peut forcer une égalité.")
# else:
#     print("Il n'existe pas de stratégie gagnante pour X.")



