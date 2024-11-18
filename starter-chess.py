# -*- coding: utf-8 -*-
from enum import Enum, auto
import time
import chess
from random import choice

def randomMove(b):
    '''Renvoie un mouvement au hasard sur la liste des mouvements possibles. Pour avoir un choix au hasard, il faut
    construire explicitement tous les mouvements. Or, generate_legal_moves() nous donne un itérateur.'''
    return choice([m for m in b.generate_legal_moves()])

def deroulementRandom(b):
    '''Déroulement d'une partie d'échecs au hasard des coups possibles. Cela va donner presque exclusivement
    des parties très longues et sans gagnant. Cela illustre cependant comment on peut jouer avec la librairie
    très simplement.'''
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    b.push(randomMove(b))
    deroulementRandom(b)
    b.pop()

board = chess.Board()
#deroulementRandom(board)


###### Ex 1 ######

# Q1
# facteur de branchement:
b_moy = (2 
+ 3 + 2 
+ 2 + 1 + 2 + 2 + 1
+ 2 + 2 + 3 + 2 + 2 + 2 + 2 + 3)/16
# print(b_moy)
# nombre d’enfants disponibles dans un arbre de données pour chaque noeud
# ici, en moyenne 2.0625 et au maximum 3
# Les branches d'un arbre de jeu ne sont pas nécessairement de même hauteur, certaines parties peuvent finir plus vite

# Q2
# Sans tenir compte de la feuille ayant une valeur de “??”, quelle est le meilleur plateau pour Ami ? 
# Quel est le meilleur plateau pour Ennemi ? Expliquez le fait que deux noeuds de l’arbre aient un seul fils.
# Est-ce plutôt une bonne chose ou une mauvaise chose pour ami ?
# Plateau de valeur 8
# Plateaux de valeur -4 (en particulier le dernier plateau, que des petits scores)
# 1 seul fils quand Ami n'a pas eu le choix pour son coup

# Q3
# 3. Donnez la plus grande valeur possible pour la feuille ayant la valeur heuristique 
# notée “??” et permettant à α-β d’élaguer la feuille 8. 
# Vous utiliserez cette valeur pour la suite du sujet ;
# ?? = 3



###### Ex 2 ######


Ex2_Q1 = False
Ex2_Q2 = True
Ex2_Q4_a = False
Ex2_Q4_b = False


infinity = 100000

# Ex2 Q1
print("---------------------------------------------")
print("Ex2 Q1: Exploration")


def explore_aux(b, horizon, counts):
    '''
    Fonction recursive auxiliaire pour explore()
    counts = [count_games, count_nodes]
    ou count_games permet de compter le nombre de parties explorees (feuilles)
    et count_nodes le nombre total de noeuds
    '''
    if b.is_game_over() or horizon == 0:
        counts[0] += 1
    else:
        for m in b.legal_moves:
            counts[1] += 1
            b.push(m)
            explore_aux(b, horizon - 1, counts)
            b.pop()
    return counts


def explore(horizon):
    '''
    Explore toutes les parties possibles avec horizon maximal
    et renvoie les compteurs [count_games, count_nodes].
    Ceux-ci sont initialement à [0,1]
    (pas encore de feuille, mais 1 noeud correspondant au plateau de départ)
    '''
    board = chess.Board()
    return explore_aux(board, horizon, [0,1])


if Ex2_Q1:
    start_time = time.time()
    [count_games, count_nodes] = explore(1)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(f"Nb of explored games: {count_games}")
    print(f"Nb of explored nodes: {count_nodes}")



# Ex2 Q2
print("---------------------------------------------")
print("Ex2 Q2: Heuristique pour l'evaluation")

