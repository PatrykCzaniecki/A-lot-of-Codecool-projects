using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace Battleship
{
    class Board
    {
        public Square[,] ocean;
        public int Size;

        public Square[,] Ocean
        {
            get { return ocean; }
        }

        public Board(int Size)
        {
            ocean = new Square[Size, Size];
            this.Size = Size;
            InitializeBoard();
        }

        private int carrierToPlace = 1;
        private int cruiserToPlace = 1;
        private int battleshipToPlace = 1;
        private int submarineToPlace = 1;
        private int destroyerToPlace = 1;

        public int CarrierToPlace
        {
            get { return carrierToPlace; }
        }
        public int CruiserToPlace
        {
            get { return cruiserToPlace; }
        }

        public int BattleshipToPlace
        {
            get { return battleshipToPlace; }
        }

        public int SubmarineToPlace
        {
            get { return submarineToPlace; }
        }

        public int DestroyerToPlace
        {
            get { return destroyerToPlace; }
        }

        public void updateShipToPlace(Square.ShipType type)
        {
            switch (type)
            {
                case Square.ShipType.Carrier:
                    carrierToPlace--;
                    break;
                case Square.ShipType.Cruiser:
                    cruiserToPlace--;
                    break;
                case Square.ShipType.Battleship:
                    battleshipToPlace--;
                    break;
                case Square.ShipType.Submarine:
                    submarineToPlace--;
                    break;
                default:
                    destroyerToPlace--;
                    break;
            }
        }

        public bool IsAnyShipPlacementPossible()
        {
            if (cruiserToPlace > 0 || carrierToPlace > 0 || battleshipToPlace > 0 || submarineToPlace > 0 ||
                destroyerToPlace > 0)
            {
                return true;
            }
            return false;
        }

        public bool IsShipTypePlacementPossible(Square.ShipType type)
        {
            switch (type)
            {
                case Square.ShipType.Carrier:
                    if (carrierToPlace == 0)
                        Console.WriteLine($"You cannot place ship {type}");
                    return carrierToPlace > 0;
                case Square.ShipType.Cruiser:
                    if (cruiserToPlace == 0)
                        Console.WriteLine($"You cannot place ship {type}");
                    return cruiserToPlace > 0;
                case Square.ShipType.Battleship:
                    if (battleshipToPlace == 0)
                        Console.WriteLine($"You cannot place ship {type}");
                    return battleshipToPlace > 0;
                case Square.ShipType.Submarine:
                    if (submarineToPlace == 0)
                        Console.WriteLine($"You cannot place ship {type}");
                    return submarineToPlace > 0;
                case Square.ShipType.Destroyer:
                    if (destroyerToPlace == 0)
                        Console.WriteLine($"You cannot place ship {type}");
                    return destroyerToPlace > 0;
                default:
                    return false;
            }
        }

        public void InitializeBoard()
        {
            for (int i = 0; i < Size; i++)
            {
                for (int j = 0; j < Size; j++)
                {
                    ocean[i, j] = new Square(Square.SquareStatus.empty, i, j);
                }
            }
        }

        public bool IsPlacementOk((int x, int y) position, string direction, Square.ShipType shipType)
        {
            int y = position.Item1;
            int x = position.Item2;
            direction = direction.ToUpper();

            switch (shipType)
            {
                case Square.ShipType.Carrier:
                    if (checkCarrierPlacement(x, y))
                    {
                        return true;
                    }
                    break;
                case Square.ShipType.Cruiser:
                    if (checkCruiserPlacement(x, y, direction))
                    {
                        return true;
                    }
                    break;
                case Square.ShipType.Battleship:
                    if (checkBattleshipPlacement(x,y, direction))
                    {
                        return true;
                    }
                    break;
                case Square.ShipType.Submarine:
                    if (checkSubmarinePlacement(x, y, direction))
                    {
                        return true;
                    }
                    break;
                case Square.ShipType.Destroyer:
                    if (checkDestroyerPlacement(x, y, direction))
                    {
                        return true;
                    }
                    break;
            }
            return false;
        }

        public bool checkCarrierPlacement(int x, int y)
        {
            if ((isIndexInRange(x, y) && isSquareAvailable(x, y)) &&
                (isSquareNearAvailable(x - 1, y)) &&
                (isSquareNearAvailable(x + 1, y)) &&
                (isSquareNearAvailable(x, y + 1)) &&
                (isSquareNearAvailable(x, y - 1)))
            {
                return true;
            }
            return false;
        }

        public bool checkCruiserPlacement(int x, int y, string direction)
        {
            if (direction == "H")
            {
                if ((isIndexInRange(x, y) && isSquareAvailable(x, y)) &&
                    (isIndexInRange(x + 1, y) && isSquareAvailable(x + 1, y)) &&
                    isSquareNearAvailable(x - 1, y) &&
                    isSquareNearAvailable(x + 2, y) &&
                    isSquareNearAvailable(x, y + 1) &&
                    isSquareNearAvailable(x, y - 1) &&
                    isSquareNearAvailable(x + 1, y + 1) &&
                    isSquareNearAvailable(x + 1, y - 1))
                {
                    return true;
                }
            }
            else if (direction == "V")
            {
                if ((isIndexInRange(x, y) && isSquareAvailable(x, y)) &&
                    (isIndexInRange(x, y + 1) && isSquareAvailable(x, y + 1)) &&
                    isSquareNearAvailable(x, y + 2) &&
                    isSquareNearAvailable(x + 1, y + 1) &&
                    isSquareNearAvailable(x - 1, y + 1) &&
                    isSquareNearAvailable(x - 1, y) &&
                    isSquareNearAvailable(x + 1, y) &&
                    isSquareNearAvailable(x, y - 1))
                {
                    return true;
                }
            }
            return false;
        }

        public bool checkBattleshipPlacement(int x, int y, string direction)
        {
            if (direction == "H")
            {
                if (!isIndexInRange(x, y))
                {
                    return false;
                }
                if (!isIndexInRange(x + 1, y))
                {
                    return false;
                }
                if (!isIndexInRange(x + 2, y))
                {
                    return false;
                }
                if ((isIndexInRange(x, y) && isSquareAvailable(x, y)) &&
                    (isIndexInRange(x + 1, y) && isSquareAvailable(x + 1, y)) &&
                    (isIndexInRange(x + 2, y) && isSquareAvailable(x + 2, y)) &&
                    isSquareNearAvailable(x - 1, y) &&
                    isSquareNearAvailable(x + 3, y) &&
                    isSquareNearAvailable(x, y + 1) &&
                    isSquareNearAvailable(x + 1, y + 1) &&
                    isSquareNearAvailable(x + 2, y + 1) &&
                    isSquareNearAvailable(x, y - 1) &&
                    isSquareNearAvailable(x + 1, y - 1) &&
                    isSquareNearAvailable(x + 2, y - 1))
                {
                    return true;
                }
            }
            else if (direction == "V")
            {
                if (!isIndexInRange(x, y))
                {
                    return false;
                }
                if (!isIndexInRange(x, y + 1))
                {
                    return false;
                }
                if (!isIndexInRange(x, y + 2))
                {
                    return false;
                }

                if ((isIndexInRange(x, y) && isSquareAvailable(x, y)) &&
                    (isIndexInRange(x, y - 1) && isSquareAvailable(x, y - 1)) &&
                    (isIndexInRange(x, y - 2) && isSquareAvailable(x, y - 2)) &&
                    isSquareNearAvailable(x, y - 3) &&
                    isSquareNearAvailable(x - 1, y) &&
                    isSquareNearAvailable(x + 1, y) &&
                    isSquareNearAvailable(x + 1, y - 1) &&
                    isSquareNearAvailable(x - 1, y - 1) &&
                    isSquareNearAvailable(x + 1, y - 2) &&
                    isSquareNearAvailable(x - 1, y - 2) &&
                    isSquareNearAvailable(x, y + 1))
                {
                    return true;
                }
            }
            return false;
        }

        public bool checkSubmarinePlacement(int x, int y, string direction)
        {
            if (direction == "H")
            {
                if ((isIndexInRange(x, y) && isSquareAvailable(x, y)) &&
                    (isIndexInRange(x + 1, y) && isSquareAvailable(x + 1, y)) &&
                    (isIndexInRange(x + 2, y) && isSquareAvailable(x + 2, y)) &&
                    (isIndexInRange(x + 3, y) && isSquareAvailable(x + 3, y)) &&
                    isSquareNearAvailable(x - 1, y) &&
                    isSquareNearAvailable(x + 4, y) &&
                    isSquareNearAvailable(x, y + 1) &&
                    isSquareNearAvailable(x + 1, y + 1) &&
                    isSquareNearAvailable(x + 2, y + 1) &&
                    isSquareNearAvailable(x + 3, y + 1) &&
                    isSquareNearAvailable(x, y - 1) &&
                    isSquareNearAvailable(x + 1, y - 1) &&
                    isSquareNearAvailable(x + 2, y - 1) &&
                    isSquareNearAvailable(x + 3, y - 1))
                {
                        return true;
                }
            } else if (direction == "V")
            {
                if ((isIndexInRange(x, y) && isSquareAvailable(x, y)) &&
                    (isIndexInRange(x, y + 1) && isSquareAvailable(x, y + 1)) &&
                    (isIndexInRange(x, y + 2) && isSquareAvailable(x, y + 2)) &&
                    (isIndexInRange(x, y + 3) && isSquareAvailable(x, y + 3)) &&
                    isSquareNearAvailable(x-1, y) &&
                    isSquareNearAvailable(x, y-1) &&
                    isSquareNearAvailable(x-1, y + 1) &&
                    isSquareNearAvailable(x - 1, y + 2) &&
                    isSquareNearAvailable(x - 1, y + 3) &&
                    isSquareNearAvailable(x, y + 4) &&
                    isSquareNearAvailable(x + 1, y) &&
                    isSquareNearAvailable(x + 1, y+1) &&
                    isSquareNearAvailable(x + 1, y + 2) &&
                    isSquareNearAvailable(x + 1, y + 3))
                {
                    return true;
                }
            }
            return false;
        }

        public bool checkDestroyerPlacement(int x, int y, string direction)
        {
            if (direction == "H")
            {
                if ((isIndexInRange(x, y) && isSquareAvailable(x, y)) &&
                    (isIndexInRange(x + 1, y) && isSquareAvailable(x + 1, y)) &&
                    (isIndexInRange(x + 2, y) && isSquareAvailable(x + 2, y)) &&
                    (isIndexInRange(x + 3, y) && isSquareAvailable(x + 3, y)) &&
                    (isIndexInRange(x + 4, y) && isSquareAvailable(x + 4, y)) &&
                    isSquareNearAvailable(x - 1, y) &&
                    isSquareNearAvailable(x + 5, y) &&
                    isSquareNearAvailable(x, y + 1) &&
                    isSquareNearAvailable(x + 1, y + 1) &&
                    isSquareNearAvailable(x + 2, y + 1) &&
                    isSquareNearAvailable(x + 3, y + 1) &&
                    isSquareNearAvailable(x + 4, y + 1) &&
                    isSquareNearAvailable(x, y - 1) &&
                    isSquareNearAvailable(x + 1, y - 1) &&
                    isSquareNearAvailable(x + 2, y - 1) &&
                    isSquareNearAvailable(x + 3, y - 1) &&
                    isSquareNearAvailable(x + 4, y - 1))
                {
                    return true;
                }
            }
            else if (direction == "V")
            {
                if (!isIndexInRange(x, y))
                {
                    return false;
                }
                if (!isIndexInRange(x, y + 1))
                {
                    return false;
                }
                if (!isIndexInRange(x, y + 2))
                {
                    return false;}
                if (!isIndexInRange(x, y + 3))
                {
                    return false;
                }
                if (!isIndexInRange(x, y + 4))
                {
                    return false;
                }
                
                if ((isIndexInRange(x, y) && isSquareAvailable(x, y)) &&
                    (isIndexInRange(x, y + 1) && isSquareAvailable(x, y + 1)) &&
                    (isIndexInRange(x, y + 2) && isSquareAvailable(x, y + 2)) &&
                    (isIndexInRange(x, y + 3) && isSquareAvailable(x, y + 3)) &&
                    (isIndexInRange(x, y + 4) && isSquareAvailable(x, y + 4)) &&
                    isSquareNearAvailable(x, y - 1) &&
                    isSquareNearAvailable(x + 1, y) &&
                    isSquareNearAvailable(x - 1, y) &&
                    isSquareNearAvailable(x + 1, y + 1) &&
                    isSquareNearAvailable(x - 1, y + 1) &&
                    isSquareNearAvailable(x - 1, y + 2) &&
                    isSquareNearAvailable(x + 1, y + 2) &&
                    isSquareNearAvailable(x - 1, y + 3) &&
                    isSquareNearAvailable(x + 1, y + 3) &&
                    isSquareNearAvailable(x - 1, y + 4) &&
                    isSquareNearAvailable(x + 1, y + 4) &&
                    isSquareNearAvailable(x, y + 5))
                {
                    return true;
                }
            }
            return false;
        }

        public bool isSquareAvailable(int y, int x)
        {
            if (ocean[x, y].status == Square.SquareStatus.empty)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        public bool isSquareNearAvailable(int y, int x)
        {
            if (isIndexInRange(x, y) == false)
            {
                return true;
            }
            if (ocean[x, y].status == Square.SquareStatus.empty)
            {
                return true;
            }
            return false;
        }

        public bool isIndexInRange(int x, int y)
        {
            if ((Size <= x || Size <= y) || (x < 0 || y < 0))
            {
                return false;
            }
            return true;
        }

        public void placeShip((int, int) position, string direction, Square.ShipType shipType)
        {
            if (IsPlacementOk(position, direction, shipType))
            {
                placeSquaresOnBoard(position, direction, shipType);
            }
        }

        private void placeSquaresOnBoard((int x, int y) position, string direction, Square.ShipType shipType)
        {
            direction = direction.ToUpper();
            if (shipType == Square.ShipType.Carrier)
            {
                placeShipOnPosition(position.x, position.y, shipType);
                ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y]);
                updateShipToPlace(shipType);
            }

            if (shipType == Square.ShipType.Cruiser)
            {
                if (direction.ToUpper() == "V")
                {
                    placeShipOnPosition(position.x, position.y, shipType);
                    placeShipOnPosition(position.x+1, position.y, shipType);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x + 1, position.y]);
                    ocean[position.x+1, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x+1, position.y].shipFragments.Add(ocean[position.x + 1, position.y]);
                    updateShipToPlace(shipType);
                }

                if (direction.ToUpper() == "H")
                {
                    placeShipOnPosition(position.x, position.y, shipType);
                    placeShipOnPosition(position.x, position.y+1, shipType);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y + 1]);
                    ocean[position.x, position.y+1].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y+1].shipFragments.Add(ocean[position.x, position.y + 1]);
                    updateShipToPlace(shipType);
                }
            }

            if (shipType == Square.ShipType.Battleship)
            {
                if (direction.ToUpper() == "V")
                {
                    placeShipOnPosition(position.x, position.y, shipType);
                    placeShipOnPosition(position.x + 1, position.y, shipType);
                    placeShipOnPosition(position.x + 2, position.y, shipType);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x + 1, position.y]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x + 2, position.y]);
                    ocean[position.x+1, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x+1, position.y].shipFragments.Add(ocean[position.x + 1, position.y]);
                    ocean[position.x+1, position.y].shipFragments.Add(ocean[position.x + 2, position.y]);
                    ocean[position.x + 2, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x + 2, position.y].shipFragments.Add(ocean[position.x + 1, position.y]);
                    ocean[position.x + 2, position.y].shipFragments.Add(ocean[position.x + 2, position.y]);
                    updateShipToPlace(shipType);
                }

                if (direction.ToUpper() == "H")
                {
                    placeShipOnPosition(position.x, position.y, shipType);
                    placeShipOnPosition(position.x, position.y + 1, shipType);
                    placeShipOnPosition(position.x, position.y + 2, shipType);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y + 1]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y + 2]);
                    ocean[position.x, position.y+1].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y+1].shipFragments.Add(ocean[position.x, position.y + 1]);
                    ocean[position.x, position.y+1].shipFragments.Add(ocean[position.x, position.y + 2]);
                    ocean[position.x, position.y + 2].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y + 2].shipFragments.Add(ocean[position.x, position.y + 1]);
                    ocean[position.x, position.y +2].shipFragments.Add(ocean[position.x, position.y + 2]);
                    updateShipToPlace(shipType);
                }
            }

            if (shipType == Square.ShipType.Submarine)
            {
                if (direction.ToUpper() == "V")
                {
                    placeShipOnPosition(position.x, position.y, shipType);
                    placeShipOnPosition(position.x + 1, position.y, shipType);
                    placeShipOnPosition(position.x + 2, position.y, shipType);
                    placeShipOnPosition(position.x + 3, position.y, shipType);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x + 1, position.y]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x + 2, position.y]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x + 3, position.y]);
                    ocean[position.x+1, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x+1, position.y].shipFragments.Add(ocean[position.x + 1, position.y]);
                    ocean[position.x+1, position.y].shipFragments.Add(ocean[position.x + 2, position.y]);
                    ocean[position.x+1, position.y].shipFragments.Add(ocean[position.x + 3, position.y]);
                    ocean[position.x + 2, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x + 2, position.y].shipFragments.Add(ocean[position.x + 1, position.y]);
                    ocean[position.x + 2, position.y].shipFragments.Add(ocean[position.x + 2, position.y]);
                    ocean[position.x + 2, position.y].shipFragments.Add(ocean[position.x + 3, position.y]);
                    ocean[position.x + 3, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x + 3, position.y].shipFragments.Add(ocean[position.x + 1, position.y]);
                    ocean[position.x + 3, position.y].shipFragments.Add(ocean[position.x + 2, position.y]);
                    ocean[position.x + 3, position.y].shipFragments.Add(ocean[position.x + 3, position.y]);
                    updateShipToPlace(shipType);
                }

                if (direction.ToUpper() == "H")
                {
                    placeShipOnPosition(position.x, position.y, shipType);
                    placeShipOnPosition(position.x, position.y + 1, shipType);
                    placeShipOnPosition(position.x, position.y + 2, shipType);
                    placeShipOnPosition(position.x, position.y + 3, shipType);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y +1]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y +2]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y +3]);
                    ocean[position.x, position.y+1].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y+1].shipFragments.Add(ocean[position.x, position.y + 1]);
                    ocean[position.x, position.y+1].shipFragments.Add(ocean[position.x, position.y + 2]);
                    ocean[position.x, position.y+1].shipFragments.Add(ocean[position.x, position.y + 3]);
                    ocean[position.x, position.y + 2].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y + 2].shipFragments.Add(ocean[position.x, position.y + 1]);
                    ocean[position.x, position.y + 2].shipFragments.Add(ocean[position.x, position.y + 2]);
                    ocean[position.x, position.y + 2].shipFragments.Add(ocean[position.x, position.y + 3]);
                    ocean[position.x, position.y + 3].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y + 3].shipFragments.Add(ocean[position.x, position.y + 1]);
                    ocean[position.x, position.y + 3].shipFragments.Add(ocean[position.x, position.y + 2]);
                    ocean[position.x, position.y + 3].shipFragments.Add(ocean[position.x, position.y + 3]);
                    updateShipToPlace(shipType);
                }
            }

            if (shipType == Square.ShipType.Destroyer)
            {
                if (direction.ToUpper() == "V")
                {
                    placeShipOnPosition(position.x, position.y, shipType);
                    placeShipOnPosition(position.x + 1, position.y, shipType);
                    placeShipOnPosition(position.x + 2, position.y, shipType);
                    placeShipOnPosition(position.x + 3, position.y, shipType);
                    placeShipOnPosition(position.x + 4, position.y, shipType);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x+1, position.y]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x+2, position.y]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x+3, position.y]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x+4, position.y]);
                    ocean[position.x+1, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x+1, position.y].shipFragments.Add(ocean[position.x + 1, position.y]);
                    ocean[position.x+1, position.y].shipFragments.Add(ocean[position.x + 2, position.y]);
                    ocean[position.x+1, position.y].shipFragments.Add(ocean[position.x + 3, position.y]);
                    ocean[position.x+1, position.y].shipFragments.Add(ocean[position.x + 4, position.y]);
                    ocean[position.x + 2, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x + 2, position.y].shipFragments.Add(ocean[position.x + 1, position.y]);
                    ocean[position.x + 2, position.y].shipFragments.Add(ocean[position.x + 2, position.y]);
                    ocean[position.x + 2, position.y].shipFragments.Add(ocean[position.x + 3, position.y]);
                    ocean[position.x + 2, position.y].shipFragments.Add(ocean[position.x + 4, position.y]);
                    ocean[position.x + 3, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x + 3, position.y].shipFragments.Add(ocean[position.x + 1, position.y]);
                    ocean[position.x + 3, position.y].shipFragments.Add(ocean[position.x + 2, position.y]);
                    ocean[position.x + 3, position.y].shipFragments.Add(ocean[position.x + 3, position.y]);
                    ocean[position.x + 3, position.y].shipFragments.Add(ocean[position.x + 4, position.y]);
                    ocean[position.x + 4, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x + 4, position.y].shipFragments.Add(ocean[position.x + 1, position.y]);
                    ocean[position.x + 4, position.y].shipFragments.Add(ocean[position.x + 2, position.y]);
                    ocean[position.x + 4, position.y].shipFragments.Add(ocean[position.x + 3, position.y]);
                    ocean[position.x + 4, position.y].shipFragments.Add(ocean[position.x + 4, position.y]);
                    updateShipToPlace(shipType);
                }

                if (direction.ToUpper() == "H")
                {
                    placeShipOnPosition(position.x, position.y, shipType);
                    placeShipOnPosition(position.x, position.y + 1, shipType);
                    placeShipOnPosition(position.x, position.y + 2, shipType);
                    placeShipOnPosition(position.x, position.y + 3, shipType);
                    placeShipOnPosition(position.x, position.y + 4, shipType);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y+1]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y+2]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y+3]);
                    ocean[position.x, position.y].shipFragments.Add(ocean[position.x, position.y+4]);
                    ocean[position.x, position.y+1].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y+1].shipFragments.Add(ocean[position.x, position.y + 1]);
                    ocean[position.x, position.y+1].shipFragments.Add(ocean[position.x, position.y + 2]);
                    ocean[position.x, position.y+1].shipFragments.Add(ocean[position.x, position.y + 3]);
                    ocean[position.x, position.y+1].shipFragments.Add(ocean[position.x, position.y + 4]);
                    ocean[position.x, position.y + 2].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y + 2].shipFragments.Add(ocean[position.x, position.y + 1]);
                    ocean[position.x, position.y + 2].shipFragments.Add(ocean[position.x, position.y + 2]);
                    ocean[position.x, position.y + 2].shipFragments.Add(ocean[position.x, position.y + 3]);
                    ocean[position.x, position.y + 2].shipFragments.Add(ocean[position.x, position.y + 4]);
                    ocean[position.x, position.y + 3].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y + 3].shipFragments.Add(ocean[position.x, position.y + 1]);
                    ocean[position.x, position.y + 3].shipFragments.Add(ocean[position.x, position.y + 2]);
                    ocean[position.x, position.y + 3].shipFragments.Add(ocean[position.x, position.y + 3]);
                    ocean[position.x, position.y + 3].shipFragments.Add(ocean[position.x, position.y + 4]);
                    ocean[position.x, position.y + 4].shipFragments.Add(ocean[position.x, position.y]);
                    ocean[position.x, position.y + 4].shipFragments.Add(ocean[position.x, position.y + 1]);
                    ocean[position.x, position.y + 4].shipFragments.Add(ocean[position.x, position.y + 2]);
                    ocean[position.x, position.y + 4].shipFragments.Add(ocean[position.x, position.y + 3]);
                    ocean[position.x, position.y + 4].shipFragments.Add(ocean[position.x, position.y + 4]);
                    updateShipToPlace(shipType);
                }
            }
        }

        private void placeShipOnPosition(int x, int y, Square.ShipType shipType)
        {
            ocean[x, y].shiptype = shipType;
            ocean[x, y].status = Square.SquareStatus.ship;
        }
    }
}
