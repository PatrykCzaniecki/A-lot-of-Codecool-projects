using System;
using System.Collections.Generic;
using System.Diagnostics.Metrics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Battleship
{
    class Game
    {
        Player player1 = new Player(1);
        Player player2 = new Player(2);
        Board boardPlayer1 = new Board(10);
        Board boardPlayer2 = new Board(10);
        
        private BoardFactory shipPlacement;
        private Player currentPlayer;
        private Input input;
        private Display display;

        private bool IsWinner(Player currentPlayer)
        {
            if (currentPlayer.PlayerNumber == 1)
            {
                return IsAllShipsSunked(boardPlayer2);
            }
            if (currentPlayer.PlayerNumber == 2)
            {
                return IsAllShipsSunked(boardPlayer1);
            }
            return false;
        }

        private static bool IsAllShipsSunked(Board board)
        {
            foreach (var square in board.ocean)
            {
                if (square.status == Square.SquareStatus.ship)
                {
                    return false;
                }
            }
            return true;
        }

        public void Round(int menuOption)
        {
            if (menuOption == 1)
            {
                string placement = ChoosePlacement();
                Console.Clear();
                if (placement == "manual")
                {
                    while (boardPlayer1.IsAnyShipPlacementPossible())
                    {
                        Display.PrintBoard(boardPlayer1);
                        Display.PrintPlacementInfo(boardPlayer1);
                        shipPlacement.ManualPlacement(boardPlayer1);
                        Console.Clear();
                    }

                    Console.WriteLine("BOARD 1");
                    Display.PrintBoard(boardPlayer1);
                    Display.PrintPlacementInfo(boardPlayer1);
                    Display.ChangeSeats();
                    Console.Clear();

                    while (boardPlayer2.IsAnyShipPlacementPossible())
                    {
                        Display.PrintBoard(boardPlayer2);
                        Display.PrintPlacementInfo(boardPlayer2);
                        shipPlacement.ManualPlacement(boardPlayer2);
                        Console.Clear();
                    }

                    Console.WriteLine("BOARD 2");
                    Display.PrintBoard(boardPlayer2);
                    Display.PrintPlacementInfo(boardPlayer2);
                    Display.ChangeSeats();
                    Console.Clear();
                }

                if (placement == "random")
                {
                    shipPlacement.RandomPlacement(boardPlayer1, 10);
                    Display.PrintBoard(boardPlayer1);
                    shipPlacement.RandomPlacement(boardPlayer2, 10);
                    Display.PrintBoard(boardPlayer2);
                }

                currentPlayer = player1;
                while (!IsWinner(currentPlayer))
                {
                    currentPlayer = player1;
                    PlayerMove();
                    if (!IsWinner(currentPlayer))
                    {
                        currentPlayer = player2;
                        PlayerMove();
                    }
                }
                PrintWinner();
            }
        }

        private void PrintWinner()
        {
            if (IsAllShipsSunked(boardPlayer1))
            {
                Display.PrintWinner(player2);
            }
            if (IsAllShipsSunked(boardPlayer2))
            {
                Display.PrintWinner(player1);
            }
        }

        private string ChoosePlacement()
        {
            int placement = -1;
            while (placement == -1)
            {
                Display.ChoosePlacement();
                placement = Input.ChooseMenuOptionInRange(1, 2);
            }
            if (placement == 1)
            {
                return "manual";
            }
            return "random";
        }

        private void PlayerMove()
        {
            bool missedShotTaken = false;
            while (!missedShotTaken && !IsWinner(currentPlayer))
            {
                if (currentPlayer.PlayerNumber == 1)
                {
                    Console.Clear();
                    Display.Shooting(boardPlayer1, boardPlayer2, currentPlayer);
                }
                if (currentPlayer.PlayerNumber == 2)
                {
                    Console.Clear();
                    Display.Shooting(boardPlayer2, boardPlayer1, currentPlayer);
                }
                string coordinates = "";
                while (coordinates == "")
                {
                    coordinates = Input.GetPlacementCoordinates();
                }

                (int, int) convertedCoordinates = (-1, -1);

                if (currentPlayer.PlayerNumber == 1)
                {
                    while (!IsValidShot(convertedCoordinates, boardPlayer2))
                    {
                        while (convertedCoordinates == (-1, -1))
                        {
                            convertedCoordinates = Input.ConvertToCoordinates(coordinates);
                        }
                    }
                }

                if (currentPlayer.PlayerNumber == 2)
                {
                    while (!IsValidShot(convertedCoordinates, boardPlayer1))
                    {
                        while (convertedCoordinates == (-1, -1))
                        {
                            convertedCoordinates = Input.ConvertToCoordinates(coordinates);
                        }
                    }
                }

                if (currentPlayer.PlayerNumber == 1)
                {
                    missedShotTaken = TakeShotAndReturnIfMissed(convertedCoordinates, currentPlayer, boardPlayer2);
                    Console.Clear();
                    Display.Shooting(boardPlayer1, boardPlayer2, currentPlayer);
                }

                if (currentPlayer.PlayerNumber == 2)
                {
                    missedShotTaken = TakeShotAndReturnIfMissed(convertedCoordinates, currentPlayer, boardPlayer1);
                    Console.Clear();
                    Display.Shooting(boardPlayer2, boardPlayer1, currentPlayer);
                }
            }

            if (!IsWinner(currentPlayer))
            {
                Display.ChangeSeats();
                Console.Clear();
            }
        }

        private bool IsValidShot((int x, int y) coord, Board board)
        {
            if (coord == (-1, -1))
            {
                return false;
            }
            if (board.ocean[coord.x, coord.y].status == Square.SquareStatus.empty)
            {
                return true;
            }
            if (board.ocean[coord.x, coord.y].status == Square.SquareStatus.ship)
            {
                return true;
            }
            return false;
        }

        private bool TakeShotAndReturnIfMissed((int x, int y) coord, Player currentPlayer, Board board)
        {
            if (board.ocean[coord.x, coord.y].status == Square.SquareStatus.ship)
            {
                board.ocean[coord.x, coord.y].status = Square.SquareStatus.hit;
                int counter = 0;
                foreach (var ship in board.ocean[coord.x, coord.y].shipFragments)
                {
                    if (ship.status == Square.SquareStatus.hit)
                    {
                        counter++;
                    }
                }

                if (board.ocean[coord.x, coord.y].shipFragments.Count == counter)
                {
                    foreach (var ship in board.ocean[coord.x, coord.y].shipFragments)
                    {
                        ship.status = Square.SquareStatus.sunk;
                    }
                    return false;
                }
                else
                {
                    board.ocean[coord.x, coord.y].status = Square.SquareStatus.hit;
                    return false;
                }
            }

            if (board.ocean[coord.x, coord.y].status == Square.SquareStatus.empty)
            {
                board.ocean[coord.x, coord.y].status = Square.SquareStatus.missed;
                return true;
            }
            return false;
        }

        public Game()
        {
            shipPlacement = new BoardFactory();
        }
    }
}
