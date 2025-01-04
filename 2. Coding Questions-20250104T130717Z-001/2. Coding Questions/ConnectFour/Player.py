import math
import copy

class Board:
    grid = []
    COLUMNS = 7
    HEIGHT = 6

class Player:
    def __init__(self, id):
        self.id = id
        self.otherId = None

        self.numMoves = 0
        self.isPlayerOne = False
        self.depthLimit = 5 

    def DoMove(self, board) -> int:
    
        if len(board.grid) != board.COLUMNS:
            print("Womp Womp")

        def IsPlayerOne(board):
            isPlayerOne = True
            otherId = None
            for i in range(len(board.grid)):
                if len(board.grid[i]) != 0:
                    isPlayerOne = False
                    otherId = board.grid[i][0]
            return isPlayerOne, otherId
        
        def GetOtherId(board):
            otherId = None
            for i in range(len(board.grid)):
                for j in range(len(board.grid[i])):
                    if board.grid[i][j] != self.id:
                        otherId = board.grid[i][j]
            return otherId

        if self.numMoves == 0:
            self.isPlayerOne, self.otherId = IsPlayerOne(board)
            print(self.isPlayerOne, self.otherId)
            print(self.numMoves)
        elif self.numMoves == 1 and self.otherId == None:
            self.otherId = GetOtherId(board)
            print(self.isPlayerOne, self.otherId)
            print(self.numMoves)

            
        def IsTerminal(board: Board):
            for i in range(len(board.grid)):
                for j in range(len(board.grid[i])):
                    try:
                        if board.grid[i][j]  == board.grid[i+1][j] == board.grid[i+2][j] == board.grid[i+3][j]:
                            return board.grid[i][j]
                    except IndexError:
                        pass

                    try:
                        if board.grid[i][j]  == board.grid[i][j+1] == board.grid[i][j+2] == board.grid[i][j+3]:
                            return board.grid[i][j]
                    except IndexError:
                        pass

                    try:
                        if not j + 3 > board.HEIGHT and board.grid[i][j] == board.grid[i+1][j + 1] == board.grid[i+2][j + 2] == board.grid[i+3][j + 3]:
                            return board.grid[i][j]
                    except IndexError:
                        pass

                    try:
                        if not j - 3 < 0 and board.grid[i][j] == board.grid[i+1][j - 1] == board.grid[i+2][j - 2] == board.grid[i+3][j - 3]:
                            return board.grid[i][j]
                    except IndexError:
                        pass
            return -1
        
        def heuristic(board: Board):
            heur = 0
            state = board.grid
            for i in range(len(board.grid)):
                for j in range(len(board.grid[i])):
                    # check horizontal streaks
                    try:
                        # add player one streak scores to heur
                        if state[i][j] == state[i + 1][j] == self.id:
                            heur += 10
                        if state[i][j] == state[i + 1][j] == state[i + 2][j] == self.id:
                            heur += 100
                        if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] == self.id:
                            heur += 10000

                        # subtract player two streak score to heur
                        if state[i][j] == state[i + 1][j] == self.otherId:
                            heur -= 10
                        if state[i][j] == state[i + 1][j] == state[i + 2][j] == self.otherId:
                            heur -= 100
                        if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] == self.otherId:
                            heur -= 10000
                    except IndexError:
                        pass

                    # check vertical streaks
                    try:
                        # add player one vertical streaks to heur
                        if state[i][j] == state[i][j + 1] == self.id:
                            heur += 10
                        if state[i][j] == state[i][j + 1] == state[i][j + 2] == self.id:
                            heur += 100
                        if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] == self.id:
                            heur += 10000

                        # subtract player two streaks from heur
                        if state[i][j] == state[i][j + 1] == self.otherId:
                            heur -= 10
                        if state[i][j] == state[i][j + 1] == state[i][j + 2] == self.otherId:
                            heur -= 100
                        if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] == self.otherId:
                            heur -= 10000
                    except IndexError:
                        pass

                    # check negative diagonal streaks
                    try:
                        # add  player one streaks
                        if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == self.id:
                            heur += 10
                        if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == self.id:
                            heur += 100
                        if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] \
                                == state[i+3][j - 3] == self.id:
                            heur += 10000

                        # subtract player two streaks
                        if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == self.otherId:
                            heur -= 10
                        if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == self.otherId:
                            heur -= 100
                        if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] \
                                == state[i+3][j - 3] == self.otherId:
                            heur -= 10000
                    except IndexError:
                        pass
            return heur


        def makeMove(board, i, player):
            if player:
                board[i].append(self.id)
            else:
                board[i].append(self.otherId)
            return board

        def Children(board, player):
            children = []
            for i in range(7):
                if len(board.grid[i]) < 6:
                    child = copy.deepcopy(board)
                    child.grid = copy.deepcopy(makeMove(copy.deepcopy(child.grid), i, player))
                    #print(child.grid)
                    children.append((i, child))
            return children

        def alphaBeta(board, depth, player, alpha, beta):
            if IsTerminal(board) == 0:
                return -math.inf if player else math.inf, -1
            elif depth == 0:
                return heuristic(board), -1

            if player:
                bestScore = -math.inf
                shouldReplace = lambda x: x > bestScore
            else:
                bestScore = math.inf
                shouldReplace = lambda x: x < bestScore

            #print(bestScore)
            bestMove = -1

            children = Children(copy.deepcopy(board), player)
            for child in children:
                move, childboard = child
                temp = alphaBeta(childboard, depth-1, not player, alpha, beta)[0]
                if shouldReplace(temp):
                    bestScore = temp
                    bestMove = move
                if player:
                    alpha = max(alpha, temp)
                else:
                    beta = min(beta, temp)
                if alpha >= beta:
                    break

            return bestScore, bestMove


        self.numMoves += 1
        score, move = alphaBeta(board, self.depthLimit, self.isPlayerOne, -math.inf, math.inf)
        return move
    
        # if board.grid[0][0] == self.id:
        #     return 0
        # else:
        #     return -1

if __name__ == '__main__':
    board = Board()
    for i in range(7):
        board.grid.append([])
    print(board.grid)
    player1 = Player("r")
    player2 = Player("b")

    player1.DoMove(board)
    board.grid[0].append("r")
    player2.DoMove(board)
    board.grid[0].append("b")
    player1.DoMove(board)
    print(board.grid)
    
