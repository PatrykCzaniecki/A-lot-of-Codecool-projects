using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Battleship
{
    public class Square
    {
        public (int, int) position;
        public SquareStatus status;
        public ShipType shiptype;

        public List<Square> shipFragments = new List<Square>();

        public string GetCharacter()
        {
            if (status == SquareStatus.ship)
            {
                return "S";
            }

            if (status == SquareStatus.sunk)
            {
                return "X";
            }

            if (status == SquareStatus.hit)
            {
                return "H";
            }

            if (status == SquareStatus.missed)
            {
                return "M";
            }
            
            else
            {
                return "~";
            }
        }

        public Square(SquareStatus status, int x, int y)
        {
            this.status = status;
            position = (x, y);
        }

        public enum SquareStatus
        {
            empty, ship, hit, missed, sunk
        }

        public enum ShipType
        {
            Carrier = 1,
            Cruiser = 2,
            Battleship = 3,
            Submarine = 4,
            Destroyer = 5,
            noSelected = -1,
        }
    }
}