def evaluate(b):
    '''
    Heuristique pour l'evaluation du plateau de jeu d'echecs
    '''

    if b.is_game_over():
        did_white_win = b.outcome().winner
        if did_white_win is None:
            return -50 # match nul, pas souhaitable
        elif did_white_win:
            return infinity/10 # victoire des blancs
        else:
            return -infinity/10 # victoire des noirs

    pieces_map = b.piece_map()
    pieces = [piece.symbol() for piece in pieces_map.values()]
    
    # un pion s'approchant du bord oppose du plateau est plus avantageux
    # on regarde d'abord sur quelles lignes (rangs) se trouvent les pions P et p:
    pawn_ranks = {'P': [], 'p': []} 
    for square,piece in pieces_map.items():
        if piece.symbol()  == 'P' or piece.symbol() == 'p':
            pawn_ranks[piece.symbol()].append(chess.square_rank(square))
    
    # puis on evalue l'avantage des pions par rapport a leurs positions sur ces lignes:
    # attention: chess.square_rank renvoie un numéro entre 0 et 7 (au lieu de 1-8 comme rank_name)
    P = 0 # pions blancs
    p = 0 # pions noirs
    for rank in pawn_ranks['P']:
            P += rank # il vaut mieux aller en haut
    for rank in pawn_ranks['p']:
            p += (7-rank) # il vaut mieux aller en bas

    # Evaluation finale avec les poids proposes par Shannon
    return (
        200*(pieces.count('K') - pieces.count('k')) 
        + 9*(pieces.count('Q') - pieces.count('q')) 
        + 5*(pieces.count('R') - pieces.count('r'))
        + 3*(pieces.count('B') - pieces.count('b') + pieces.count('N') - pieces.count('n')) 
        + (P - p)
    )

if Ex2_Q2:
    board = chess.Board()
    print(evaluate(board)) # 0 pour le plateau initial


# Ex2 Q3
print("---------------------------------------------")
print("Ex2 Q3: Minimax")

def minimax_(b, horizon, max_player=True):
    '''
    Minimax sur les echecs
    Retourne un couple (eval, best_move):
    l'evaluation du plateau a horizon maximal
    et le meilleur coup a jouer
    '''

    if b.is_game_over() or horizon == 0:
        return evaluate(b), None
    
    best_move = None
    # si c'est le tour de max_player (ami)
    if max_player:
        max_eval = -infinity
        for m in b.legal_moves:
            b.push(m)
            eval = minimax(b, horizon-1, False)[0]
            max_eval = max (eval, max_eval)
            if eval == max_eval:
                best_move = m
            b.pop()
        return max_eval, best_move
    # si c'est le tour de min_player (ennemi)
    else:
        min_eval = infinity
        for m in b.legal_moves:
            b.push(m)
            eval = minimax(b, horizon-1, True)[0]
            min_eval = min (eval, min_eval)
            if eval == min_eval:
                best_move = m
            b.pop()
        return min_eval, best_move

def choose_move_or_none(best_moves):
    if len(best_moves) == 0:
        return None
    return choice(best_moves)


def minimax(b, horizon, max_player=True, return_move=False):
    '''
    Minimax sur les echecs
    avec mecanisme pour eviter de tourner en boucle
    Retourne un couple (eval, best_move):
    l'evaluation du plateau a horizon maximal
    et le (ou un des) meilleur coup a jouer
    (si return_move est False, le coup n'est pas calcule et on retourne None)
    '''

    if b.is_game_over() or horizon == 0:
        return evaluate(b), None
    
    best_moves = []
    
    # si c'est le tour de max_player (ami)
    if max_player:
        max_eval = -infinity
        for m in b.legal_moves:
            b.push(m)
            eval = minimax(b, horizon-1, max_player=False)[0]
            # mise a jour evaluation et liste des meilleurs coups
            if return_move and eval == max_eval:
                best_moves.append(m)
            elif eval > max_eval:
                if return_move:
                    best_moves = [m]
                max_eval = eval
            b.pop()
        return max_eval, choose_move_or_none(best_moves)
    # si c'est le tour de min_player (ennemi)
    else:
        min_eval = infinity
        for m in b.legal_moves:
            b.push(m)
            eval = minimax(b, horizon-1, max_player=True)[0]
            # mise a jour evaluation et liste des meilleurs coups
            if return_move and eval == min_eval:
                best_moves.append(m)
            elif eval < min_eval:
                if return_move:
                    best_moves = [m]
                min_eval = eval
            b.pop()
        return min_eval, choose_move_or_none(best_moves)

