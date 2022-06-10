using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Channels;
using System.Threading.Tasks;

namespace Battleship
{
    public class Ship
    {
        private List<Square> shipLocationList;
        public Ship(List<Square> shipLocationList)
        {
            this.shipLocationList = shipLocationList;
        }
    }
}
