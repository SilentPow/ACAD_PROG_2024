# 1. f) Determine if a string from standard input is a palindrome.
#       If your code returns a value without attempting to solve the question, you will get a score of 0.
#       You may freely modify everything except the name of solution function and its parameters.

# 1. f) Déterminez si une chaîne de charactères reçue de la flux standard d'entrée est un palindrôme.
#       Si votre code ramène une valeure sans tenter de résoudre la question, vous auriez un score de 0.
#       Vous pouvez librement modifier la totalité du ficher mise à part le nom de la fonction solution donnée et ses paramètres.



def solution():
    string = input()
    assert isinstance(string, str)
    assert len(string) <= 10
    if string[0] == string[-1]:
        return True
    else:
        return False