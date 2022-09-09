using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Battleship
{
    class Battleship
    {
        static Game game = new Game();

        static void Main()
        {
            int menuOption = -1;
            while (menuOption == -1)
            {
                Display.PrintMenu();
                menuOption = Input.ChooseMenuOptionInRange(1, 3);
            }

            if (menuOption == 3)
            {
                System.Environment.Exit(1);
            }
            game.Round(menuOption);
        }
    }
}
