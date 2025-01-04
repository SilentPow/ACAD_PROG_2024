// 1. e) Given several dice of varying sizes, determine the average value when rolling all dice. 
//       The list of tuples dice is of the format xdy, where x is the number of dice and y is the size of the dice. For example, 2d6 is two six-sided dice.
//       You may freely modify everything except the name of solution function and its parameters.

// 1. e) Adonné plusieurs dés de tailles différentes, déterminez la valeur moyenne obtenue en roulant tous les dés.
//       La liste de tuples dice est du format xdy, où x est le nombre de dés et y est la tailles des dés. Par exemple, 2d6 représente deux dés à six faces.
//       Vous pouvez librement modifier la totalité du ficher mise à part le nom de la fonction solution donnée et ses paramètres.

// Go 1.23.2

package main

type dice struct {
	number int
	size   int
}

func solution(n int, dice ...dice) float32 {
	if dice[0].number <= 0 || dice[0].size <= 0 {
		panic("invalid die expression")
	}
	var probability float32 = 0.5
	if probability > 1 || probability < 0 {
		panic("probabilité invalide")
	}
	return probability
}
