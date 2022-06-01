using System;
using Codecool.LifeOfAnts.Colony;
using Codecool.LifeOfAnts.Img;

namespace Codecool.LifeOfAnts
{
    public static class Program
    {
        public static void Main()
        {
            View.PrintFile("Title.txt");
            View.PrintFile("Ant.txt");

            Console.WriteLine("Provide colony width: \n");
            var area = GetInput();
            AntColony colony = new AntColony(area);
            colony.CreateEmptyColony();

            Console.WriteLine("Provide number of workers: \n");
            var workers = GetInput();

            Console.WriteLine("Provide number of soldiers: \n");
            var soldiers = GetInput();

            Console.WriteLine("Provide number of drones: \n");
            var drones = GetInput();
            Console.Clear();

            colony.GenerateAnts(workers, soldiers, drones);
            Console.WriteLine("Hello, Ants!");
            Console.WriteLine("Press Enter to update the colony.\n");
            colony.PrintColony();
            Console.WriteLine("Colony statistics: \n");
            Console.WriteLine("All ants: " + (workers + drones + soldiers + 1));
            Console.WriteLine("Workers: " + workers + "\n" + "Soldiers: " + soldiers + "\n" + "Drones: " + drones + "\n" + "The Queen" + "\n");
            Console.WriteLine("Colony area: " + area + " X " + area);

            while (IsUpdated())
            {
                Console.Clear();
                Console.WriteLine("Mating status: \n");
                colony.UpdateAndPrintColony();
                Console.WriteLine("Colony statistics: \n");
                Console.WriteLine("All ants: " + (workers + drones + soldiers + 1));
                Console.WriteLine("Workers: " + workers + "\n" + "Soldiers: " + soldiers + "\n" + "Drones: " + drones + "\n" + "The Queen" + "\n");
                Console.WriteLine("Colony area: " + area + "X" + area + "\n");
                Console.WriteLine("Press Enter to update the colony. \nPress 'q' or 'Q' to finish the simulation. \n");
            }
        }

        public static bool IsUpdated()
        {
            var userInput = Console.ReadKey();

            if (userInput.Key == ConsoleKey.Enter)
            {
                return true;
            }
            else if (userInput.KeyChar == 'q' || userInput.KeyChar == 'Q')
            {
                return false;
            }
            return IsUpdated();
        }

        public static int GetInput()
        {
            var input = Console.ReadLine();
            while (!CheckIfInt(input))
            {
                Console.WriteLine("Your input must be a number: \n");
                input = Console.ReadLine();
            }
            return Int32.Parse(input);
        }

        public static bool CheckIfInt(string input)
        {
            if (Int32.TryParse(input, out _))
            {
                return true;
            }
            return false;
        }
    }
}
