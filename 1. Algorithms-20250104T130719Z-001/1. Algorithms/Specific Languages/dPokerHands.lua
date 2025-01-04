-- 1. d) Given 5 playing cards, determine the strongest hand possible.
--       Flush five: 5 cards of the same suit and rank
--       Flush house: Full house in which all cards are of the same suit
--       Five of a kind: 5 cards of the same rank
--       The hands in the Hands enum are in order of decreasing strength.
--       1 is Ace, 11 is Jack, 12 is Queen, 13 is King.
--       You may freely modify everything except the name of solution function and its parameters.

-- 1. d) Déterminez la main la plus forte selon 5 cartes de jeu adonnées.
--       Quinte flush: 5 cartes de la même couleur et du même rang
--       Full flush: Main pleine dans laquelle toutes les cartes sont de la même couleur
--       Quinte: 5 cartes du même rang
--       Les mains dans la enum Hands sont en ordre de puissance décroissante.
--       1 est l'as, 11 est le valet, 12 est la reine, 13 est le roi.
--       N.B.: Les traductions de les mains dans Hands et de les couleurs dans Suits sont à-côté de leur équivalent anglophone.
--       Vous pouvez librement modifier la totalité du ficher mise à part le nom de la fonction solution donnée et ses paramètres.

-- Lua 5.1

local Hands = {
    FLUSH_FIVE = 0,        -- Quinte flush
    FLUSH_HOUSE = 1,       -- Full flush
    FIVE_OF_A_KIND = 2,    -- Quinte
    ROYAL_FLUSH = 3,       -- Suite royale flush
    STRAIGHT_FLUSH = 4,    -- Suite flush
    FOUR_OF_A_KIND = 5,    -- Carré
    FULL_HOUSE = 6,        -- Main Pleine
    FLUSH = 7,             -- Couleur
    STRAIGHT = 8,          -- Suite
    THREE_OF_A_KIND = 9,   -- Brelan
    TWO_PAIR = 10,         -- Deux paires
    PAIR = 11,             -- Paire
    HIGH_CARD = 12,        -- Carte haute
}

local Suits = {
    HEARTS = 1,            -- Coeurs
    DIAMONDS = 2,          -- Carreaux
    SPADES = 3,            -- Piques
    CLUBS = 4,             -- Trèfles
}

local function contains( table, key )
    return table[key] ~= nil;
end;

local function solution( cards )
    assert(#cards == 5);
    assert(contains( Suits, cards[0][1] ));
    assert(cards[0][0] >= 1 and cards[0][0] <= 13);
    return Hands.FIVE_OF_A_KIND;
end;
