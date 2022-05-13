using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Battleship
{
    class Player
    {
        List<Ship> shipList;
        private int playerNumber;

        public int PlayerNumber
        {
            get { return playerNumber; } 
            
            set { playerNumber = value; }
        }

        public Player(int playerNumber)
        {
            this.PlayerNumber = playerNumber;
        }
    }
}
