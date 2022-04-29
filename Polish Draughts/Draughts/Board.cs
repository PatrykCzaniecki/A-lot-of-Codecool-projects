namespace Draughts
{
    public class Board
    {
        public Pawn[,] Field { get; set; }

        public Board(int n)
        {
            Field = new Pawn[n, n];
            
            for (int x = 0; x < n; x++)
            {
                for (int y = 0; y < n; y++)
                {
                    if (x == n / 2 || x == n / 2 - 1)
                    {
                        Field[x, y] = new Pawn('.', x, y);
                    }
                    else if (x < n / 2)
                    {
                        if (x % 2 == 0 && y % 2 == 0 || x % 2 == 1 && y % 2 == 1)
                        {
                            Field[x, y] = new Pawn('x', x, y);
                        }
                        else
                        {
                            Field[x, y] = new Pawn('.', x, y);
                        }
                    }
                    else
                    {
                        if (x % 2 == 0 && y % 2 == 0 || x % 2 == 1 && y % 2 == 1)
                        {
                            Field[x, y] = new Pawn('o', x, y);
                        }
                        else
                        {
                            Field[x, y] = new Pawn('.', x, y);
                        }
                    }
                }
            }
        }

        public void DisplayBoard()
        {
            Console.Clear();
            char[] alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".ToCharArray();
            for (int x = 0; x < Field.GetLength(0) + 1; x++)
            {
                for (int y = 0; y < Field.GetLength(1) + 1; y++)
                {
                    if (x == 0 && y == 0)
                    {
                        Console.Write("  ");
                    }
                    if (x == 0 && y != 0)
                    {
                        Console.Write($"{alpha[y-1]} ");
                    }
                    if (y == 0 && x != 0)
                    {
                        if (x >= 10 && y == 0)
                        {
                            Console.Write($"{x}");
                        } 
                        else
                        {
                            Console.Write($"{x} ");
                        }
                    }
                    if (x != 0 && y != 0)
                    {
                        Console.Write($"{Field[x-1,y-1].Color} ");
                    }
                }
                Console.WriteLine();
            }
        }

        public void Move()
        {
            char player = 'o';
            while (WinGame() == false)
            {
                Console.WriteLine($"Select pawn {player}:");
                string cordinate = Console.ReadLine();
                int rowInt = Int32.Parse(cordinate.Substring(1)) - 1;
                int column = AlphaToInt(cordinate);
                while (Field[rowInt, column].Color != player)
                {
                    Console.WriteLine("Wrong coordinates choose :");
                    cordinate = Console.ReadLine();
                    rowInt = Int32.Parse(cordinate.Substring(1)) - 1;
                    column = AlphaToInt(cordinate);
                }
                if (AttackMove(rowInt, column, player) == false)
                {
                    if (player == 'o')
                    {
                        if (rowInt - 1 > 0 && column - 1 > 0)
                        {
                            if (Field[rowInt - 1, column - 1].Color == '.')
                            {
                                Field[rowInt - 1, column - 1].Color = 'M';
                            }
                        }
                        if (rowInt - 1 > 0 && column + 1 < Field.GetLength(1))
                        {
                            if (Field[rowInt - 1, column + 1].Color == '.')
                            {
                                Field[rowInt - 1, column + 1].Color = 'M';
                            }
                        }
                    }
                    else
                    {
                        if (rowInt + 1 < Field.GetLength(1) && column - 1 > 0)
                        {
                            if (Field[rowInt + 1, column - 1].Color == '.')
                            {
                                Field[rowInt + 1, column - 1].Color = 'M';
                            }
                        }
                        if (rowInt + 1 < Field.GetLength(1) && column + 1 < Field.GetLength(1))
                        {
                            if (Field[rowInt + 1, column + 1].Color == '.')
                            {
                                Field[rowInt + 1, column + 1].Color = 'M';
                            }
                        }
                    }
                    DisplayBoard();
                    Console.WriteLine("Choose move:");
                    string move = Console.ReadLine();
                    int moveRow = Int32.Parse(move.Substring(1)) - 1;
                    int moveColumn = AlphaToInt(move);
                    while (Field[moveRow, moveColumn].Color != 'M')
                    {
                        Console.WriteLine("Wrong coordinates choose :");
                        move = Console.ReadLine();
                        moveRow = Int32.Parse(cordinate.Substring(1)) - 1;
                        moveColumn = AlphaToInt(cordinate);
                    }
                    Field[moveRow, moveColumn].Color = player;
                    Field[rowInt, column].Color = '.';
                    RemoveMarker();
                    DisplayBoard();
                }
                else
                {
                    DisplayBoard();
                    Console.WriteLine("Choose move:");
                    string move = Console.ReadLine();
                    int moveRow = Int32.Parse(move.Substring(1)) - 1;
                    int moveColumn = AlphaToInt(move);
                    while (Field[moveRow, moveColumn].Color != 'M')
                    {
                        Console.Clear();
                        DisplayBoard();
                        Console.WriteLine("Wrong coordinates choose :");
                        move = Console.ReadLine();
                        moveRow = Int32.Parse(cordinate.Substring(1)) - 1;
                        moveColumn = AlphaToInt(cordinate);
                    }
                    Field[moveRow, moveColumn].Color = player;
                    Field[(moveRow + rowInt) / 2, (moveColumn + column) / 2].Color = '.';
                    Field[rowInt, column].Color = '.';
                    RemoveMarker();
                    DisplayBoard();
                }
                player = ChangePlayer(player);
            }
        }

        public bool AttackMove(int row, int col, char player)
        {
            char enemyPlayer = ChangePlayer(player);
            if (row - 1 > 0 && col - 1 > 0)
            {
                if (Field[row - 1, col - 1].Color == enemyPlayer && row - 2 > 0 && col - 2 > 0)
                {
                    if (Field[row - 2, col - 2].Color == '.')
                    {
                        Field[row - 2, col - 2].Color = 'M';
                    }
                }
            }
            if (row - 1 > 0 && col + 1 < Field.GetLength(1))
            {
                if (Field[row - 1, col + 1].Color == enemyPlayer && row - 2 > 0 && col + 2 < Field.GetLength(0))
                {
                    if (Field[row - 2, col + 2].Color == '.')
                    {
                        Field[row - 2, col + 2].Color = 'M';
                    }
                }
            }
            if (row + 1 < Field.GetLength(0) && col - 1 > 0)
            {
                if (Field[row + 1, col - 1].Color == enemyPlayer && row + 2 < Field.GetLength(0) && col - 2 > 0)
                {
                    if (Field[row + 2, col - 2].Color == '.')
                    {
                        Field[row + 2, col - 2].Color = 'M';
                    }
                }
            }
            if (row + 1 < Field.GetLength(0) && col + 1 < Field.GetLength(1))
            {
                if (Field[row + 1, col + 1].Color == enemyPlayer && row + 2 < Field.GetLength(0) &&
                    col + 2 < Field.GetLength(1))
                {
                    if (Field[row + 2, col + 2].Color == '.')
                    {
                        Field[row + 2, col + 2].Color = 'M';
                    }
                }
            }
            foreach (var celle in Field)
            {
                if (celle.Color == 'M')
                {
                    return true;
                }            
            }
            return false;
        }

        public bool WinGame()
        {
            int countX = 0;
            int countY = 0;
            foreach (var cell in Field)
            {
                if (cell.Color == 'x' )
                {
                    countX += 1;
                }
                else if (cell.Color == 'o')
                {
                    countY += 1;
                }

            }
            if (countY == 0)
            {
                Console.Clear();
                Console.WriteLine("Player X Win!");
                return true;
            } 
            if (countX == 0)
            {
                Console.Clear();
                Console.WriteLine("Player Y Win!");
                return true;
            }
            return false;
        }

        public char ChangePlayer(char player)
        {
            if (player == 'o')
            {
                return 'x';
            }
            return 'o';
        }

        public void RemoveMarker()
        {
            foreach (var cell in Field)
            {
                if (cell.Color == 'M')
                {
                    cell.Color = '.';
                }
            }
        }

        public int AlphaToInt(string position)
        {
            char rowChar = position[0];
            char[] alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".ToCharArray();
            for (int i = 0; i < alpha.Length; i++)
            {
                if (alpha[i] == rowChar)
                {
                    return i;
                }
            }
            return rowChar;
        }

    }
}