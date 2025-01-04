# 1. d) Given 5 playing cards, determine the strongest hand possible.
#       Flush five: 5 cards of the same suit and rank
#       Flush house: Full house in which all cards are of the same suit
#       Five of a kind: 5 cards of the same rank
#       The hands in the Hands enum are in order of decreasing strength.
#       1 is Ace, 11 is Jack, 12 is Queen, 13 is King.
#       You may freely modify everything except the name of solution function and its parameters.

# 1. d) Déterminez la main la plus forte selon 5 cartes données.
#       Quinte flush: 5 cartes de la même couleur et du même rang
#       Full flush: Main pleine dans laquelle toutes les cartes sont de la même couleur
#       Quinte: 5 cartes du même rang
#       Les mains dans la enum Hands sont en ordre de puissance décroissante.
#       1 est l'as, 11 est le valet, 12 est la reine, 13 est le roi.
#       N.B.: Les traductions de les mains dans Hands et de les couleurs dans Suits sont juste au-dessus de leur équivalent en Anglais.
#       Vous pouvez librement modifier la totalité du ficher mise à part le nom de la fonction solution donnée et ses paramètres.


from enum import Enum
#                       Quinte flush   Full Flush     Quinte            Suite royale flush   Suite flush       Carré             Main pleine    Couleur  Suite       Brelan             Deux paires  Paire   Carte haute
Hands = Enum('Hands', ['FLUSH_FIVE',  'FLUSH_HOUSE', 'FIVE_OF_A_KIND', 'ROYAL_FLUSH',       'STRAIGHT_FLUSH', 'FOUR_OF_A_KIND', 'FULL_HOUSE' , 'FLUSH', 'STRAIGHT', 'THREE_OF_A_KIND', 'TWO_PAIR',  'PAIR', 'HIGH_CARD'])

#                       Coeurs    Carreaux    Piques    Trèfles
Suits = Enum('Suits', ['HEARTS', 'DIAMONDS', 'SPADES', 'CLUBS'])


def solution(*cards):
    assert len(cards) == 5
    assert isinstance(cards[0], (int, Suits))
    assert cards[0][0] >= 1 and cards[0][0] <= 13
    return Hands.FIVE_OF_A_KIND

