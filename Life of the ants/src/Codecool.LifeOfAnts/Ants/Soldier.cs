namespace Codecool.LifeOfAnts.Ants
{
    public class Soldier : Ant
    {
        public Soldier(Position position)
        {
            Symbol = 'S';
            Coordinates = position;
        }

        public override string ToString()
        {
            return Symbol.ToString();
        }

        private Direction _lastStepDirection;

        public Direction GetNextDirection()
        {
            Direction nextDirection = _lastStepDirection;

            switch (_lastStepDirection)
            {
                case Direction.West:
                    nextDirection = Direction.South;
                    _lastStepDirection = Direction.South;
                    break;
                case Direction.East:
                    nextDirection = Direction.North;
                    _lastStepDirection = Direction.North;
                    break;
                case Direction.North:
                    nextDirection = Direction.West;
                    _lastStepDirection = Direction.West;
                    break;
                case Direction.South:
                    nextDirection = Direction.East;
                    _lastStepDirection = Direction.East;
                    break;
            }
            return nextDirection;
        }

        public override void MakeMove()
        {
            var nextPosition = Coordinates.NextCoordinatesInDirection(GetNextDirection());

            while (!IsMoveValid(nextPosition))
            {
                nextPosition = Coordinates.NextCoordinatesInDirection(GetNextDirection());
            }
            Coordinates = nextPosition;
        }
    }
}
