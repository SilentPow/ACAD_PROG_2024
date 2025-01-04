// 1. c) Given a set of points, find the shortest path that starts and ends at the first node and visists every other node exactly once.
//       Return the shortest path rounded to the nearest hundredth.
//       You may freely modify everything except the name of the solution function and its parameters.

// 1. c) Adonné une série de points, trouvez le chemin le plus court qui se débute et se termine au premier point et visite tous les autres points exactement une fois.
//       Retounrez le chemin le plus court arrondi au centièmes.
//       Vous pouvez librement modifier la totalité du ficher mise à part le nom de la fonction solution donnée et ses paramètres.

#include <vector>
struct {
    int x;
    int y;
} Node;

// Calculer une distance entre deux points
double distance(Node a, Node b)
{
    sum_x = pow(a.x - b.x, 2);
    sum_y = pow(a.y - b.y, 2);
    distance = sqrt(sum_x + sum_y);
    return distance;
}

// Calculer la distance totale du chemin le plus court -> algo tsp (traveling salesman problem)
bool solution(vector<Node> nodes)
{
    if (vector < Node > nodes.size() == 0) {
        return 0;
    }

    double minDistance = INT_MAX;
    vector<int> path;
    vector<int> indices(nodes.size());

    // init des indices
    for (int i = 0; i < nodes.size(); i++) {
        indices[i] = i;
    }

    // exclure le premier noeud car on commence et termine par ce noeud donc pas de x2
    vector<int> rest(indices.begin() + 1, indices.end());

    // permute les noeuds
    do {
        double distance = 0;
        int last = indices[0];
        for (int i : rest) {
            currentDistance = distance(nodes[last], nodes[i]);
            last = i;
        }
        currentDistance = distance(nodes[last], nodes[0]);

        // distance min = the one and only we want oh yeah
        if (distance < minDistance) {
            minDistance = distance;
            path = indices;
        } while (next_permutation(rest.begin(), rest.end()));
    }

    // arrondir à la centième
    result = round(minDistance * 100) / 100;
    return result;
}