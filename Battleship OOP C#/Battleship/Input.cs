using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata;
using System.Text;
using System.Threading.Tasks;

namespace Battleship
{
    class Input
    {
        private string move = "";

        public static int ChooseMenuOptionInRange(int min, int max)
        {
            Console.Write("Choose option: ");
            string user_input = Console.ReadLine();
            if (int.TryParse(user_input, out int result))
            {
                if (int.Parse(user_input) >= min && int.Parse(user_input) <= max)
                {
                    return int.Parse(user_input);
                }
                else
                {
                    Console.WriteLine($"Input is not in specified range, from {min} to {max}");
                    return -1;
                }
            }
            else
            {
                Console.WriteLine("Input is not a number!");
                return -1;
            }
        }

        public static string GetPlacementCoordinates()
        {
            Console.Write("Type coordinates: ");
            string user_input = Console.ReadLine();
            string VALIDLETTERS = "ABCDEFGHIJ"; 
            string VALIDNUMBERS = "12345678910";
            if (user_input.Length == 2 && VALIDLETTERS.Contains(user_input.Substring(0, 1).ToUpper()) && 
                VALIDNUMBERS.Contains(user_input.Substring(1, 1).ToString().ToUpper()))
            {
                return user_input.ToUpper();
            }
            else
            {
                Console.WriteLine("Invalid coordinates!");
                return "";
            }
        }

        public static (int, int) ConvertToCoordinates(string coordinates)
        {
            string xString = coordinates.Substring(0, 1).ToString().ToUpper();
            int x;
            switch (xString)
            {
                case "A":
                    x = 0;
                    break;
                case "B":
                    x = 1;
                    break;
                case "C":
                    x = 2;
                    break;
                case "D":
                    x = 3;
                    break;
                case "E":
                    x = 4;
                    break;
                case "F":
                    x = 5;
                    break;
                case "G":
                    x = 6;
                    break;
                case "H":
                    x = 7;
                    break;
                case "I":
                    x = 8;
                    break;
                default:
                    x = 9;
                    break;
            }
            int y = int.Parse(coordinates.Substring(1, 1))-1;
            return (x, y);
        }

        public static string GetOrientation()
        {
            Display.Orientation();
            string user_input = Console.ReadLine();
            string VALIDLETTERS = "HV";
            if (user_input.Length == 1 && VALIDLETTERS.Contains(user_input.Substring(0, 1).ToUpper()))
            {
                return user_input.ToUpper();
            }
            else
            {
                Console.WriteLine("Invalid orientation!");
                return "";
            }
            throw new NotImplementedException();
        }

        public static Square.ShipType GetShipType()
        {
            int user_input = -1;
            while (user_input == -1)
            {
                Display.ShipTypes();
                user_input = ChooseMenuOptionInRange(1, 5);
            }

            Square.ShipType shipType;

            switch (user_input)
            {
                case 1:
                    shipType = Square.ShipType.Carrier;
                    break;
                case 2:
                    shipType = Square.ShipType.Cruiser;
                    break;
                case 3:
                    shipType = Square.ShipType.Battleship;
                    break;
                case 4:
                    shipType = Square.ShipType.Submarine;
                    break;
                default:
                    shipType = Square.ShipType.Destroyer;
                    break;
            }
            return shipType;
        }
    }
}
