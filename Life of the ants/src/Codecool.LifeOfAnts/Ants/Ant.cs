using Codecool.LifeOfAnts.Colony;

namespace Codecool.LifeOfAnts.Ants
{
    public abstract class Ant
    {
        public AntColony AntColony { get; set; }

        protected char Symbol { get; set; }

        protected Position Coordinates { get; set; }

        public abstract void MakeMove();

        public bool IsMoveValid(Position next)
        {
            if (next.X >= AntColony.GetWidth() || next.X < 0)
            {
                return false;
            }
            else if (next.Y >= AntColony.GetWidth() || next.Y < 0)
            {
                return false;
            }
            else
            {
                return true;
            }
        }

        public virtual Position GetPosition()
        {
            return Coordinates;
        }

        public virtual char GetSymbol()
        {
            return Symbol;
        }
    }
}
