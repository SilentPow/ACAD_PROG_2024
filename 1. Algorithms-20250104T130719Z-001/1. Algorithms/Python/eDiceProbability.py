# 1. e) Given several dice of varying sizes, determine the average value when rolling all dice. 
#       The list of tuples dice is of the format xdy, where x is the number of dice and y is the size of the dice. For example, 2d6 is two six-sided dice.
#       You may freely modify everything except the name of solution function and its parameters.

# 1. e) Déterminez la valeur moyenne obtenue à partir de plusieurs dés de tailles différentes en roulant tous les dés. 
#       La liste de tuples dice est du format xdy, où x est le nombre de dés et y est la tailles des dés. Par exemple, 2d6 représente deux dés à six faces.
#       Vous pouvez librement modifier la totalité du ficher mise à part le nom de la fonction solution donnée et ses paramètres.



def solution(*dice, n):
    assert isinstance(n, int)
    assert isinstance(dice[0], (int, int))
    assert dice[0][0] > 0
    assert dice[0][1] > 0
    probability = 0.5
    assert probability <= 1 and probability >= 0
    return probability
