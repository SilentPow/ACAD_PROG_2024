# 1. b) Given a set of points, find the shortest path that starts and ends at the first node and visists every other node exactly once.
#       Return the shortest path rounded to the nearest hundredth.
#       You may freely modify everything except the name of the solution function and its parameters.

# 1. b) Donné une série de points, trouver le chemin le plus court qui se débute et se termine au premier point et visite tous les autres points exactement une fois.
#       Retounrez le chemin le plus court arrondi au centièmes.
#       Vous pouvez librement modifier la totalité du ficher mise à part le nom de la fonction solution donnée et ses paramètres.

def solution(*nodes):
    assert isinstance(nodes, list)
    assert isinstance(nodes[0], (int, int))
    return 0;