# Ex2 Q4
print("---------------------------------------------")
print("Ex2 Q4: IA contre IA")     

def deroulement_random_vs_minimax(b, horizon, is_random_white=True, is_random_turn=True):
    '''Effectue un déroulement random vs minmax du jeu d'echecs'''
    print("----------")
    print(b)
    print("----------")
    print(evaluate(b))
    print("----------")
    if b.is_game_over():
        print(b.outcome())
        return
    
    if (is_random_turn):
        print("Random is playing")
        move = randomMove(b)
    else:
        print("Minimax is playing")
        move = minimax(b, horizon, max_player=not is_random_white, return_move=True)[1]
    b.push(move)
    deroulement_random_vs_minimax(b, horizon, is_random_white, not is_random_turn)
    b.pop()
    
# if Ex2_Q4_a:
#     board = chess.Board()
#     deroulement_random_vs_minimax(board, 3)


def deroulement_minimax(b, horizon1, horizon2, max_player=True):
    '''Effectue un déroulement minmax du jeu d'echecs'''
    print("----------")
    print(b)
    print("----------")
    print(evaluate(b))
    print("----------")
    if b.is_game_over():
        print(b.outcome)
        return
    
    move = minimax(b, horizon1, max_player, return_move=True)[1]
    b.push(move)
    deroulement_minimax(b, horizon2, horizon1, not max_player)
    b.pop()

# if Ex2_Q4_b:
#     board = chess.Board()
#     deroulement_minimax(board, 1, 3)

# dans la suit on fera un programme général pour simuler les différents matches


###### Ex 3 ######

Ex3_Q1 = False
Ex3_Q2 = False

# Ex3 Q1
print("---------------------------------------------")
print("Ex3 Q1: AlphaBeta")
        
def alphabeta(b, alpha, beta, horizon, max_player=True, return_move=False):
    '''
    Minimax avec elagage alpha-beta sur les echecs
    avec mecanisme pour eviter de tourner en boucle
    Retourne un couple (eval, best_move):
    l'evaluation du plateau a horizon maximal
    et le (ou un des) meilleur coup a jouer
    (si return_move est False, le coup n'est pas calcule et on retourne None)
    '''

    if b.is_game_over() or horizon == 0:
        return evaluate(b), None
    
    best_moves = []
    # si c'est le tour de max_player (ami)
    if max_player:
        value = -infinity
        for m in b.legal_moves:
            b.push(m)
            tmp_value = alphabeta(b, alpha, beta, horizon-1, max_player=False)[0]
            # mise a jour evaluation et liste des meilleurs coups
            if return_move and tmp_value == value:
                best_moves.append(m)
            elif tmp_value > value:
                if return_move:
                    best_moves = [m]
                value = tmp_value
            ### Elagage BETA
            if beta <= value:
                b.pop()
                break
            ###
            alpha = max(alpha, value)
            b.pop()
    # si c'est le tour de min_player (ennemi)
    else:
        value = infinity
        for m in b.legal_moves:
            b.push(m)
            tmp_value = alphabeta(b, alpha, beta, horizon-1, max_player=True)[0]
            # mise a jour evaluation et liste des meilleurs coups
            if return_move and tmp_value == value:
                best_moves.append(m)
            elif tmp_value < value:
                if return_move:
                    best_moves = [m]
                value = tmp_value
            ### Elagage ALPHA
            if value <= alpha:
                b.pop()
                break
            ###
            beta = min(beta, value)
            b.pop()
    return value, choose_move_or_none(best_moves)


