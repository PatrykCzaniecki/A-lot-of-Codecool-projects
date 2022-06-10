using Codecool.LifeOfAnts.Geometry;

namespace Codecool.LifeOfAnts.Ants
{
    public class Worker : Ant
    {
        public Worker(Position position)
        {
            Symbol = 'W';
            Coordinates = position;
        }

        public override string ToString()
        {
            return Symbol.ToString();
        }

        public override void MakeMove()
        {
            var nextPosition = Coordinates.NextCoordinatesInDirection(DirectionExtensions.GetRandomDirection());

            while (!IsMoveValid(nextPosition))
            {
                nextPosition = Coordinates.NextCoordinatesInDirection(DirectionExtensions.GetRandomDirection());
            }
            Coordinates = nextPosition;
        }
    }
}
