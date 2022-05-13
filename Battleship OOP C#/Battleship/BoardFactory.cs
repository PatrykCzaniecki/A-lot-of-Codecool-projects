using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Battleship
{
    class BoardFactory
    {
        public void RandomPlacement(Board boardPlayer, int size)
        {
            Random random = new Random();
            int x;
            int y;
            List<string> directions = new List<string> {"v", "h"};

            while (boardPlayer.IsAnyShipPlacementPossible())
            {
                x = random.Next(0, size - 1);
                y = random.Next(0, size - 1);
                (int, int) position = (x, y);
                string direction = directions[random.Next(0, 2)];

                if (boardPlayer.IsShipTypePlacementPossible(Square.ShipType.Carrier))
                {
                    boardPlayer.placeShip(position, direction, Square.ShipType.Carrier);
                }
                else if (boardPlayer.IsShipTypePlacementPossible(Square.ShipType.Cruiser))
                {
                    boardPlayer.placeShip(position, direction, Square.ShipType.Cruiser);
                }
                else if (boardPlayer.IsShipTypePlacementPossible(Square.ShipType.Battleship))
                {
                    Console.WriteLine($"bug battleship, {x}, {y}");
                    boardPlayer.placeShip((x, y), direction, Square.ShipType.Battleship);
                }
                else if (boardPlayer.IsShipTypePlacementPossible(Square.ShipType.Submarine))
                {
                    Console.WriteLine($"bug submarine, {x}, {y}"); //bug na submarine v
                    boardPlayer.placeShip((x, y), direction, Square.ShipType.Submarine);
                }
                else if (boardPlayer.IsShipTypePlacementPossible(Square.ShipType.Destroyer))
                {
                    Console.WriteLine($"bug destroyer, {x}, {y}"); //bug destroyer v
                    boardPlayer.placeShip((x, y), direction, Square.ShipType.Destroyer);
                }
                else
                {
                    break;
                }
            }
        }

        public void ManualPlacement(Board board)
        {
            string coordinates = "";
            while (coordinates == "")
            {
                coordinates = Input.GetPlacementCoordinates();
            }

            (int, int) convertedCoordinates = (-1, -1);
            while (convertedCoordinates == (-1,-1))
            {
                convertedCoordinates = Input.ConvertToCoordinates(coordinates);
            }

            string orientation = "";
            while (orientation == "")
            {
                orientation = Input.GetOrientation();
            }

            Square.ShipType shipType = Square.ShipType.noSelected;
            while (!board.IsShipTypePlacementPossible(shipType))
            {
                shipType = Input.GetShipType();
            }
            board.placeShip(convertedCoordinates,orientation,shipType);
        }
    }
}
