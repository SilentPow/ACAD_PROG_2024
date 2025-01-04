using System;

class Board 
{
    public List<List<char>> grid = [];
    public const int MAX_COLUMNS = 7;
    public const int HEIGHT = 6;
}

class Player(char id)
{
    public char id = id; // The reference character corresponding to your program. Each team has a different id.
    public int DoMove(Board board)
    {
        if (board.grid[0][0] == id)
            return 0;
        else
            return -1;
    }
}
