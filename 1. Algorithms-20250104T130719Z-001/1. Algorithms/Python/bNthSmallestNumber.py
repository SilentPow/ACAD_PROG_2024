# 1. b) Return the nth smallest integer in a given unsorted list. 0 < n < len(numbers).
#       You may freely modify everything except the name of the solution function and its parameters.

# 1. a) Retournez le n-ieme nombre entier dans une liste non-classée. 0 < n < len(numbers). 
#       Vous pouvez librement modifier la totalité du ficher mise à part le nom de la fonction solution donnée et ses paramètres.


def solution(n, *numbers):
    assert isinstance(n, int)
    assert (numbers, int)
    i = numbers[n]
    return i
