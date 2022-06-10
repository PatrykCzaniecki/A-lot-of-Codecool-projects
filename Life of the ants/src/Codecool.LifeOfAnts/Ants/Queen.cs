using System;

namespace Codecool.LifeOfAnts.Ants
{
    public class Queen : Ant
    {
        public Queen(Position position)
        {
            Symbol = 'Q';
            Coordinates = position;
            _goodMoodCountdown = new Random().Next(10, 50);
        }

        public override string ToString()
        {
            return Symbol.ToString();
        }

        private int _goodMoodCountdown;

        public int GetGoodMoodCountdown()
        {
            return _goodMoodCountdown;
        }

        public bool IsInGoodMood()
        {
            if (_goodMoodCountdown == 0)
            {
                Console.WriteLine("The Queen is in mood for mating.");
                return true;
            }
            else
            {
                return false;
            }
        }

        public void Mate()
        {
            _goodMoodCountdown = new Random().Next(10, 50);
        }

        public override void MakeMove()
        {
            if (IsInGoodMood())
            {
                Mate();
            }
            else if (!IsInGoodMood() && _goodMoodCountdown != 0)
            {
                _goodMoodCountdown -= 1;
            }
            Console.WriteLine("The Queen will be in good mood for another mating in " + _goodMoodCountdown + " time steps.\n");
        }
    }
}
