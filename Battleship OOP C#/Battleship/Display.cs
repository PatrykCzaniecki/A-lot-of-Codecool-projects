using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Battleship
{
    class Display
    {
        public static void PrintMenu()
        {
            Console.WriteLine("Welcome to Battleship War Game!");
            Console.WriteLine("");
            Console.WriteLine("");
            Console.WriteLine("1. New Game (Player vs Player)");
            Console.WriteLine("2. New Game (Player vs Ai) * coming soon *");
            Console.WriteLine("3. Quit");
            Console.WriteLine("");
            Console.WriteLine("");
            Console.WriteLine("(Insert 1 or 2 or 3 for continue..)");
        }

        public static void PrintBoard(Board board)
        {
            string numbers = " ";
            string lettersAJ = "ABCDEFGHIJ";

            for (int i = 1; i <= board.Size; i++)
            {
                numbers += " " + i.ToString();
            }

            Console.WriteLine(numbers);

            for (int i = 0; i < board.Size; i++)
            {
                Console.Write(lettersAJ[i] + " ");
                for (int j = 0; j < board.Size; j++)
                {
                    Console.Write(board.ocean[i, j].GetCharacter() + " ");
                }
                Console.Write("\n");
            }
        }

        public static void PrintWinner(Player winner)
        {
            Console.WriteLine($"WINNER IS PLAYER {winner.PlayerNumber}");
        }

        public static void ChoosePlacement()
        {
            Console.WriteLine("Choose placement method!");
            Console.WriteLine("1. Manual");
            Console.WriteLine("2. Random");
            Console.WriteLine("");
        }

        public static void Orientation()
        {
            Console.WriteLine("Type orientation: ");
            Console.WriteLine("(V) - Vertical");
            Console.WriteLine("(H) - Horizontal");
        }

        public static void ShipTypes()
        {
            Console.WriteLine("Choose ship type: ");
            Console.WriteLine("1. Carrier ( length = 1 )");
            Console.WriteLine("2. Cruiser ( length = 2 )");
            Console.WriteLine("3. Battleship ( length = 3 )");
            Console.WriteLine("4. Submarine ( length = 4 )");
            Console.WriteLine("5. Destroyer ( length = 5 )");
        }

        public static void PrintPlacementInfo(Board boardPlayer1)
        {
            Console.Write("Carrier to place (1 square): ");
            Console.Write($"[ {boardPlayer1.CarrierToPlace} ]");
            Console.Write("\n");
            Console.Write("Cruiser to place (2 square): ");
            Console.Write($"[ {boardPlayer1.CruiserToPlace} ]");
            Console.Write("\n");
            Console.Write("Battleship to place (3 square): ");
            Console.Write($"[ {boardPlayer1.BattleshipToPlace} ]");
            Console.Write("\n");
            Console.Write("Submarine to place (4 square): ");
            Console.Write($"[ {boardPlayer1.SubmarineToPlace} ]");
            Console.Write("\n");
            Console.Write("Destroyer to place (5 square): ");
            Console.Write($"[ {boardPlayer1.DestroyerToPlace} ]");
            Console.Write("\n");
        }

        public static void ChangeSeats()
        {
            Console.WriteLine("Change seats time for next player. Press enter to continue...");
            Console.ReadLine();
        }

        public static void Shooting(Board visibleBoard, Board hiddenBoard, Player currentPlayer)
        {
            Console.WriteLine($"Player {currentPlayer.PlayerNumber} turn...");
            Console.WriteLine("YOUR BOARD:");
            Display.PrintBoard(visibleBoard);
            Console.WriteLine("ENEMY BOARD:");
            Display.PrintHiddenBoard(hiddenBoard);
        }

        private static void PrintHiddenBoard(Board board)
        {
            string numbers = " ";
            string lettersAJ = "ABCDEFGHIJ";

            for (int i = 1; i <= board.Size; i++)
            {
                numbers += " " + i.ToString();
            }

            Console.WriteLine(numbers);

            for (int i = 0; i < board.Size; i++)
            {
                Console.Write(lettersAJ[i] + " ");
                for (int j = 0; j < board.Size; j++)
                {
                    if (board.ocean[i, j].GetCharacter() == "S")
                    {
                        Console.Write("~" + " ");
                    }
                    else
                    {
                        Console.Write(board.ocean[i, j].GetCharacter() + " ");
                    }
                }
                Console.Write("\n");
            }
        }
    }
}
