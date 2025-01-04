# 1. g) Given a list of treasures with varying weights and values, determine the highest value possible within a given total weight limit.
#       Objects are given in the format (x, y) where x is the weight and y is the value.
#       You may freely modify everything except the name of solution function and its parameters.

# 1. g) Déterminez la plus grande valeure possible étant donné une liste de trésors de valeurs et de pids différents, avec une limite de poids total.
#       Les trésors dans treasures sont du format (x, y) où x est le poids et y est la valeure.
#       Vous pouvez librement modifier la totalité du ficher mise à part le nom de la fonction solution donnée et ses paramètres.



def solution(*treasures, weightLimit):
    assert isinstance(treasures[0], (int, int))
    assert isinstance(weightLimit, int)
    
    value = treasures[0][1]
    weight = treasures[0][0]

    if weight <= weightLimit:
        return value
    else:
        return 0