# Ex3 Q2
print("---------------------------------------------")
print("Ex3 Q2: Humain contre IA")

#################################################################
################## Programme général ############################
#################################################################

class TypeJoueur(Enum):
    RANDOM = auto()
    MINMAX = auto()
    ALPHABETA = auto()
    HUMAN = auto()

class Joueur:
    """Classe pour définir le joueur"""
    def __init__(self, type_joueur: TypeJoueur, color: chess.Color, horizon=0):
        self.type_joueur = type_joueur
        self.color = color
        if (type_joueur == TypeJoueur.MINMAX or type_joueur == TypeJoueur.ALPHABETA):
            self.horizon = horizon

    def name(self):
        str_name = str(self.type_joueur.name)
        if (self.type_joueur == TypeJoueur.MINMAX or self.type_joueur == TypeJoueur.ALPHABETA):
            str_name += f" {self.horizon}"
        str_name += " WHITE" if self.color else " BLACK"
        return str_name
    
    def move(self, b):
        if (self.type_joueur == TypeJoueur.RANDOM):
            return randomMove(b)

        if (self.type_joueur == TypeJoueur.MINMAX):
            return minimax(b, self.horizon, self.color, return_move=True)[1]

        if (self.type_joueur == TypeJoueur.ALPHABETA):
            return alphabeta(b, -infinity, infinity, self.horizon, self.color, return_move=True)[1]
        
        if self.type_joueur == TypeJoueur.HUMAN:
            if b.is_check():
                print("Vous êtes en échec!")
            print("A vous de jouer!")
            input_from = input("De quelle case voulez-vous partir?")
            input_to = input("En quelle case voulez-vous aller?")
            try:
                move =  b.find_move(chess.parse_square(input_from), chess.parse_square(input_to))
            except(chess.IllegalMoveError, ValueError):
                print("Ce mouvement n'est pas autorisé, veuillez réessayer")
                return self.move(b)
            return move
    
    def outcome(self, b):
        termination = b.outcome().termination.name
        did_white_win = b.outcome().winner
        if did_white_win is None:
            print("Match Nul!")
        elif did_white_win:
            print("Victoire aux Blancs")
        else:
            print("Victoire aux Noirs")
        print("Details: " + termination)
        return


def deroulement(white_player, black_player):
    board = chess.Board()
    deroulement_aux(board, white_player, black_player)


def deroulement_aux(b, white_player, black_player, is_white_turn = True):
    '''Effectue un déroulement du jeu d'echecs'''
    print("----------")
    print(b)
    print("----------")
    print(evaluate(b))
    print("----------")
    
    if b.is_game_over():
        white_player.outcome(b)
        return

    if is_white_turn:
        print(white_player.name() + " joue")
        move = white_player.move(b)
    else:
        print(black_player.name() + " joue")
        move = black_player.move(b)
    b.push(move)
    deroulement_aux(b, white_player, black_player, not is_white_turn)
    b.pop()



Ex2_Q4_a = True
Ex2_Q4_b = False
Ex3_Q1 = False
Ex3_Q2 = False

if Ex2_Q4_a:
    deroulement(
        Joueur(TypeJoueur.RANDOM, chess.WHITE), 
        Joueur(TypeJoueur.MINMAX, chess.BLACK, 3)
        )

if Ex2_Q4_b:
    deroulement(
        Joueur(TypeJoueur.MINMAX, chess.WHITE, 1), 
        Joueur(TypeJoueur.MINMAX, chess.BLACK, 3)
        )

if Ex3_Q1:
    deroulement(
        Joueur(TypeJoueur.ALPHABETA, chess.WHITE, 2), 
        Joueur(TypeJoueur.ALPHABETA, chess.BLACK, 2)
        )
    
if Ex3_Q2:
    deroulement(
        Joueur(TypeJoueur.HUMAN, chess.WHITE), 
        Joueur(TypeJoueur.ALPHABETA, chess.BLACK, 3)
        )